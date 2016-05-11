#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016-5-11

@author: zqm
'''
from __future__ import division  #from 需放开头，使用这个导入/默认为float除法
import zqm.qc.DoExcel as DE
import zqm.qc.TxtDealer as TD
import zqm.qc.PiraTxt as PT
import zqm.qc.similarity.jaccard.Jaccard as Jac


class TestCase():
   
    def __init__(self,file='D:\WorkSpaces\MasterQc\doc\Sample10.xls'):
        self.excel=file
        
    def getPiraTxts(self):
        data=DE.open_excel(self.excel)
        PiraTxts=list()
        table = data.sheets()[0]
        nrows = table.nrows
        for i in range(1,nrows+1):
            pt=PT.PiraTxt(DE.read_excel(i,5,data),DE.read_excel(i,3,data))
            PiraTxts.append(pt);
        return PiraTxts
   
    def getSimPiraTxts(self):
        PiraTxts=self.getPiraTxts()
        txt_num=len(PiraTxts)
        PiraTxtWithRids=list()
        ids=list()
        for i in range(txt_num):
            if i not in ids:      
                for j in range(i+1,txt_num):
                    iTxtWords=TD.cut_word(PiraTxts[i].getText())
                    jTxtWords=TD.cut_word(PiraTxts[j].getText())
                    jc=Jac.Jaccard()
                    #print similar
                    if jc.isSim(iTxtWords,jTxtWords):
                        PiraTxts[j].setRid(i)
                        PiraTxtWithRids.append(PiraTxts[j])
                        print '(%d , %d)' % (i+1,j+1) 
                        ids.append(j)       
  
    
#if __name__=="__main__":
   
  
    
    
        