#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016-5-11

@author: zqm
'''
from __future__ import division  #from 需放开头，使用这个导入/默认为float除法
import zqm.qc.DoExcel as DE
import zqm.qc.DoTxt as TD


class Jaccard():
   
    def __init__(self,threshold=0.77):
        '''
        Jaccard构造器，构造参数中需传递相似阈值
        '''
        self.threshold=threshold
        
    def jaccard(self,set1,set2):
        '''
                        获得两个集合的jaccad
        '''
        inters=list(set(set1).intersection(set(set2)))
        unions=list(set(set1).union(set(set2)))
        similar=len(inters)/len(unions)
        return similar
    
    def isSim(self,words1,words2):
        '''
                        获得两个word集合的是否相似
        '''
        if self.jaccard(words1,words2) > self.threshold:
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
    
    
        