from Photo import Photo
import os

photoList = []

print 'imported photolist'

def initPhotoList():
   directory = 'images/'
   images = os.listdir(directory)
   images.sort()

   for f in images:
      if f.endswith('.jpg'):
         photoList.append(Photo(directory + f, f))


def computeCC():
   return None

def computeInt():
   return None


