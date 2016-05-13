#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016-5-11

@author: zqm
'''
from __future__ import division  #from 需放开头，使用这个导入/默认为float除法
import math
import zqm.qc.DoExcel as DE
import zqm.qc.DoTxt as TD


class CosinHash():
   
    def __init__(self,threshold=0.97):
        self.threshold=threshold
    
    def getRelativeTF(self,words):
        '''相对TF提取'''
        
        tf_dict = dict()
        for i in range(len(words)):
            s =words[i];
            if s not in tf_dict:
                tf_dict[s] = 1
            else:
                tf_dict[s] += 1
                
        for key in tf_dict.keys():
            tf_dict[key]=tf_dict[key]/len(words)
            
        return tf_dict    
        
        
    def Cosine(self,set1,set2):
        '''
                        获得两个集合的Cosine
        '''
        Dict1=self.getRelativeTF(set1)
        Dict2=self.getRelativeTF(set2)
        keys1=Dict1.keys()
        keys2=Dict2.keys()
        
        keys=list()
        keys.extend(keys1)
        keys.extend(keys2)
    
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
   
    txt1=DE.read_excel(2)
    wordList1=TD.cut_word(txt1)
    
    txt2=DE.read_excel(3)
    wordList2=TD.cut_word(txt2)
    
    Jc=CosinHash()
    print Jc.Cosine(wordList1,wordList2)
    print Jc.isSim(wordList1,wordList2)
   
    
    
        