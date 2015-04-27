import wx
import math

class QueryImagePanel(wx.Panel):
   def __init__(self, parent):
      super(QueryImagePanel, self).__init__(parent)
      self.displayedImage = None

      # Set 1.jpg as query image at app start
      self.updateQueryImage('images/1.jpg')

   def scaleImage(self, img):
      """ Scale down image to fit in grid """
      size = 200.0
      (w,h) = img.GetSize()
      f = w/size

      if f > 1:
         scaled = img.Scale(w/f, h/f)
      else:
         scaled = img

      return scaled

   def updateQueryImage(self, queryImage):
      """
         Set query image for computation
         Also displays the image
      """
      self.queryImage = queryImage 

      #Load image
      #img = self.scaleImage(wx.Image(queryImage, wx.BITMAP_TYPE_ANY))
      img = wx.Image(queryImage, wx.BITMAP_TYPE_ANY)

      #Display
      if self.displayedImage is not None:
         self.displayedImage.Destroy()

      self.displayedImage = wx.StaticBitmap(self, -1, img.ConvertToBitmap(), self.GetPosition(), img.GetSize())
