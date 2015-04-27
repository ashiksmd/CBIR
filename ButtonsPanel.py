import wx
from PageControl import PageControl
import common
import PhotoList

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
      #Page controls
      self.pageControls = PageControl(self) 
      common.pageControls = self.pageControls

      #Button events
      self.Bind(wx.EVT_BUTTON, self.chooseImage, self.browseButton)
      self.Bind(wx.EVT_BUTTON, self.computeInt, self.inButton)
      self.Bind(wx.EVT_BUTTON, self.computeCC, self.ccButton)
      self.Bind(wx.EVT_BUTTON, self.computeRF, self.intCCButton)

      #Checkbox event
      self.Bind(wx.EVT_CHECKBOX, self.toggleRF, self.rfToggle)

      #Position buttons on screen
      vbox = wx.BoxSizer(wx.VERTICAL);
      vbox.Add(self.browseButton, 0, wx.ALIGN_CENTER | wx.TOP, 5)
      vbox.Add(self.ccButton, 0, wx.ALIGN_CENTER | wx.TOP, 5)
      vbox.Add(self.inButton, 0, wx.ALIGN_CENTER | wx.TOP, 5)
      vbox.Add(self.intCCButton, 0, wx.ALIGN_CENTER | wx.TOP, 5)
      vbox.Add(self.rfToggle, 0, wx.ALIGN_CENTER | wx.TOP, 5)
      vbox.Add(self.pageControls, 0, wx.ALIGN_CENTER, 5)

      self.SetSizer(vbox)

   def chooseImage(self, e):
      """ Choose new query image """
      openFileDialog = wx.FileDialog(self, "Choose Image", "images/", "1.jpg",
                                       "Jpeg files (*.jpg)|*.jpg", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_PREVIEW )

      if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return     # the user did not choose a file

      #We have a file
      common.queryImagePanel.updateQueryImage(openFileDialog.GetPath())

   def computeInt(self, e ):
      """ Compute results using intensity method """
      PhotoList.computeInt(common.queryImagePanel.queryImage)
      common.pageControls.gotoFirst(None, False)

   def computeCC(self, e):
      """ Compute results using color coding method """
      PhotoList.computeCC(common.queryImagePanel.queryImage)
      common.pageControls.gotoFirst(None, False)

   def computeRF(self, e):
      """
         Compute results using both intensity and color coding
         and then apply Relevance Feedback
      """
      PhotoList.computeRF(common.queryImagePanel.queryImage)
      common.pageControls.gotoFirst(None, False)

   def toggleRF(self, e):
      rfOn = self.rfToggle.IsChecked()
      if(rfOn):
          self.inButton.Disable()
          self.ccButton.Disable()
      else:
          self.inButton.Enable()
          self.ccButton.Enable()

      self.pageControls.refreshPage()

