import wx
import wx.lib.scrolledpanel as scrolled
import PhotoList
from ThumbnailsPanel import ThumbnailsPanel

class ResultsPanel(scrolled.ScrolledPanel):
   def __init__(self, parent, start, end):
      super(ResultsPanel, self).__init__(parent, size=(1366,200))

      self.grid = wx.GridSizer(4, 5, 0, 0)
      
      self.thumbs = []
      self.updateResults(start, end)

   def updateResults(self, start, end):
      for i in range(len(self.thumbs)):
          self.thumbs[i].Destroy()

      self.thumbs = []

      for photo in PhotoList.photoList[start:end]:
         thumbnailsPanel = ThumbnailsPanel(self, photo)
         self.thumbs.append(thumbnailsPanel)
         self.grid.Add(thumbnailsPanel, 0, wx.ALL)

      self.SetSizer(self.grid)
      self.SetAutoLayout(1)
      self.SetupScrolling() 
