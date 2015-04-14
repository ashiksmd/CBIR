import wx
import math
import os.path

class Photo:
   def __init__(self, path, fName):
      self.img = wx.Image(path, wx.BITMAP_TYPE_ANY)
      self.name = fName

      #Histogram bins
      self.intBins = [0]*25
      self.ccBins = [0]*64

      #Image size
      (w,h) = self.img.GetSize()
      self.imgSize = w*h
      self.imgH = h
      self.imgW = w

      if(os.path.isfile('intBins/' + self.name + '.txt')):
         self.readIntBins()
      else:
         self.computeIntBins()

      if(os.path.isfile('ccBins/' + self.name + '.txt')):
         self.readCCBins()
      else:
         self.computeCCBins()

      #Scale and fit
      size = 260
      f = min(w,h)/float(size)
      if f > 0:
         self.scaled = self.img.Scale(w/f, h/f).Size((size,size), (0,0))
      else:
         self.scaled = self.img.Size((size, size), (0,0))

      #Distance to query image
      self.distance = 0

   def computeIntBins(self):
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

      self.writeIntBins()

   def computeCCBins(self):
      for i in range(0, self.imgW):
          for j in range(0, self.imgH):
             r = self.img.GetRed(i,j)
             g = self.img.GetGreen(i,j)
             b = self.img.GetBlue(i,j)

             bin = ((r >> 6) << 4) | ((g >> 6) << 2) | (b >> 6)

             #Add pixel to bin
             self.ccBins[bin]+=1

      self.writeCCBins()

   def writeIntBins(self):
       f = open('intBins/' + self.name + '.txt', 'w')
       for i in range(0, 25):
           f.write(str(self.intBins[i]) + ' ')
       
       f.close()

   def writeCCBins(self):
       f = open('ccBins/' + self.name + '.txt', 'w')
       for i in range(0, 64):
           f.write(str(self.ccBins[i]) + ' ')
       
       f.close()


   def readIntBins(self):
      f = open('intBins/' + self.name + '.txt', 'r')
      i = 0
      for line in f:
         for word in line.split():
            if word:
               self.intBins[i] = int(word)
               i+=1

      f.close()


   def readCCBins(self):
      f = open('ccBins/' + self.name + '.txt', 'r')
      i = 0
      for line in f:
         for word in line.split():
            if word:
               self.ccBins[i] = int(word)
               i+=1

      f.close()

   def computeIntDistance(self, img):
      self.distance = 0

      for i in range(0,25):
         self.distance += abs(self.intBins[i]/self.imgSize - img.intBins[i]/img.imgSize)

   def computeCCDistance(self, img):
      self.distance = 0

      for i in range(0,25):
         self.distance += abs(self.ccBins[i]/self.imgSize - img.ccBins[i]/img.imgSize)

