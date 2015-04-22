import wx

class ButtonsPanel(wx.Panel):
   def __init__(self, parent):
      super(ButtonsPanel, self).__init__(parent)

      #Choose an image
      self.browseButton = wx.Button(self, label='Change Image', size=(200, 30))
      #Find similar images using color codes method
      self.ccButton =  wx.Button(self, label='Color Coding', size=(200, 30))
      #Find similar images uing intensity method
      self.inButton =  wx.Button(self, label='Intensity', size=(200, 30))
      #Use intensity and color coding at the same time
      self.intCCButton = wx.Button(self, label='Intensity && Color Coding', size=(200,30))
      #Toggle Relevance Feedback
      self.rfToggle = wx.CheckBox(self, -1, 'Relevance Feedback', (10, 10))

      #Position buttons on screen
      vbox = wx.BoxSizer(wx.VERTICAL);
      vbox.Add(self.browseButton, 0, wx.ALIGN_CENTER | wx.TOP, 5)
      vbox.Add(self.ccButton, 0, wx.ALIGN_CENTER | wx.TOP, 5)
      vbox.Add(self.inButton, 0, wx.ALIGN_CENTER | wx.TOP, 5)
      vbox.Add(self.intCCButton, 0, wx.ALIGN_CENTER | wx.TOP, 5)
      vbox.Add(self.rfToggle, 0, wx.ALIGN_CENTER | wx.TOP, 5)

      self.SetSizer(vbox)

   def chooseImage(self):
      """ Choose new query image """
      openFileDialog = wx.FileDialog(self, "Choose Image", "images/", "1.jpg",
                                       "Jpeg files (*.jpg)|*.jpg", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_PREVIEW )

      if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return None    # the user did not choose a file

      #We have a file
      return openFileDialog.GetPath()
