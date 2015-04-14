from Photo import Photo
import os

photoList = []

def initPhotoList():
   directory = 'images/'
   images = os.listdir(directory)
   images.sort()

   for f in images:
      if f.endswith('.jpg'):
         photoList.append(Photo(directory + f, f))


def displayPhotos():
   print '\nPhotos:'
   for photo in photoList:
      print photo.name

def computeCC(queryImage):
   _,fName = os.path.split(queryImage)

   query = Photo(queryImage, fName)
   for photo in photoList:
      photo.computeIntDistance(query)

   displayPhotos()
   photoList.sort(key=lambda x: x.distance)
   displayPhotos()

def computeInt(queryImage):
   _,fName = os.path.split(queryImage)

   query = Photo(queryImage, fName)
   for photo in photoList:
      photo.computeIntDistance(query)

   photoList.sort(key=lambda x: x.distance)



