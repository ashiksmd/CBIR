import wx
import math

class QueryImagePanel(wx.Panel):
   def __init__(self, parent):
      super(QueryImagePanel, self).__init__(parent)

      self.updateQueryImage('images/1.jpg')

   def updateQueryImage(self, queryImage):
      self.queryImage = queryImage 

      #Load image
      img = wx.Image(queryImage, wx.BITMAP_TYPE_ANY)

      #Display
      wx.StaticBitmap(self, -1, img.ConvertToBitmap(), self.GetPosition(), img.GetSize())
