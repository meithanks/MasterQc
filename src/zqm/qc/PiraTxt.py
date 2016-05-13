#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016-5-11

@author: zqm
'''

class PiraTxt():
    '''
            样本记录对象
    '''
    def __init__(self,title,text,id,codes=list()):
        self.title=title
        self.text=text
        self.id=id
        self.rid=id
        self.codes=codes
        
    def getId(self):
        return self.Id
    
    def getTitle(self):
        return self.title
    
    def getText(self):
        return self.text
    
    def getRid(self):
        return self.rid
    
    def getCodes(self):
        return self.codes

    def setId(self,id):
        self.id=id
    
    def setTitle(self,title):
        self.title=title
    
    def setText(self,text):
        self.text=text
        
    def setRid(self,rid):
        self.rid=rid
        
    def setCodes(self,codes):
        self.codes=codes
        