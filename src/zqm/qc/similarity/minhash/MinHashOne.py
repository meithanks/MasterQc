#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016-5-13

@author: zqm
'''
from __future__ import division  
import zqm.qc.ExcelHandle as ExcelHandle
import zqm.qc.PiraTxt as PiraTxt
import zqm.qc.TxtHandle as TxtHandle
import zqm.qc.DoHash  as StrHash

class MinHash():
    '''
            单个hash函数的MinHash
    '''
    def __init__(self,hashNum=20,threshold=0.5):
        self.hashNum=hashNum
        self.threshold=threshold
          
    #用于MinHashBaseSingleJenkins Hashes 若k较大，可考虑用token 的方式减小shingles。tokenize为是否进行hash的开关， 当开启hash时，klen为是否hash的阀值。
    def directJenkins(self,words,initval=0):
        '''shingling by hash'''
        S = dict()
        for i in range(len(words)):
            s=StrHash.jenkins(words[i],initval)
            if s not in S:
                S[s] = 1
            else:
                S[s] += 1
        return S

    #用于MinHashBaseSingleJenkins Hashes 若k较大，可考虑用token 的方式减小shingles。tokenize为是否进行hash的开关， 当开启hash时，klen为是否hash的阀值。
    def shinglingJenkins(self,words,initval=0,step=5,on=True):
        '''shingling or shingling by hash'''
        S = dict()
        for i in range(len(words) - step+1):
            s = ''.join(words[i:i + step])
            if on:
                s=StrHash.jenkins(s,initval);
            if s not in S:
                S[s] = 1
            else:
                S[s] += 1
        return S      
        
    def extraSign(self,words):
        key_count=self.directJenkins(words)
        keys=key_count.keys();
        min_keys=keys[0:self.hashNum]
        for cd in keys[self.hashNum:]:
            mx=max(min_keys)
            if cd>mx:
                min_keys.remove(mx); 
                min_keys.append(cd);
            else:
                continue;
        return min_keys
        
    def jaccard(self,set1,set2):
        '''
                        获得两个集合的jaccad
        '''
        inters=list(set(set1).intersection(set(set2)))
        unions=list(set(set1).union(set(set2)))
        similar=len(inters)/len(unions)
        return similar
        
    def isSim(self,hashs1,hashs2):
        '''
                        获得两个hashs集合的是否相似
        '''
        if self.jaccard(hashs1,hashs2) > self.threshold:
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
    signHandle=MinHash.MinHash()
    codes=signHandle.extraSign(TxtH.getWords())
    PiraTxts[0].setCodes(codes)
    
    txt=PiraTxts[1].getText()
    TxtH=TxtHandle.TxtHandle(txt)
    signHandle=MinHash.MinHash()
    codes=signHandle.extraSign(TxtH.getWords())
    PiraTxts[1].setCodes(codes)
    
    Jc=MinHash()
    
    print Jc.Cosine(PiraTxts[0].getCodes(),PiraTxts[1].getCodes())
    print Jc.isSim(PiraTxts[0].getCodes(),PiraTxts[1].getCodes())