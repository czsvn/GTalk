#! /usr/bin/env python 
#coding:utf-8
'''
Created on 2016年5月18日

@author: chenzhen
'''
import client
import login
import wx
import asyncore
import threading


def windowstart():
    app = wx.App(False)
    app.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    frame = login.MyFrame(None)
    frame.Show(True)
    app.MainLoop()

def clientstart():
    message = 'adjfdjfjjdf**end**'
    client = client.Client('localhost', 8080, message)
    asyncore.loop()

if __name__ == '__main__':
    app = wx.App(False)
    app.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    frame = login.MyFrame(None)
    frame.Show(True)
    
    window = frame
    client = client.Client('localhost', 8080, frame)
    
    
    cs = threading.Thread(name='clientstart', target=asyncore.loop)
    ws = threading.Thread(name='windowstart', target=app.MainLoop)
    ws.setDaemon(True)
    ws.start()
    cs.start()
