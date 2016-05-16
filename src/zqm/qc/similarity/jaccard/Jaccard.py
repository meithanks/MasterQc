#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016-5-11

@author: zqm
'''
from __future__ import division  #from 需放开头，使用这个导入/默认为float除法
import zqm.qc.ExcelHandle as ExcelHandle
import zqm.qc.PiraTxt as PiraTxt
import zqm.qc.TxtHandle as TxtHandle


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
   
    file='D:\WorkSpaces\MasterQc\doc\Sample10.xls'
    exclHandle=ExcelHandle.ExcelHandle(file)
    PiraTxts=list()
    i=2
    pt=PiraTxt.PiraTxt(exclHandle.read_cell(i,0),exclHandle.read_cell(i,1),exclHandle.read_cell(i,2))
    PiraTxts.append(pt);
    j=3
    pt=PiraTxt.PiraTxt(exclHandle.read_cell(j,0),exclHandle.read_cell(j,1),exclHandle.read_cell(j,2))
    PiraTxts.append(pt);
    
    txt=PiraTxts[0].getText()
    TxtH=TxtHandle.TxtHandle(txt)
    codes=TxtH.getWords()
    PiraTxts[0].setCodes(codes)
    
    txt=PiraTxts[1].getText()
    TxtH=TxtHandle.TxtHandle(txt)
    codes=TxtH.getWords()
    PiraTxts[1].setCodes(codes)
    
    Jc=Jaccard()
    
    print Jc.Cosine(PiraTxts[0].getCodes(),PiraTxts[1].getCodes())
    print Jc.isSim(PiraTxts[0].getCodes(),PiraTxts[1].getCodes())
    
        