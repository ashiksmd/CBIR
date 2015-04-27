import wx
from wx.lib import buttons
import common

class ThumbnailsPanel(wx.Panel):
   def __init__(self, parent, photo, rfState=False):
      super(ThumbnailsPanel, self).__init__(parent)

      vbox = wx.BoxSizer(wx.VERTICAL)
      hbox = wx.BoxSizer(wx.HORIZONTAL)

      self.photoName = photo.name

      # Image to display
      img = photo.scaled
      bmp = wx.BitmapButton(self, -1, img.ConvertToBitmap(), self.GetPosition(), img.GetSize())

      #When clicked, do this
      self.Bind(wx.EVT_BUTTON, self.updateQueryImage, bmp) 

      # File name
      fName = wx.StaticText(self, label=photo.name)

      #Relevance checkbox
      if(rfState):
         self.relevanceCB = wx.CheckBox(self, -1, 'Relevant', (10,10))     
      vbox.Add(bmp, 0, wx.ALIGN_CENTER, 1)
      hbox.Add(fName, 0, wx.ALL, 1)
      if(rfState):
          hbox.Add(self.relevanceCB, 0, wx.ALL, 1)

      vbox.Add(hbox, 0, wx.ALIGN_CENTER, 1)
      self.SetSizer(vbox)

   def updateQueryImage(self, e):
      common.queryImagePanel.updateQueryImage('images/' + self.photoName)

