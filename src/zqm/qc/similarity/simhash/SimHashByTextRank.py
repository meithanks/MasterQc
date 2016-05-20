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
import zqm.qc.DoHash  as StrHash


class SimHash():
   
    def __init__(self,threshold=5,maxiter=200,mindiff=0.001,d=0.85):
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
        
    #用于MinHashBaseSingleJenkins Hashes 若k较大，可考虑用token 的方式减小shingles。tokenize为是否进行hash的开关， 当开启hash时，klen为是否hash的阀值。
    def directJenkins(self,words,initval=0):
        '''shingling by hash'''
        TextRankDict=self.getTextRank(words)
        S = dict()
        for key in TextRankDict.keys():
            s=StrHash.jenkins(key,initval)
            S[s] = TextRankDict[key]
    
        return S
        
    def extraSign(self,words):
        key_count=self.directJenkins(words)
        keys=key_count.keys();
        
        bits=list()
        for i in range(32):
            bits.append(0)
        
        for key in keys:
            weight=key_count[key]
            for i in range(32):
                if ((key>>i) & 0x1)!=0:
                    bits[i]=bits[i]+weight
                else:
                    bits[i]=bits[i]-weight
        
        for i in range(32):
            if bits[i]>0:
                bits[i]=1
            else:
                bits[i]=0
                
        return bits           
              
            
    def HammingDistance(self,sign1,sign2):
        count=0
        for i in range(32):
            if sign1[i]!=sign2[i]:
                count=count+1
                
        return count
  
    
    def isSim(self,sign1,sign2):
        '''
                        获得两个word集合的是否相似
        '''
        if self.HammingDistance(sign1,sign2) < self.threshold:
            return True
        else:
            return False
        
if __name__=="__main__":
   
    Jc=SimHash()
   
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
    words=TxtH.getWords()
    codes= Jc.extraSign(words)
    PiraTxts[0].setCodes(codes)
    
    txt=PiraTxts[1].getText()
    TxtH=TxtHandle.TxtHandle(txt)
    words=TxtH.getWords()
    codes= Jc.extraSign(words)
    PiraTxts[1].setCodes(codes)
    
    print Jc.HammingDistance(PiraTxts[0].getCodes(),PiraTxts[1].getCodes())
    print Jc.isSim(PiraTxts[0].getCodes(),PiraTxts[1].getCodes())
   
   
    
    
        