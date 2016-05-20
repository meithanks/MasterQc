#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015-12-2
@author: zqm
'''
import jieba.analyse
import re
#相对当前py文件路径，zqmdict.txt：使用notepad++,格式->以utf-8无BOM编码，
#然后输入，格式：词 词频 词性（一行）,自定义词典里提词频越高则成词概率越大，不宜过大。
#jieba.load_userdict("D:\WorkSpaces\MasterQc\doc\dict.txt") 

class TxtHandle():
    
    def __init__(self,txt,cut=1):
        self.txt=txt
        self.words=list()
        if cut==1:
            self.words=self.cut_word()
        if cut==2:
            self.words=self.extract_key()
        if cut==3:
            self.words=self.extract_tzc()
    
    #1     
    def cut_word(self,all_mode=False):
        '''分词操作'''
        words = list(jieba.cut(self.txt, all_mode))           #返回类型：可迭代的generator
        return  words;
    #2
    def extract_key(self,key_num=10):
        '''关键词提取'''
        keys=list(jieba.analyse.extract_tags(self.txt,key_num)); #返回类型：可迭代的generator
        return  keys;
    #3
    def extract_tzc(self,tzhN=5):
        '''特征串提取'''
        tzcs=list()
        text=re.sub(r'&#[\d]+','', self.txt)
        
        splitStr=text.split('。');
        if splitStr[len(splitStr)-1]=='':
            splitStr.remove(splitStr[len(splitStr)-1])
        
        if len(splitStr)<2:
            splitStr=text.split('，')
            if splitStr[len(splitStr)-1]=='':
                splitStr.remove(splitStr[len(splitStr)-1])
                  
        for i in range(len(splitStr)-1):
            words = splitStr[i]
           
            if len(words)>=3*tzhN:
                beforeStr=''.join(words[len(words)-3*tzhN:len(words)])
            else:
                beforeStr = ''.join(words)
            
            words = splitStr[i+1]  
            if len(words)>=3*tzhN:
                afterStr=''.join(words[0:3*tzhN])
            else:
                afterStr=''.join(words)
                
            tzcs.append(''.join([beforeStr,afterStr]))
            

        return  tzcs; 
    #================================================================================#
       
    def getWords(self):
        return self.words   
    
    def setWords(self,words):
        self.words =words

if __name__=="__main__":
    txt="中新网4月6日电据日媒报道，近日，日本大分县别府市在当地大平山(通称：扇山)举行了名为“扇山火祭”的烧荒活动。"
    TxtH=TxtHandle(txt,3)
    for w in TxtH.words:
        print w

#    for i in TxtH.words:
#        print i
