from Photo import Photo
import os

# List of photos. 100 objects
photoList = []

def initPhotoList(computeAndReturn=False):
   """ Load all the images in the directory and initialize """

   directory = 'images/'

   # Read all files in directory
   images = os.listdir(directory)
   images.sort()

   # Use all jpg files in the directory
   for f in images:
      if f.endswith('.jpg'):
         photoList.append(Photo(directory + f, f, computeAndReturn))

def computeCC(queryImage):
   """
      Re-order photoList using similarity of images
      Uses color coding histogram method
   """
   _,fName = os.path.split(queryImage)

   query = Photo(queryImage, fName)
   for photo in photoList:
      photo.computeCCDistance(query)

   # Sort using the computed distance values
   photoList.sort(key=lambda x: x.distance)

def computeInt(queryImage):
   """
      Re-order photoList using similarity of images
      Uses intensity color histogram method
   """
   _,fName = os.path.split(queryImage)

   query = Photo(queryImage, fName)
   for photo in photoList:
      photo.computeIntDistance(query)

   # Sort using the computed distance values
   photoList.sort(key=lambda x: x.distance)

def computeRF(queryImage):
   """
      Re-order photoList using similarity of images
      Uses both intensity and color coding histograms
      Uses Relevance Feedback
   """
   _,fName = os.path.split(queryImage)

   query = Photo(queryImage, fName)
   weights = [1/89.0]*89 # Feature weights

   for photo in photoList:
      photo.computeRFDistance(query, weights)

   # Sort using the computed distance values
   photoList.sort(key=lambda x: x.distance)

def normalizeResults():
   """
      After loading all images and initializing their color histograms,
      use Gaussian normalization for feature normalization
   """
   # Normalize intensity histograms
   for i in range(0, 25):
      sum = 0; variance = 0

      # Find mean
      for photo in photoList:
         sum += photo.intBins[i]

      mean = sum / 25.0

      # Find variance
      for photo in photoList:
         variance += (photo.intBins[i] - mean) ** 2

      # Find standard deviation
      sd = variance ** 0.5
     
      # Update normalized values
      for photo in photoList:
         if sd == 0:
            photo.rfBins[i] = mean
         else:
            photo.rfBins[i] = (photo.intBins[i] - mean) / sd

   # Do the same for color code histograms
   for i in range(0, 64):
      sum = 0; variance = 0

      # Find mean
      for photo in photoList:
         sum += photo.ccBins[i]

      mean = sum / 64.0

      # Find variance
      for photo in photoList:
         variance += (photo.ccBins[i] - mean) ** 2

      # Find standard deviation
      sd = variance ** 0.5

      # Update normalized values
      for photo in photoList:
         if sd == 0:
            photo.rfBins[25 + i] = mean
         else:
            photo.rfBins[25 + i] = (photo.ccBins[i] - mean) / sd

if __name__ == "__main__":
   print 'Re-computing Gaussian normalized features'

   initPhotoList(True)
   normalizeResults()

   # Write normalized features to disk
   for photo in photoList:
      photo.writeRFBins()

