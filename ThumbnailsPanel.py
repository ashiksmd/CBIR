# ThumbnailsPanel.py
# Displays a single image as a thumbnail in the results section
# Also includes the file name and the checkbox to mark it as relevant

import wx
import PhotoList
import common

class ThumbnailsPanel(wx.Panel):
   def __init__(self, parent, photo, rfState=False):
      super(ThumbnailsPanel, self).__init__(parent)

      vbox = wx.BoxSizer(wx.VERTICAL)
      hbox = wx.BoxSizer(wx.HORIZONTAL)

      self.photoName = photo.name

      # Image to display
      img = photo.scaled
      bmp = wx.BitmapButton(self, -1, img.ConvertToBitmap(), self.GetPosition(), img.GetSize())

      #When clicked, do this
      self.Bind(wx.EVT_BUTTON, self.updateQueryImage, bmp) 

      # File name
      fName = wx.StaticText(self, label=photo.name)

      #Relevance checkbox
      if(rfState):
         self.relevanceCB = wx.CheckBox(self, -1, 'Relevant', (10,10))
         if photo in PhotoList.relevantPhotos:
            self.relevanceCB.SetValue(True)

      vbox.Add(bmp, 0, wx.ALIGN_CENTER, 1)
      hbox.Add(fName, 0, wx.ALL, 1)
      if(rfState):
          hbox.Add(self.relevanceCB, 0, wx.ALL, 1)
          self.Bind(wx.EVT_CHECKBOX, self.markRelevant, self.relevanceCB)

      vbox.Add(hbox, 0, wx.ALIGN_CENTER, 1)
      self.SetSizer(vbox)

   def updateQueryImage(self, e):
      """If a thumbnail is clicked, the image is set as the new query image"""
      common.queryImagePanel.updateQueryImage('images/' + self.photoName)

   def markRelevant(self, e):
      """Mark this image as relevant for next iteration"""
      state = self.relevanceCB.IsChecked()
      PhotoList.updateRelevantPhotos(self.photoName, state)
