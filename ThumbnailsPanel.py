import wx

class ThumbnailsPanel(wx.Panel):
   def __init__(self, parent, photo):
      super(ThumbnailsPanel, self).__init__(parent)

      vbox = wx.BoxSizer(wx.VERTICAL)

      img = photo.scaled
      
      bmp = wx.StaticBitmap(self, -1, img.ConvertToBitmap(), self.GetPosition(), img.GetSize())
      fName = wx.StaticText(self, label=photo.name)

      vbox.Add(bmp, 0, wx.ALL, 1)
      vbox.Add(fName, 0, wx.ALL, 1)

      self.SetSizer(vbox)
