#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015-12-2

@author: zqm
'''
import jieba
jieba.load_userdict("..\doc\dict.txt") #相对当前py文件路径，zqmdict.txt：使用notepad++,格式->以utf-8无BOM编码，然后输入，格式：词 词频 词性（一行）
class CutWord:
    #构造函数
    def __init__(self,txt):
        self.txt=txt;
        #self.words=self.cut_word(self.txt);
        
    def cut_word(self,cut_all=False):
        words = jieba.cut(self.txt,cut_all)   #返回类型：可迭代的generator
        #word_list=list(words)            #unicode编码
        return  "/".join(words);
    
if __name__ == '__main__':
    txt="垃圾回收机制不仅针对引用计数为0的对象，同样也可以处理循环引用的情况。";
    c1=CutWord(txt);
    print(c1.cut_word());