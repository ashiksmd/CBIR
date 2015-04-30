from Photo import Photo
import os

# List of photos. 100 objects
photoList = []

# List of photos marked as relevant
relevantPhotos = set()

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

def computeStats(photos):
   mean = [0]*89
   sd = [0]*89
   minNonZeroSD = float('inf')

   for i in range(0, 89):
      sum = 0; variance = 0

      # Find mean
      for photo in photos:
         sum += photo.rfBins[i]

      mean[i] = sum / len(photos)

      # Find variance
      for photo in photos:
         variance += (photo.rfBins[i] - mean[i]) ** 2

      # Find standard deviation
      sd[i] = variance ** 0.5

      #Find minimum non zero standard deviation
      if(sd[i] != 0 and sd[i] < minNonZeroSD):
         minNonZeroSD = sd[i]

   return (mean,sd, minNonZeroSD)

def computeWeights():
   """
      Compute feature weights with current set of relevant images
   """
   (mean, sd, minNonZeroSD) = computeStats(list(relevantPhotos))
   weights = [1]*89
   for i in range(0,89):
      if sd[i] == 0 and mean[i] == 0:
         weights[i] = 0
      elif sd[i] == 0:
         weights[i] = 2 / minNonZeroSD
      else:
         weights[i] = 1 / sd[i]

   # Get sum of weights
   sum = 0
   for i in range(0, 89):
      sum += weights[i]

   # Normalize weights
   for i in range(0, 89):
      weights[i] /= sum

   return weights

def computeRF(queryImage):
   """
      Re-order photoList using similarity of images
      Uses both intensity and color coding histograms
      Uses Relevance Feedback
   """
   _,fName = os.path.split(queryImage)

   query = Photo(queryImage, fName)

   if not relevantPhotos:
      weights = [1/89.0]*89 # Feature weights
   else:
      # Add query image to relevant photos if not already marked so
      relevantPhotos.add(query)
      # Compute feature weights using the list of relevant photos
      weights = computeWeights()

   for photo in photoList:
      photo.computeRFDistance(query, weights)

   # Sort using the computed distance values
   photoList.sort(key=lambda x: x.distance)

def normalizeResults():
   """
      After loading all images and initializing their color histograms,
      use Gaussian normalization for feature normalization
   """
   for i in range(0, 25):
      sum = 0; variance = 0

      # Find mean
      for photo in photoList:
         sum += photo.intBins[i]

      mean = sum / len(photoList)

      # Find variance
      for photo in photoList:
         variance += (photo.intBins[i] - mean) ** 2

      # Find standard deviation
      sd = variance ** 0.5

      for photo in photoList:
         if sd == 0:
            photo.rfBins[i] = mean
         else:
            photo.rfBins[i] = (photo.intBins[i] - mean) / sd

   for i in range(0, 64):
      j = 25 + i

      sum = 0; variance = 0

      # Find mean
      for photo in photoList:
         sum += photo.ccBins[i]

      mean = sum / len(photoList)

      # Find variance
      for photo in photoList:
         variance += (photo.ccBins[i] - mean) ** 2

      # Find standard deviation
      sd = variance ** 0.5

      for photo in photoList:
         if sd == 0:
            photo.rfBins[j] = mean
         else:
            photo.rfBins[j] = (photo.ccBins[i] - mean) / sd

def updateRelevantPhotos(photoName, relevant):
   """
      Update the list of relevant photos
      photo - The photo to add/remove from list
      relevant - true/false
   """
   photo = Photo('images/'+photoName, photoName)
   if(relevant):
      relevantPhotos.add(photo)
   else:
      relevantPhotos.discard(photo)

if __name__ == "__main__":
   print 'Re-computing Gaussian normalized features'

   initPhotoList(True)
   normalizeResults()

   # Write normalized features to disk
   for photo in photoList:
      photo.writeRFBins()

