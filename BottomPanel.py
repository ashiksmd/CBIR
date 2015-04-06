import wx
from PageControl import PageControl
from ResultsPanel import ResultsPanel

class BottomPanel(wx.Panel):
   def __init__(self, parent, wSize):
      super(BottomPanel, self).__init__(parent)

      vbox = wx.BoxSizer(wx.VERTICAL)

      self.pageControls = PageControl(self, self.updateResults, self) 
      vbox.Add(self.pageControls, 0, wx.ALL | wx.ALIGN_RIGHT, 1)

      self.resultsPanel = ResultsPanel(self, 0, 20, wSize)
      vbox.Add(self.resultsPanel, wx.ALL)

      self.SetSizer(vbox)

   def updateResults(self, context, start, end):
      context.resultsPanel.updateResults(start, end) 
