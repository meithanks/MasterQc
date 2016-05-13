#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016-5-13

@author: zqm
'''
from __future__ import division  
import zqm.qc.DoHash  as StrHash
import zqm.qc.DoExcel as DE
import zqm.qc.DoTxt as TD

class MinHash():
    '''
            单个hash函数的MinHash
    '''
    def __init__(self,hashNum=20,threshold=15):
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
        minKeys=list()
        for i in range(self.hashNum):
            key_count=self.directJenkins(words,i)
            keys=key_count.keys();
            min_key=min(keys)
            minKeys.append(min_key)
        return minKeys
        
    def PseudoHamming(self,list1,list2):
        '''
                        获得两个集合的伪海明距离
        '''
        distance=0
        for i in range(self.hashNum):
            key1=list1[i]
            key2=list2[i]
            if key1==key2:
                distance=distance+1
        return distance
        
    def isSim(self,hashs1,hashs2):
        '''
                        获得两个hashs集合的是否相似
        '''
        if self.PseudoHamming(hashs1,hashs2) > self.threshold:
            return True
        else:
            return False
        
        
if __name__=="__main__":
   
    Jc=MinHash()
    txt1=DE.read_excel(2)
    print txt1
    wordList1=TD.cut_word(txt1)
    wordList1=Jc.extraSign(wordList1)
    
    txt2=DE.read_excel(3)
    print txt2
    wordList2=TD.cut_word(txt2)
    wordList2=Jc.extraSign(wordList2)
    
    print Jc.PseudoHamming(wordList1,wordList2)
    print Jc.isSim(wordList1,wordList2)