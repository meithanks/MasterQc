#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015-12-2
@author: zqm
'''
import jieba
import jieba.analyse
import StrHash
#相对当前py文件路径，zqmdict.txt：使用notepad++,格式->以utf-8无BOM编码，
#然后输入，格式：词 词频 词性（一行）,自定义词典里提词频越高则成词概率越大，不宜过大。
#jieba.load_userdict("..\doc\dict.txt") 

def cut_word(txt,all_mode=False):
    '''分词操作'''
    words = list(jieba.cut(txt, all_mode))           #返回类型：可迭代的generator
    return  words;

def extract_key(self,key_num=10):
    '''关键词提取'''
    keys=list(jieba.analyse.extract_tags(txt,key_num)); #返回类型：可迭代的generator
    return  keys;

def get_TF(txt):
    '''TF提取'''
    words= cut_word(txt);
    words=list(words);
    tf_dict = dict()
    for i in range(len(words)):
        s =words[i];
        if s not in tf_dict:
            tf_dict[s] = 1
        else:
            tf_dict[s] += 1
    return tf_dict

def shingling(txt,step=5,on=True):
    '''shingling'''
    words= cut_word(txt);
    S = dict()
    for i in range(len(words) - step+1):
        s = ''.join(words[i:i + step])
        if s not in S:
            S[s] = 1
        else:
            S[s] += 1
    return S

#用于MinHashBaseSingleJenkins Hashes 若k较大，可考虑用token 的方式减小shingles。tokenize为是否进行hash的开关， 当开启hash时，klen为是否hash的阀值。
def shingling_jenkins(txt,step=10,on=True):
    '''shingling by hash'''
    words= cut_word(txt);
    S = dict()
    for i in range(len(words) - step+1):
        s = ''.join(words[i:i + step])
        if on:
            s=StrHash.jenkins(s);
        if s not in S:
            S[s] = 1
        else:
            S[s] += 1
    return S        
