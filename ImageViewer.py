import wx
from QueryImagePanel import QueryImagePanel
from ButtonsPanel import ButtonsPanel
from RightPanel import RightPanel
import PhotoList
import common

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

      vbox = wx.BoxSizer(wx.VERTICAL)
      hbox = wx.BoxSizer(wx.HORIZONTAL)

      #Top panel. Contains query image and some buttons
      leftPanel = wx.Panel(panel)

      #Panel to display the query image
      self.queryImagePanel = QueryImagePanel(leftPanel)
      common.queryImagePanel = self.queryImagePanel

      #Buttons
      self.buttonsPanel = ButtonsPanel(leftPanel)
      common.buttonsPanel = self.buttonsPanel 

      #Position the panels on screen
      vbox.Add(self.queryImagePanel, 2, wx.EXPAND | wx.ALL | wx.ALIGN_LEFT)
      vbox.Add(self.buttonsPanel, 1, wx.EXPAND | wx.ALL | wx.ALIGN_RIGHT)

      leftPanel.SetSizer(vbox)

      self.rightPanel = RightPanel(panel)

      hbox.Add(leftPanel, 0, wx.EXPAND | wx.ALL, 10)
      hbox.Add(self.rightPanel, 2, wx.EXPAND | wx.ALL, 10)

      panel.SetSizer(hbox)

   def OnQuit(self, e):
      self.Close()

if __name__ == '__main__':
   app = wx.App()
   ImageViewer(None, title='Image Viewer')
   app.MainLoop()
