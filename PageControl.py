# PageControl.py
# Contains components for navigating between pages of search results

import wx
import common

class PageControl(wx.Panel):
   def __init__(self, parent):
      super(PageControl, self).__init__(parent)

      self.total = 100    # 100 images in total
      self.page = 1       # Start on page 1
      self.pageSize = 20  # 20 images in each page
      pages = ['1','2','3','4','5']

      hbox = wx.BoxSizer(wx.HORIZONTAL)

      #Buttons
      self.firstPage = wx.Button(self, label='First', size=(50,30))
      self.prevPage = wx.Button(self, label='Prev', size=(50,30))
      self.currPage = wx.ComboBox(self, size=(50, 30), choices=pages, value='1', style=wx.CB_READONLY)
      self.nextPage = wx.Button(self, label='Next', size=(50,30))
      self.lastPage = wx.Button(self, label='Last', size=(50,30))

      #Position the buttons
      hbox.Add(self.firstPage, 0, wx.ALL | wx.ALIGN_RIGHT, 1)
      hbox.Add(self.prevPage, 0, wx.ALL | wx.ALIGN_RIGHT, 1)
      hbox.Add(self.currPage, 0, wx.ALL | wx.ALIGN_RIGHT, 1)
      hbox.Add(self.nextPage, 0, wx.ALL | wx.ALIGN_RIGHT, 1)
      hbox.Add(self.lastPage, 0, wx.ALL | wx.ALIGN_RIGHT, 1)

      self.SetSizer(hbox)

      #Button events
      self.Bind(wx.EVT_BUTTON, self.gotoFirst, self.firstPage)
      self.Bind(wx.EVT_BUTTON, self.gotoPrev, self.prevPage)
      self.Bind(wx.EVT_BUTTON, self.gotoNext, self.nextPage)
      self.Bind(wx.EVT_BUTTON, self.gotoLast, self.lastPage)
      self.Bind(wx.EVT_COMBOBOX, self.gotoPage, self.currPage)

   def refreshPage(self):
      """ Refresh display with images from current page """
      self.currPage.SetSelection(self.page - 1)

      start = self.pageSize * (self.page - 1)
      end = start + self.pageSize

      common.resultsPanel.updateResults(start, end)

   def gotoFirst(self, e, ignoreIfAtFirst=True):
      """Go to the first page of search results"""
      if (self.page == 1 and ignoreIfAtFirst): return

      self.page = 1
      self.refreshPage()
      
   def gotoPrev(self, e):
      """Go to previous page of search results"""
      if (self.page == 1): return

      self.page = self.page - 1
      self.refreshPage()

   def gotoNext(self, e):
      """Go to next page of search results"""
      if (self.page == 5): return

      self.page = self.page + 1
      self.refreshPage()

   def gotoLast(self, e):
      """Go to the last page of search results"""
      if (self.page == 5): return

      self.page = 5
      self.refreshPage()

   def gotoPage(self, e):
      """Go to the selected page of search results"""
      page = self.currPage.GetSelection() + 1
      if (self.page == page): return

      self.page = page
      self.refreshPage()
