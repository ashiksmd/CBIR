import wx
import math

class QueryImagePanel(wx.Panel):
   def __init__(self, parent):
      super(QueryImagePanel, self).__init__(parent)
      self.displayedImage = None

      # Set 1.jpg as query image at app start
      self.updateQueryImage('images/1.jpg')

   def updateQueryImage(self, queryImage):
      """
         Set query image for computation
         Also displays the image
      """
      self.queryImage = queryImage 

      #Load image
      img = wx.Image(queryImage, wx.BITMAP_TYPE_ANY)

      #Display
      if self.displayedImage is not None:
         self.displayedImage.Destroy()

      self.displayedImage = wx.StaticBitmap(self, -1, img.ConvertToBitmap(), self.GetPosition(), img.GetSize())
