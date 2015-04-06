import wx
import math

class Photo:
   def __init__(self, path, fName):
      self.img = wx.Image(path, wx.BITMAP_TYPE_ANY)
      self.name = fName

      (w,h) = self.img.GetSize()

      size = 260

      f = min(w,h)/float(size)
      if f > 0:
         self.scaled = self.img.Scale(w/f, h/f).Size((size,size), (0,0))
      else:
         self.scaled = self.img.Size((size, size), (0,0))
