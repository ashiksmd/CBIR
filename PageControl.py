import wx

class PageControl(wx.Panel):
   def __init__(self, parent, updateFunc, context):
      super(PageControl, self).__init__(parent)

      self.updateFunc = updateFunc
      self.context = context

      self.total = 100
      self.page = 1
      self.pageSize = 20
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
      self.currPage.SetSelection(self.page - 1)

      start = self.pageSize * (self.page - 1)
      end = start + self.pageSize

      self.updateFunc(self.context, start, end)

   def gotoFirst(self, e):
      if (self.page == 1): return

      self.page = 1
      self.refreshPage()
      
   def gotoPrev(self, e):
      if (self.page == 1): return

      self.page = self.page - 1
      self.refreshPage()

   def gotoNext(self, e):
      if (self.page == 5): return

      self.page = self.page + 1
      self.refreshPage()

   def gotoLast(self, e):
      if (self.page == 5): return

      self.page = 5
      self.refreshPage()

   def gotoPage(self, e):
      page = self.currPage.GetSelection() + 1
      if (self.page == page): return

      self.page = page
      self.refreshPage()
