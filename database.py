#! /usr/bin/env python 
#coding:utf-8
'''
Created on 2016年5月12日

@author: chenzhen
'''
import sqlite3

class SqliteDb:
    def __init__(self, databasename='gtalk.s3db'):
        self.conn = None
        self.cursor = None
        self.tables = {}
        self.tables['usermanage'] = 'USERMANAGE'
        self.databasename = databasename
    
    def __enter__(self):
        self.checkconn()
        return self
    
    def __exit__(self, type, value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
    
    def checkconn(self):
        if not self.conn:
            self.conn = sqlite3.connect(self.databasename, isolation_level="DEFERRED")
        if not self.cursor:
            self.cursor = self.conn.cursor()
    
    def GetUserInformation(self):
        query = "SELECT * FROM USERMANAGE"
        try:
            self.cursor.execute(query)
        except:
            self.cursor.rollback()
            return False
        else:
            return self.cursor.fetchall()
    
if __name__ == '__main__':
    with SqliteDb() as db:
        result = db.GetUserInformation()
    print result
    