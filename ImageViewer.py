import wx

class ImageViewer(wx.Frame):
   def __init__(self, parent, title):
      super(ImageViewer, self).__init__(parent, title=title)

      self.initUI()
      self.Maximize()
      self.Show()

   def initUI(self):
      menuBar = wx.MenuBar()
      fileMenu = wx.Menu()

      exitMenuItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
      menuBar.Append(fileMenu, '&File')
      self.SetMenuBar(menuBar)

      self.Bind(wx.EVT_MENU, self.OnQuit, exitMenuItem)

      panel = wx.Panel(self)
      panel.SetBackgroundColour('#4f5049')

      vbox = wx.BoxSizer(wx.VERTICAL)
      hbox = wx.BoxSizer(wx.HORIZONTAL)

      topPanel = wx.Panel(panel)
      topPanel.SetBackgroundColour('#ededed')

      queryImagePanel = wx.Panel(topPanel)
      queryImagePanel.SetBackgroundColour('#0000ff')

      buttonsPanel = wx.Panel(topPanel)
      buttonsPanel.SetBackgroundColour('#ff0000')

      hbox.Add(queryImagePanel, 2, wx.EXPAND | wx.ALL | wx.ALIGN_LEFT, 2)
      hbox.Add(buttonsPanel, 1, wx.EXPAND | wx.ALL | wx.ALIGN_RIGHT, 2)

      topPanel.SetSizer(hbox)

      resultsPanel = wx.Panel(panel)
      resultsPanel.SetBackgroundColour('#ffffff')

      vbox.Add(topPanel, 1, wx.EXPAND | wx.ALL, 5)
      vbox.Add(resultsPanel, 2, wx.EXPAND | wx.ALL, 5)

      panel.SetSizer(vbox)

      font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
      font.SetPointSize(9)
      st1 = wx.StaticText(queryImagePanel, label='Query Image')
      st1.SetFont(font)
      st2 = wx.StaticText(buttonsPanel, label='Buttons')
      st2.SetFont(font)
      st3 = wx.StaticText(resultsPanel, label='Results')
      st3.SetFont(font)

   def OnQuit(self, e):
      self.Close()

if __name__ == '__main__':
   app = wx.App()
   ImageViewer(None, title='Image Viewer')
   app.MainLoop()
