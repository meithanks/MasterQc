#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016-5-28

@author: qmzhang
'''
from jpype import *

#
startJVM(getDefaultJVMPath(), "-Djava.class.path=D:\WorkSpaces\MasterQc\class\IKAnalyzer2012FF_u1.jar;D:\WorkSpaces\MasterQc\class\lucene-core-4.4.0.jar;D:\WorkSpaces\MasterQc\class", "-Xms1g", "-Xmx1g")
txt="水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露,有部分省接近了红线的指标，有部分省超过红线的指标。";

words=list()
IKAnalyzer = JClass('org.wltea.analyzer.lucene.IKAnalyzer')
IKATokenizer=IKAnalyzer(True)

ts=IKATokenizer.tokenStream("content",java.io.StringReader(txt))

CharTermAttribute = JClass('org.apache.lucene.analysis.tokenattributes.CharTermAttribute')
term=ts.getAttribute(CharTermAttribute);

while ts.incrementToken():
    words.append(str(java.lang.String(term.buffer(),0,term.length())))

print words
for i in range(len(words)):
    print(words[i]);    