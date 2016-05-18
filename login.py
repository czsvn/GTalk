#! /usr/bin/env python 
#coding:utf-8
'''
Created on 2016年5月12日

@author: chenzhen
'''
import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade
import random
from logincheck import LoginCheck
import main



class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        # begin wxGlade: MyFrame.__init__
        kwargs['style'] = wx.BORDER_NONE
        wx.Frame.__init__(self, *args, **kwargs)
        #self.strofimage =  "images\login" + str(random.randrange(0, 3)) + ".png"     
        self.bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("images\login.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("images\my.png", wx.BITMAP_TYPE_ANY))
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "")
        if getattr(self, 'remberpw', None):
            if self.remberpw and self.username:
                self.text_ctrl_1.SetValue(self.username)      
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PASSWORD)
        self.checkbox_1 = wx.CheckBox(self, wx.ID_ANY, u"\u8bb0\u4f4f\u5bc6\u7801")
        self.checkbox_2 = wx.CheckBox(self, wx.ID_ANY, u"\u81ea\u52a8\u767b\u5f55")
        self.button_1 = wx.Button(self, wx.ID_ANY, u"\u767b\u5f55")
        self.hyperlink_1 = wx.HyperlinkCtrl(self, wx.ID_ANY, u"\u6ce8\u518c\u8d26\u53f7", "")
        self.hyperlink_2 = wx.HyperlinkCtrl(self, wx.ID_ANY, u"\u627e\u56de\u5bc6\u7801", "")

        self.__set_properties()
        self.__do_layout()
        self.__bind_event()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        self.SetSize((400, 300))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bitmap_2.SetMinSize((120, 82))
        self.text_ctrl_1.SetMinSize((180, 28))
        self.text_ctrl_2.SetMinSize((180, 30))
        self.checkbox_2.SetMinSize((91, 0))
        self.button_1.SetMinSize((180, 24))
        self.hyperlink_1.SetMinSize((61, 28))
        self.hyperlink_2.SetMinSize((61, 28))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.bitmap_1, 0, 0, 0)
        sizer_2.Add(self.bitmap_2, 0, wx.TOP, 10)
        sizer_3.Add(self.text_ctrl_1, 0, wx.TOP, 10)
        sizer_3.Add(self.text_ctrl_2, 0, 0, 0)
        sizer_4.Add(self.checkbox_1, 0, wx.TOP, 8)
        sizer_4.Add(self.checkbox_2, 0, wx.TOP, 8)
        sizer_3.Add(sizer_4, 1, 0, 0)
        sizer_3.Add(self.button_1, 0, wx.TOP, 10)
        sizer_2.Add(sizer_3, 1, 0, 0)
        sizer_5.Add(self.hyperlink_1, 0, wx.LEFT | wx.TOP, 18)
        sizer_5.Add(self.hyperlink_2, 0, wx.LEFT, 18)
        sizer_2.Add(sizer_5, 1, 0, 0)
        sizer_1.Add(sizer_2, 1, 0, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Center()
        # end wxGlade
    def __bind_event(self):
        self.checkbox_1.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        self.button_1.Bind(wx.EVT_BUTTON, self.OnButton)
        
    def ShowDialog(self, remind, title):
        dlg = wx.MessageDialog( self, remind, title, wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy()
        
    def OnCheckBox(self, event):
        if self.checkbox_1.GetValue():
            self.remberpw = True
        else:
            self.remberpw = False 
        
    def OnButton(self, event):
        self.username = self.text_ctrl_1.GetValue()
        self.password = self.text_ctrl_2.GetValue()
        if self.username.strip() and self.password.strip():
            if LoginCheck(self.username, self.password):
                self.Close()
                self.Destroy()
                main.MainFrame(None, -1, self.username).Show()
            else:
                self.ShowDialog(u'用户名或密码错误', u'提示')
                
        else:
            self.ShowDialog(u'用户名或密码未填', u'提示')
            
        

# end of class MyFrame
if __name__ == '__main__':
    app = wx.App(False)
    app.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    frame = MyFrame(None)
    frame.Show(True)
    app.MainLoop()
    



