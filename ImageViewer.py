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
      wx.CallAfter(self.initUI)

   def initUI(self):
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

      #Position the panels on screen
      hbox.Add(self.queryImagePanel, 2, wx.EXPAND | wx.ALL | wx.ALIGN_LEFT)
      hbox.Add(self.buttonsPanel, 1, wx.EXPAND | wx.ALL | wx.ALIGN_RIGHT)

      topPanel.SetSizer(hbox)

      bottomPanel = BottomPanel(panel, self.GetSize())

      vbox.Add(topPanel, 1, wx.EXPAND | wx.ALL, 5)
      vbox.Add(bottomPanel, 2, wx.EXPAND | wx.ALL)

      panel.SetSizer(vbox)

   def chooseImage(self, e):
      path = self.buttonsPanel.chooseImage()
      if path is not None:
         self.queryImagePanel.updateQueryImage(path)
 
   def OnQuit(self, e):
      self.Close()

if __name__ == '__main__':
   app = wx.App()
   ImageViewer(None, title='Image Viewer')
   app.MainLoop()
