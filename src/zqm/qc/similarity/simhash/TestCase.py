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

import time

class TestCase():
   
    def __init__(self,file='D:\WorkSpaces\MasterQc\doc\Sample10.xls',testType="Jaccard",resultCol=4,extraSignTime=0,compSignTime=0):
        self.excel=file
        self.reaultCol=resultCol
        self.extraSignTime=extraSignTime
        self.compSignTime=compSignTime
        self.testType=testType
        
    def getPiraTxts(self):
        '''
                        将测试样本转化为对象List
        '''
        print "0.开始..."
        exclHandle=ExcelHandle.ExcelHandle(self.excel)
        PiraTxts=list()
        for i in range(1,exclHandle.nrows):
            pt=PiraTxt.PiraTxt(exclHandle.read_cell(i,0),exclHandle.read_cell(i,1),exclHandle.read_cell(i,2))
            PiraTxts.append(pt);
        
        #提取特征存入舆情样本对象中的codes
        start = time.clock()
        for i in range(len(PiraTxts)):
            txt=PiraTxts[i].getText()
            TxtH=TxtHandle.TxtHandle(txt)
            signHandle=SimHash.SimHash()
            codes=signHandle.extraSign(TxtH.getWords())
            PiraTxts[i].setCodes(codes)
        end = time.clock() 
        self.extraSignTime=end-start
        
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
                    #使用SimHashOne 计算相似度
                    simHandle=SimHash.SimHash()
                    #print similar
                    if simHandle.isSim(PiraTxts[i].getCodes(),PiraTxts[j].getCodes()):
                        PiraTxts[j].setRid(PiraTxts[i].id)
                        PiraTxtWithRids.append(PiraTxts[j])
                        ids.append(j) 
        end = time.clock() 
        self.compSignTime=end-start
        print "2.获取测试样本中相似文章对"
        return PiraTxtWithRids 
    
    def saveSimPiraTxts(self):
        PiraTxtPairs =self.getSimPiraTxts()
        exclHandle=ExcelHandle.ExcelHandle(self.excel)
        #记录运行时间和分词+特征提取时间
        exclHandle.write_cell(0,self.reaultCol,self.testType+"(extraSign:"+str(self.extraSignTime)+")"+"(compSign:"+str(self.compSignTime)+")")
        for i in range(len(PiraTxtPairs)):
            #print '(%d , %d)' % (PiraTxtPairs[i].id,PiraTxtPairs[i].rid) 
            exclHandle.write_cell(PiraTxtPairs[i].id-1,self.reaultCol,PiraTxtPairs[i].rid)
        print "2.相似文章对标记完成"
        
    def countWrongMiss(self):
        exclHandle=ExcelHandle.ExcelHandle(self.excel)
        print exclHandle.count_wrong_miss_num(2,3,4)
                  
if __name__=="__main__":
    filename='D:\WorkSpaces\MasterQc\doc\Sample10.xls'
    

    
#    '''SimHashByTF TestCase'''
#    import zqm.qc.similarity.simhash.SimHashByTF as SimHash
#    TCase=TestCase(filename,'SimHashTF',10)
#    TCase.saveSimPiraTxts()
    
#    '''SimHashByTFIDF TestCase'''
#    import zqm.qc.similarity.simhash.SimHashByTFIDF as SimHash
#    TCase=TestCase(filename,'SimHashTFIDF',11)
#    TCase.saveSimPiraTxts()
    
    '''SimHashByTFIDF TestCase'''
    import zqm.qc.similarity.simhash.SimHashByTextRank as SimHash
    TCase=TestCase(filename,'SimHashTextRank',12)
    TCase.saveSimPiraTxts()
    
#    TCase.countWrongMiss()

#    PiraTxtWithRids=TCase.getSimPiraTxts()
#    print TCase.runtime
##    txt_num=len(PiraTxtWithRids)
##    for i in range(txt_num):
##        print PiraTxtWithRids[i].id,PiraTxtWithRids[i].rid
   
  
    
    
        