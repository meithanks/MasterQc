#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016-5-11

@author: zqm
'''
from __future__ import division  #from 需放开头，使用这个导入/默认为float除法
import math

import zqm.qc.ExcelHandle as ExcelHandle
import zqm.qc.PiraTxt as PiraTxt
import zqm.qc.TxtHandle as TxtHandle

class CosinHash():
   
    def __init__(self,threshold=0.85,maxiter=200,mindiff=0.001,d=0.85):
        self.threshold=threshold
        self.maxiter=maxiter
        self.mindiff=mindiff
        self.d=d
    
    def getTextRank(self,words):
        '''TF提取'''
        TextRank_dict = dict()
        wordList_dict = dict()
        queue=list()
        for i in range(len(words)):
            s =words[i];
            if s not in wordList_dict.keys():
                wordList_dict[s] = list()
            queue.append(s)
            if len(queue)>5:
                queue.remove(queue[0])
            
            for q in queue:
                for p in queue:
                    if q==p:
                        continue
                    wordList_dict[q].append(p)
                    wordList_dict[p].append(q)
                    
        #print wordList_dict
               
        for i in range(self.maxiter):
            TextRank_tempdict = dict()
            max_diff=0
            for key in wordList_dict.keys():
                listValue=wordList_dict[key]
                TextRank_tempdict[key]=1-self.d
                for value in listValue:
                    size=len(listValue)
                    if (key==value or size==0):
                        continue
                    if value not in TextRank_dict.keys():
                        TextRank_dict[value]=0
                        
                    TextRank_tempdict[key]=TextRank_tempdict[key]+self.d/size*TextRank_dict[value]
                
                if key not in TextRank_dict.keys():
                        TextRank_dict[key]=0
                max_diff=max(max_diff,abs(TextRank_tempdict[key]-TextRank_dict[key]))
            
            TextRank_dict=TextRank_tempdict
            if max_diff <= self.mindiff:
                break
            
        return TextRank_dict    
    
        
    def Cosine(self,set1,set2):
        '''
                        获得两个集合的Cosine
        '''
        #分别获取两个词集的词频dict
        Dict1=self.getTextRank(set1)
        Dict2=self.getTextRank(set2)
        
        #分别获取两个词频dict的keys
        keys1=Dict1.keys()
        keys2=Dict2.keys()
        
        #合并两个词频dict的keys
        keys=list()
        keys.extend(keys1)
        keys.extend(keys2)
    
        #以两个词频dict的keys合集为坐标，分别求出两个词集在这个坐标下的向量
        keys=list(set(keys))
        for key in keys:
            if key not in keys1:
                Dict1[key]=0
                
        for key in keys:
            if key not in keys2:
                Dict2[key]=0
                
        denominator=0
        v1=0
        v2=0
        for key in keys:
            denominator=denominator+Dict1[key]*Dict2[key]
            v1=v1+Dict1[key]*Dict1[key]
            v2=v2+Dict2[key]*Dict2[key]
        similar=denominator/(math.sqrt(v1)*math.sqrt(v2))
        return similar
    
    def isSim(self,words1,words2):
        '''
                        获得两个word集合的是否相似
        '''
        if self.Cosine(words1,words2) > self.threshold:
            return True
        else:
            return False
        
if __name__=="__main__":
    file='D:\WorkSpaces\MasterQc\doc\Sample10.xls'
    exclHandle=ExcelHandle.ExcelHandle(file)
    PiraTxts=list()
    i=8
    pt=PiraTxt.PiraTxt(exclHandle.read_cell(i,0),exclHandle.read_cell(i,1),exclHandle.read_cell(i,2))
    PiraTxts.append(pt);
    j=10
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
    
    Jc=CosinHash()
    
    print Jc.Cosine(PiraTxts[0].getCodes(),PiraTxts[1].getCodes())
    print Jc.isSim(PiraTxts[0].getCodes(),PiraTxts[1].getCodes())
   
    
    
        