#! /usr/bin/env python 
#coding:utf-8
'''
Created on 2016年5月17日

@author: chenzhen
'''
import database 

def LoginCheck(username, password):
    with database.SqliteDb() as db:
        result = db.GetUserInformation()
    if result:
        if (username, password) in result:
            return True
        else :
            return False 
    else :
        return False           
    
if __name__ == '__main__':
    print LoginCheck('admin', 'admin')