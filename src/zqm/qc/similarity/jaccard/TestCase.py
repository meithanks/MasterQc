#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016-5-11

@author: zqm
'''
from __future__ import division  #from 需放开头，使用这个导入/默认为float除法
import zqm.qc.ExcelHandle as ExcelHandle
import zqm.qc.PiraTxt as PiraTxt
import zqm.qc.TxtHandle as TxtHandle
import zqm.qc.similarity.jaccard.Jaccard as Jaccard
import time

class TestCase():
   
    def __init__(self,file='D:\WorkSpaces\MasterQc\doc\Sample3000.xls',resultCol=4,runtime=0,testType="Jaccard"):
        self.excel=file
        self.reaultCol=resultCol
        self.runtime=runtime
        self.testType=testType
        
    def getPiraTxts(self):
        '''
                        将测试样本转化为对象List
        '''
        print "0.开始..."
        exclHandle=ExcelHandle.ExcelHandle(self.excel)
        PiraTxts=list()
        for i in range(1,exclHandle.nrows):
            txt=exclHandle.read_cell(i,1)
            TxtH=TxtHandle.TxtHandle(txt)
            pt=PiraTxt.PiraTxt(exclHandle.read_cell(i,0),"",exclHandle.read_cell(i,2),TxtH.words)
            PiraTxts.append(pt);
        print "1.将测试样本转化为对象List完成"
        return PiraTxts
   
    def getSimPiraTxts(self):
        '''
                        获取测试样本中相似文章对
        '''
        
        PiraTxts=self.getPiraTxts()
        txt_num=len(PiraTxts)
        PiraTxtWithRids=list()
        #保存已检测出和之前文章重复的文章序号
        ids=list()
        start = time.clock()
        for i in range(txt_num):
            if i not in ids:      
                for j in range(i+1,txt_num):
                    jc=Jaccard.Jaccard()
                    #print similar
                    if jc.isSim(PiraTxts[i].getWords(),PiraTxts[j].getWords()):
                        PiraTxts[j].setRid(PiraTxts[i].id)
                        PiraTxtWithRids.append(PiraTxts[j])
                        ids.append(j) 
        end = time.clock() 
        self.runtime=end-start
        print "2.获取测试样本中相似文章对"
        return PiraTxtWithRids 
    
    def saveSimPiraTxts(self):
        PiraTxtPairs =self.getSimPiraTxts()
        exclHandle=ExcelHandle.ExcelHandle(self.excel)
        exclHandle.write_cell(0,self.reaultCol,self.testType+"("+str(self.runtime)+")")
        for i in range(len(PiraTxtPairs)):
            #print '(%d , %d)' % (PiraTxtPairs[i].id,PiraTxtPairs[i].rid) 
            exclHandle.write_cell(PiraTxtPairs[i].id-1,self.reaultCol,PiraTxtPairs[i].rid)
        print "2.相似文章对标记完成"
        
    def countWrongMiss(self):
        exclHandle=ExcelHandle.ExcelHandle(self.excel)
        print exclHandle.count_wrong_miss_num(2,3,4)
                  
if __name__=="__main__":
   
    TCase=TestCase()
#    TCase.saveSimPiraTxts()
    TCase.countWrongMiss()

#    PiraTxtWithRids=TCase.getSimPiraTxts()
#    print TCase.runtime
##    txt_num=len(PiraTxtWithRids)
##    for i in range(txt_num):
##        print PiraTxtWithRids[i].id,PiraTxtWithRids[i].rid
   
  
    
    
        