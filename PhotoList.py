from Photo import Photo
import os

# List of photos. 100 objects
photoList = []

def initPhotoList():
   """ Load all the images in the directory and initialize """

   directory = 'images/'

   # Read all files in directory
   images = os.listdir(directory)
   images.sort()

   # Use all jpg files in the directory
   for f in images:
      if f.endswith('.jpg'):
         photoList.append(Photo(directory + f, f))

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

