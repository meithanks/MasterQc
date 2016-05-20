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
   
    def __init__(self,threshold=7):
        self.threshold=threshold  
    
    def getTFIDF(self,words):
        '''TF提取'''
        tfidf_dict = dict()
        tf_dict = dict()
        for i in range(len(words)):
            s =words[i];
            if s not in tf_dict:
                tf_dict[s] = 1
            else:
                tf_dict[s] += 1
        #求取相对词频        
        for key in tf_dict.keys():
            tf_dict[key]=tf_dict[key]/len(words) 
        
        #获取文档总数                   
        docNum=len(PiraTxt.PiraTxt.wordTxtsDict.keys())
        
        #求取每个词的tf-idf
        for key in tf_dict.keys():
            tf=tf_dict[key]
            containDocNum=PiraTxt.PiraTxt.wordTxtsDict[key]
            idf=math.log(docNum/(containDocNum+1))
            tfidf=tf*idf
            tfidf_dict[key]=tfidf
        
        return tfidf_dict  
        
    #用于MinHashBaseSingleJenkins Hashes 若k较大，可考虑用token 的方式减小shingles。tokenize为是否进行hash的开关， 当开启hash时，klen为是否hash的阀值。
    def directJenkins(self,words,initval=0):
        '''shingling by hash'''
        tfidfDict=self.getTFIDF(words)
        S = dict()
        for key in tfidfDict.keys():
            s=StrHash.jenkins(key,initval)
            S[s] = tfidfDict[key]
    
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
    i=8
    pt=PiraTxt.PiraTxt(exclHandle.read_cell(i,0),exclHandle.read_cell(i,1),exclHandle.read_cell(i,2))
    PiraTxts.append(pt);
    j=10
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
   
   
    
    
        