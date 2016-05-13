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
   
    Jc=MinHash()
    txt1=DE.read_excel(7)
    print txt1
    wordList1=TD.cut_word(txt1)
    wordList1=Jc.directJenkins(wordList1)
    
    txt2=DE.read_excel(8)
    print txt2
    wordList2=TD.cut_word(txt2)
    wordList2=Jc.directJenkins(wordList2)
    
    print Jc.jaccard(wordList1,wordList2)
    print Jc.isSim(wordList1,wordList2)