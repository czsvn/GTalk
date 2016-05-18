#! /usr/bin/env python 
#coding:utf-8
'''
Created on 2016年5月12日

@author: chenzhen
'''
import wx

#-------------------------------------------------------------------------

class LoginDialog(wx.Dialog):
    def __init__(self, parent, id, title,  
                       size = (350, 200),
                       pos = wx.DefaultPosition,
                       style = wx.DEFAULT_DIALOG_STYLE, useMetal = False):
        pre = wx.PreDialog()
        pre.Create(parent, id, title, pos, size, style)
        self.PostCreate(pre)
        self.user, self.password = '', ''
        self.CreateSizer()
        
    def dataEntries(self):
        return (('用户  ', 0, self.OnUser),('密码  ', wx.TE_PASSWORD, self.OnPassword))
                                    
    def dataButtons(self):
        return ((wx.ID_OK, '确定'),(wx.ID_CANCEL, '取消'))
        
    def CreateSizer(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wx.StaticText(self, -1, '请输入用户名和密码'), 0, wx.ALIGN_CENTER | wx.ALL, 5)
        for eachLabel, eachStyle, eachHandler in self.dataEntries():
            self.CreateEntry(sizer, eachLabel, eachStyle, eachHandler)
        sizer.Add(wx.StaticLine(self, -1, size=(20, -1), style=wx.LI_HORIZONTAL),
                            0, wx.GROW | wx.ALIGN_CENTER_VERTICAL | wx.RIGHT | wx.TOP, 5)
        btnsizer = wx.StdDialogButtonSizer()
        for eachId, eachLabel in self.dataButtons():
            self.CreateButton(btnsizer, eachId, eachLabel)
        btnsizer.Realize()
        sizer.Add(btnsizer, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.SetSizer(sizer)
        sizer.Fit(self)
            
    def CreateEntry(self, sizer, label, style, handler):
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(wx.StaticText(self, -1, label), 0, wx.ALIGN_CENTER | wx.ALL, 5)
        text = wx.TextCtrl(self, -1, "", size = (80, -1), style = style)
        text.Bind(wx.EVT_TEXT, handler)
        box.Add(text, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        
    def CreateButton(self, btnsizer, id, label):
        button = wx.Button(self, id, label)
        if id == wx.ID_OK:
            button.SetDefault()
        btnsizer.AddButton(button)        
        
    def OnUser(self, event):
        self.user = event.GetString()
        
    def OnPassword(self, event):
        self.password = event.GetString()
        
    def GetValue(self):
        return (self.user, self.password)
    
    