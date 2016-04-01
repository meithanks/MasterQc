#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016-4-1

@author: zqm
'''
import numpy as np

import zqm.qc.DoExcel as DE
import zqm.qc.TxtDealer as TD

class getoutofloop(Exception): pass

def signature(row):
    txt=DE.read_excel(row)
    print(txt)
    code_count=TD.shingling_jenkins(txt)
    codes=code_count.keys();
    min_ten_codes=codes[0:10]
    for cd in codes[10:]:
        mx=max(min_ten_codes)
        if cd>mx:
            min_ten_codes.remove(mx); 
            min_ten_codes.append(cd);
        else:
            continue;
    return min_ten_codes

def minhash(gat):
    code_txts=dict()
    sign1=signature(1)
    #初始化code_txts
    for j in range(len(sign1)):
        key=str(j)+str(sign1[j]);
        code_txts[key]=list(1);
    try:     
        for i in range(2,50):
            flag=0
            #每个文章都有一个txt_count，用来统计和历史文章相同的code个数
            txt_count=dict();
            #获取该文章的sign
            isign=signature(i)
            for k in range(len(isign)):
                key=str(k)+str(isign[k]);
                if key in code_txts.keys():
                    txtlist=code_txts.get(key)
                    for t in txtlist:
                        if txt_count[t]:
                            txt_count[t]= txt_count[t]+1
                        else:
                            txt_count[t]=0;
                        if txt_count[t]>gat:
                            flag=1
                            raise getoutofloop("break")   
                elif flag!=1:
                    code_txts[key]=list(i);
            
                
                    
    except getoutofloop:
        pass
                       
                    
                        
                    
        

