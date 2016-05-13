#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015-12-2
@author: zqm
'''
import jieba.analyse
#相对当前py文件路径，zqmdict.txt：使用notepad++,格式->以utf-8无BOM编码，
#然后输入，格式：词 词频 词性（一行）,自定义词典里提词频越高则成词概率越大，不宜过大。
#jieba.load_userdict("..\doc\dict.txt") 

class TxtHandle():
    
    def __init__(self,txt,cut=True):
        self.txt=txt
        self.words=list()
        if cut:
            self.words=self.cut_word()
         
    def cut_word(self,all_mode=False):
        '''分词操作'''
        words = list(jieba.cut(self.txt, all_mode))           #返回类型：可迭代的generator
        return  words;
    
    def extract_key(self,key_num=10):
        '''关键词提取'''
        keys=list(jieba.analyse.extract_tags(self.txt,key_num)); #返回类型：可迭代的generator
        return  keys;
    #================================================================================#
       
    def getWords(self):
        return self.words   
    
    def setWords(self,words):
        self.words =words

if __name__=="__main__":
   
    TxtH=TxtHandle("我有一只小狗，特别可爱")
    
    print TxtH.words