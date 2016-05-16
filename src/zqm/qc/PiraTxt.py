#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016-5-11

@author: zqm
'''
import zqm.qc.TxtHandle as TxtHandle

class PiraTxt():
    '''
            样本记录对象
    '''
    wordTxtsDict=dict()
    
    def __init__(self,title,text,id,codes=list()):
        self.title=title
        self.text=text
        self.id=id
        self.rid=id
        self.codes=codes
        self.load_word()
        
    def load_word(self,all_mode=False):
        '''各个词对应的包含其的文章个数'''
        th=TxtHandle.TxtHandle(self.text)
        words=th.getWords()
        
        for word in words:
            if word not in PiraTxt.wordTxtsDict.keys():
                PiraTxt.wordTxtsDict[word]=1
            else:
                PiraTxt.wordTxtsDict[word]=PiraTxt.wordTxtsDict[word]+1
        
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
        