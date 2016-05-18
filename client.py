#! /usr/bin/env python 
#coding:utf-8
'''
Created on 2016年5月18日

@author: chenzhen
'''
from asynchat import async_chat
import socket
import asyncore
import wx

class Client(async_chat):
    def __init__(self, host, port, window):
        self.window = window
        self.data = []
        async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        
        self.window.button.Bind(wx.EVT_BUTTON, self.OnSend)
        
    def handle_connect(self, text='hello**end**'):
        self.push(text)
        #self.push('hello**end**')
        
        #self.window.button.Bind(wx.EVT_BUTTON, self.OnSend)
        self.set_terminator('\r\n')
    
    def collect_incoming_data(self, data):
        data = data.decode('utf8')
        self.data.append(data)
    
    def found_terminator(self):
        receive_message = ''.join(self.data) + '\r\n'
        self.data = []
        self.window.control.WriteText(receive_message)
        
    def OnSend(self, event):
        if self.window.control2.GetValue():
            message = self.window.control2.GetValue().encode('utf8') + "**end**"
            self.send(message)
        self.window.control2.SetValue('')

    
    
        
if __name__ == '__main__':
    message = 'adjfdjfjjdf**end**'
    clinet = Client('localhost', 8080, message)
    asyncore.loop()

    
