import wx
from QueryImagePanel import QueryImagePanel
from ButtonsPanel import ButtonsPanel
from BottomPanel import BottomPanel
import PhotoList

class ImageViewer(wx.Frame):
   def __init__(self, parent, title):
      super(ImageViewer, self).__init__(parent, title=title)

      PhotoList.initPhotoList()
      self.Maximize()
      self.Show()
      self.initUI()

   def initUI(self):
      """ Initialize the UI """
      #Create menu bar with a quit option
      menuBar = wx.MenuBar()
      fileMenu = wx.Menu()

      exitMenuItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
      menuBar.Append(fileMenu, '&File')
      self.SetMenuBar(menuBar)

      self.Bind(wx.EVT_MENU, self.OnQuit, exitMenuItem)

      #Main panel
      panel = wx.Panel(self)
      panel.SetBackgroundColour('#4f5049')

      vbox = wx.BoxSizer(wx.VERTICAL)
      hbox = wx.BoxSizer(wx.HORIZONTAL)

      #Top panel. Contains query image and some buttons
      topPanel = wx.Panel(panel)
      topPanel.SetBackgroundColour('#ededed')

      #Panel to display the query image
      self.queryImagePanel = QueryImagePanel(topPanel)

      #Buttons
      self.buttonsPanel = ButtonsPanel(topPanel)
      
      #Button events
      self.Bind(wx.EVT_BUTTON, self.chooseImage, self.buttonsPanel.browseButton)
      self.Bind(wx.EVT_BUTTON, self.computeInt, self.buttonsPanel.inButton)
      self.Bind(wx.EVT_BUTTON, self.computeCC, self.buttonsPanel.ccButton)

      #Checkbox event
      self.Bind(wx.EVT_CHECKBOX, self.toggleRF, self.buttonsPanel.rfToggle)

      #Position the panels on screen
      hbox.Add(self.queryImagePanel, 2, wx.EXPAND | wx.ALL | wx.ALIGN_LEFT)
      hbox.Add(self.buttonsPanel, 1, wx.EXPAND | wx.ALL | wx.ALIGN_RIGHT)

      topPanel.SetSizer(hbox)

      self.bottomPanel = BottomPanel(panel)

      vbox.Add(topPanel, 0, wx.EXPAND | wx.ALL, 5)
      vbox.Add(self.bottomPanel, 2, wx.EXPAND | wx.ALL)

      panel.SetSizer(vbox)

   def chooseImage(self, e):
      """ Choose a new query image """
      path = self.buttonsPanel.chooseImage()
      if path is not None:
         self.queryImagePanel.updateQueryImage(path)
 
   def toggleRF(self, e):
      rfOn = self.buttonsPanel.rfToggle.IsChecked()
      if(rfOn):
          self.buttonsPanel.inButton.Disable()
          self.buttonsPanel.ccButton.Disable()
      else:
          self.buttonsPanel.inButton.Enable()
          self.buttonsPanel.ccButton.Enable()

      self.bottomPanel.toggleRFOption(rfOn)

   def computeInt(self, e ):
      """ Compute results using intensity method """
      PhotoList.computeInt(self.queryImagePanel.queryImage)
      self.bottomPanel.pageControls.gotoFirst(None, False)

   def computeCC(self, e):
      """ Compute results using color coding method """
      PhotoList.computeCC(self.queryImagePanel.queryImage)
      self.bottomPanel.pageControls.gotoFirst(None, False)

   def OnQuit(self, e):
      self.Close()

if __name__ == '__main__':
   app = wx.App()
   ImageViewer(None, title='Image Viewer')
   app.MainLoop()
