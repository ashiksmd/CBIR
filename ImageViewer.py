import wx

class ImageViewer(wx.Frame):
   def __init__(self, parent, title):
      super(ImageViewer, self).__init__(parent, title=title)

      self.initUI()
      self.Maximize()
      self.Show()

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

      queryImagePanel = wx.Panel(topPanel)

      buttonsPanel = wx.Panel(topPanel)
      #Choose an image
      browseButton = wx.Button(buttonsPanel, label='Change Image', size=(100, 30))
      #Find similar images using color codes method
      ccButton =  wx.Button(buttonsPanel, label='Color Coding', size=(100, 30))
      #Find similar images uing intensity method
      inButton =  wx.Button(buttonsPanel, label='Intensity', size=(100, 30))

      #When 'Choose Image' button is clicked
      self.Bind(wx.EVT_BUTTON, self.chooseImage, browseButton)

      #Position buttons on screen
      vbox2 = wx.BoxSizer(wx.VERTICAL);
      vbox2.Add(browseButton, 0, wx.ALIGN_CENTER | wx.TOP, 20)
      vbox2.Add(ccButton, 0, wx.ALIGN_CENTER | wx.TOP, 5)
      vbox2.Add(inButton, 0, wx.ALIGN_CENTER | wx.TOP, 5)

      buttonsPanel.SetSizer(vbox2)

      hbox.Add(queryImagePanel, 2, wx.EXPAND | wx.ALL | wx.ALIGN_LEFT, 2)
      hbox.Add(buttonsPanel, 1, wx.EXPAND | wx.ALL | wx.ALIGN_RIGHT, 2)

      topPanel.SetSizer(hbox)

      resultsPanel = wx.Panel(panel)
      resultsPanel.SetBackgroundColour('#ffffff')

      vbox.Add(topPanel, 1, wx.EXPAND | wx.ALL, 5)
      vbox.Add(resultsPanel, 2, wx.EXPAND | wx.ALL, 5)

      panel.SetSizer(vbox)

      #Placeholder text
      font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
      font.SetPointSize(9)
      st1 = wx.StaticText(queryImagePanel, label='Query Image')
      st1.SetFont(font)
      st3 = wx.StaticText(resultsPanel, label='Results')
      st3.SetFont(font)

   def chooseImage(self, e):
      openFileDialog = wx.FileDialog(self, "Choose Image", "images/", "1.jpg",
                                       "Jpeg files (*.jpg)|*.jpg", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_PREVIEW | wx.FD_CHANGE_DIR)

      if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return     # the user did not choose a file

      #We have a file
      print openFileDialog.GetPath()

   def OnQuit(self, e):
      self.Close()

if __name__ == '__main__':
   app = wx.App()
   ImageViewer(None, title='Image Viewer')
   app.MainLoop()
