import wx
from PageControl import PageControl
from ResultsPanel import ResultsPanel

class BottomPanel(wx.Panel):
   def __init__(self, parent):
      super(BottomPanel, self).__init__(parent)

      vbox = wx.BoxSizer(wx.VERTICAL)

      # Page control to view results
      self.pageControls = PageControl(self, self.updateResults, self) 
      vbox.Add(self.pageControls, 0, wx.ALL | wx.ALIGN_RIGHT, 1)

      # Results will be displayed here
      self.resultsPanel = ResultsPanel(self, 0, 20)
      vbox.Add(self.resultsPanel, wx.ALL)

      self.SetSizer(vbox)

   def updateResults(self, context, start, end):
      """
         Display the results
         Can display a range of images from the result
         start, end - used for pagination
         context - BottomPanel object. Useful when called from other scopes
      """
      context.resultsPanel.updateResults(start, end) 

