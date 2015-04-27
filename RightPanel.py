import wx
from PageControl import PageControl
from ResultsPanel import ResultsPanel
import common

class RightPanel(wx.Panel):
   def __init__(self, parent):
      super(RightPanel, self).__init__(parent)

      vbox = wx.BoxSizer(wx.VERTICAL)
      
      # Results will be displayed here
      self.resultsPanel = ResultsPanel(self, 0, 20)
      common.resultsPanel = self.resultsPanel

      vbox.Add(self.resultsPanel, wx.ALL)

      self.SetSizer(vbox)
