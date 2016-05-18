#! /usr/bin/env python 
#coding:utf-8
'''
Created on 2016年5月12日

@author: chenzhen
'''
from asyncore import dispatcher
from asynchat import async_chat
import socket 
import asyncore

PORT = 8080
NAME = 'GTALK'

class Server(dispatcher):
    def __init__(self, port, name):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.name = name
        self.sessions = []
    
    def disconnect(self, session):
        self.sessions.remove(session)
    
    def broadcast(self, line):
        for session in self.sessions:
            session.push(line)
            
    def handle_accept(self):
        sock, addr = self.accept()
        print addr
        self.sessions.append(Session(self, sock))

class Session(async_chat):
    def __init__(self, server, sock):
        async_chat.__init__(self, sock)
        self.server = server
        self.data = []
        self.set_terminator('**end**')
        self.push('Welcome to %s' % self.server.name + '\r\n')
    
    def collect_incoming_data(self, data):
        self.data.append(data)
    
    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        self.server.broadcast(line + "\r\n")
    
    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)
               
if __name__ == '__main__':
    s = Server(PORT, NAME)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print 