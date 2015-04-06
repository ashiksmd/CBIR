import wx
import math

class QueryImagePanel(wx.Panel):
   def __init__(self, parent):
      super(QueryImagePanel, self).__init__(parent)
      self.displayedImage = None

      self.updateQueryImage('images/1.jpg')

   def scaleImage(self, img):
      size = 250
      (w,h) = img.GetSize()
      print w,h
      f = h/float(size)

      if f > 0:
         scaled = img.Scale(w/f, h/f)
      else:
         scaled = img

      return scaled

   def updateQueryImage(self, queryImage):
      self.queryImage = queryImage 

      #Load image
      img = self.scaleImage(wx.Image(queryImage, wx.BITMAP_TYPE_ANY))
     
      #Display
      if self.displayedImage is not None:
         self.displayedImage.Destroy()

      self.displayedImage = wx.StaticBitmap(self, -1, img.ConvertToBitmap(), self.GetPosition(), img.GetSize())
