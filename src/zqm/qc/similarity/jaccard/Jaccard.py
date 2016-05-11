#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016-5-11

@author: zqm
'''
from __future__ import division  #from 需放开头，使用这个导入/默认为float除法
import zqm.qc.DoExcel as DE
import zqm.qc.TxtDealer as TD


class Jaccard():
   
    def __init__(self,accuracy=0.77):
        self.accuracy=accuracy
        
    def getSimScore(self,words1,words2):
        inters=list(set(words1).intersection(set(words2)))
        unions=list(set(words1).union(set(words2)))
        similar=len(inters)/len(unions)
        return similar
    
    def isSim(self,words1,words2):
        if self.getSimScore(words1,words2) > self.accuracy:
            return True
        else:
            return False
        
if __name__=="__main__":
   
    txt1=DE.read_excel(9)
    wordList1=TD.cut_word(txt1)
    
    txt2=DE.read_excel(10)
    wordList2=TD.cut_word(txt2)
    
    Jc=Jaccard()
    print Jc.isSim(wordList1,wordList2)
    
    
        