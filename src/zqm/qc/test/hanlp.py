#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016-5-28

@author: qmzhang
'''
from jpype import *

startJVM(getDefaultJVMPath(), "-Djava.class.path=C:\ProgramFiles\hanlp\hanlp-1.2.8.jar;C:\ProgramFiles\hanlp", "-Xms1g", "-Xmx1g")
txt="水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露,有部分省接近了红线的指标，有部分省超过红线的指标。";

HanLP = JClass('com.hankcs.hanlp.HanLP')

termList = HanLP.segment(txt)
words=list()
for i in range(termList.size()):
    words.append(termList.get(i).toString());

print(words[0])
#words = list(HanLP.segment(txt))  
#print(words)

print("===============================标准分词=====================================")
#标准分词
StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
print(StandardTokenizer.segment(txt))

print("===============================NLP分词=====================================")
#NLP分词    
NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
print(NLPTokenizer.segment(txt))


print("===============================索引分词=====================================")
#索引分词
IndexTokenizer = JClass('com.hankcs.hanlp.tokenizer.IndexTokenizer')
print(IndexTokenizer.segment(txt))

print("===============================基础分词=====================================")
#基础分词器，只做基本NGram分词，不识别命名实体，不使用用户词典
BasicTokenizer = JClass('com.hankcs.hanlp.tokenizer.BasicTokenizer')
print(BasicTokenizer.segment(txt))

print("===============================实词分词=====================================")
#实词分词器，自动移除停用词
NotionalTokenizer = JClass('com.hankcs.hanlp.tokenizer.NotionalTokenizer')
print(NotionalTokenizer.segment(txt))

print("===============================繁体分词=====================================")
#繁体分词
TraditionalChineseTokenizer = JClass('com.hankcs.hanlp.tokenizer.TraditionalChineseTokenizer')
print(TraditionalChineseTokenizer.segment(txt))

print("===============================极速分词=====================================")
#极速分词
SpeedTokenizer = JClass('com.hankcs.hanlp.tokenizer.SpeedTokenizer')
print(SpeedTokenizer.segment(txt))

print("===============================N最短路径分词=====================================")
#N最短路径分词
NShortSegment = JClass('com.hankcs.hanlp.seg.NShort.NShortSegment')
NShortTokenizer=NShortSegment().enableCustomDictionary(False).enablePlaceRecognize(True).enableOrganizationRecognize(True).enablePlaceRecognize(True)
print(NShortTokenizer.seg(txt))

print("===============================最短路径分词=====================================")
#最短路径分词
DijkstraSegment = JClass('com.hankcs.hanlp.seg.Dijkstra.DijkstraSegment')
DijkstraTokenizer=DijkstraSegment().enableCustomDictionary(False).enablePlaceRecognize(True).enableOrganizationRecognize(True).enablePlaceRecognize(True)
print(DijkstraTokenizer.seg(txt))

print("===============================CRF分词=====================================")
#CRF分词
CRFSegment = JClass('com.hankcs.hanlp.seg.CRF.CRFSegment')
CRFTokenizer=CRFSegment()
print(CRFTokenizer.seg(txt))
