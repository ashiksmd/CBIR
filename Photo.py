# Photo.py
# Contains all the information about a single photo
# Also contains methods for computing feature bins 
# and distance/similarity for each photo

import wx
import math
import os.path

class Photo:
   def __init__(self, path, fName, computeAndReturn=False):
      self.img = wx.Image(path, wx.BITMAP_TYPE_ANY)
      self.name = fName

      #Histogram bins
      self.intBins = [0]*25
      self.ccBins = [0]*64
      self.rfBins = [0]*89

      #Image size
      (w,h) = self.img.GetSize()
      self.imgSize = float(w*h)
      self.imgH = h
      self.imgW = w

      # Compute or read color histogram bins
      if (os.path.isfile('intBins/' + self.name + '.txt')):
         self.readIntBins()
      else:
         self.computeIntBins()

      if(os.path.isfile('ccBins/' + self.name + '.txt')):
         self.readCCBins()
      else:
         self.computeCCBins()

      # During pre-computation phase, just compute relevant parts and return
      if(computeAndReturn):
         return

      if(not os.path.isfile('rfBins/' + self.name + '.txt')):
         print 'Could not find Gaussian normalized features for ' + self.name + '.txt'
         print 'Compute by running: python PhotoList.py'
         exit
      else:
         self.readRFBins()

      #Scale and fit
      size = 104
      f = h/float(size)
      self.scaled = self.img.Scale(w/f, h/f)

      #Distance to query image
      self.distance = 0

   def computeIntBins(self):
      """
         Compute color histogram bins
         Uses intensity method
      """
      for i in range(0, self.imgW):
         for j in range(0, self.imgH):
             r = self.img.GetRed(i,j)
             g = self.img.GetGreen(i,j)
             b = self.img.GetBlue(i,j)

             intensity = 0.299 * r + 0.587 * g + 0.114 * b

             #Find the histogram bin this belongs to
             bin = int(intensity/10)
             if bin == 25: bin = 24  #Last bin is slightly larger

             #Add pixel to bin
             self.intBins[bin]+=1

      # Normalize by dividing by image size
      for i in range(0,25):
         self.intBins[i] /= self.imgSize

      # Write to file
      self.writeIntBins()

   def computeCCBins(self):
      """
         Compute color histogram bins
         Uses color codes method
      """
      for i in range(0, self.imgW):
          for j in range(0, self.imgH):
             r = self.img.GetRed(i,j)
             g = self.img.GetGreen(i,j)
             b = self.img.GetBlue(i,j)

             bin = ((r >> 6) << 4) | ((g >> 6) << 2) | (b >> 6)

             #Add pixel to bin
             self.ccBins[bin]+=1

      # Normalize by dividing by image size
      for i in range(0,64):
         self.ccBins[i] /= self.imgSize

      # Write to file
      self.writeCCBins()

   def writeIntBins(self):
       """ write histogram bins to file """
       f = open('intBins/' + self.name + '.txt', 'w')
       for i in range(0, 25):
           f.write(str(self.intBins[i]) + ' ')
       
       f.close()

   def writeCCBins(self):
       """ write histogram bins to file """
       f = open('ccBins/' + self.name + '.txt', 'w')
       for i in range(0, 64):
           f.write(str(self.ccBins[i]) + ' ')
       
       f.close()

   def writeRFBins(self):
       """ write histogram bins to file """
       f = open('rfBins/' + self.name + '.txt', 'w')
       for i in range(0, 89):
           f.write(str(self.rfBins[i]) + ' ')
       
       f.close()

   def readIntBins(self):
      """ Read histogram bins back from file """
      f = open('intBins/' + self.name + '.txt', 'r')
      i = 0
      for line in f:
         for word in line.split():
            if word:
               self.intBins[i] = float(word)
               i+=1

      f.close()

   def readCCBins(self):
      """ Read histogram bins back from file """
      f = open('ccBins/' + self.name + '.txt', 'r')
      i = 0
      for line in f:
         for word in line.split():
            if word:
               self.ccBins[i] = float(word)
               i+=1

      f.close()

   def readRFBins(self):
      """ Read histogram bins back from file """
      f = open('rfBins/' + self.name + '.txt', 'r')
      i = 0
      for line in f:
         for word in line.split():
            if word:
               self.rfBins[i] = float(word)
               i+=1

      f.close()

   def computeIntDistance(self, img):
      """
         Compute Manhattan-distance to img
         using intensity color histogram bins
      """
      self.distance = 0

      for i in range(0,25):
         self.distance += abs(self.intBins[i] - img.intBins[i])

   def computeCCDistance(self, img):
      """
         Compute Manhattan-distance to img
         using color codes histogram bins
      """
      self.distance = 0

      for i in range(0,64):
         self.distance += abs(self.ccBins[i] - img.ccBins[i])

   def computeRFDistance(self, img, weights):
      """
         Compute Manhattan-distance to img using the 
         combined and normalized feature histogram bins
      """
      self.distance = 0

      for i in range(0,89):
         self.distance += weights[i] * abs(self.rfBins[i] - img.rfBins[i])

   def __str__(self):
      return 'Photo: images/' + self.name

   def __hash__(self):
      return hash(str(self))

   def __eq__(self, other):
      if isinstance(other, self.__class__):
         return self.name == other.name
      else:
         return False

   def __ne__(self, other):
      return not self.__eq__(other)

