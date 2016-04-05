#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016-4-1

@author: zqm
'''
from __future__ import division
import time
import zqm.qc.DoExcel as DE
import zqm.qc.TxtDealer as TD

def signature_one(row,n=20):
    '''抽取某文章中的n个最小的hash值，使用的是一种hash'''
    txt=DE.read_excel(row)
    key_count=TD.shingling_jenkins(txt)
    #print(txt)
    keys=key_count.keys();
    min_keys=keys[0:n]
    for cd in keys[n:]:
        mx=max(min_keys)
        if cd>mx:
            min_keys.remove(mx); 
            min_keys.append(cd);
        else:
            continue;
    return min_keys

def jaccard(T1,T2):
    intersection=list(set(T1).intersection(set(T2))) #计算交集  
    union_set= list(set(T1).union(set(T2))) #计算并集  
    return len(intersection)/len(union_set)
    
def minhash_one(gate,code_num,txt_num):
    ids=list()
    for i in range(1,txt_num):
        if i not in ids:      
            for j in range(i+1,txt_num):
                isign=signature_one(i,code_num)
                jsign=signature_one(j,code_num)
                similar=jaccard(isign,jsign)
                #print similar
                if similar>gate:
                    DE.write_excel(i+1,j)
                    print '(%d , %d)' % (i+1,j+1) 
                    ids.append(j)                       
#================================================================#
def signature_k(row,n=20):
    '''抽取某文章中的n个最小的hash值，使用的是k种hash函数'''
    txt=DE.read_excel(row)
    min_keys=list()
    for i in range(n):
        key_count=TD.shingling_jenkins(txt,i)
        #print(txt)
        keys=key_count.keys();
        mi=min(keys)
        min_keys.append(mi)
    return min_keys
                    
def minhash_k(gate,code_num,txt_num):
    key_txts=dict()
      
    for i in range(1,txt_num):
        flag=0
        #每个文章都有一个txt_count，用来统计和历史文章相同的key个数
        txt_count=dict();
        #获取该文章的sign
        isign=signature_k(i,code_num)
       
        for k in range(len(isign)):
            key=str(k)+str(isign[k]);
            txts=key_txts.get(key)
            if txts:
                for t in txts:
                    if t in txt_count.keys():
                        txt_count[t]= txt_count[t]+1
                    else:
                        txt_count[t]=0;
                    if txt_count[t]>gate:
                        flag=1 
                        DE.write_excel(t+1,i)
                        print '(%d , %d)' % (t+1,i+1)   
                        break
                    
                if flag==1:
                    break
            
        if flag!=1:
            for k in range(len(isign)):
                key=str(k)+str(isign[k]);
                txts=key_txts.get(key)
                if txts:
                    key_txts[key].append(i)
                else:
                    txts=list()
                    txts.append(i)
                    key_txts[key]=txts                      
                    
#start = time.clock()    
#print "run start"
#minhash_one(0.2,10,11)
#print "run over"
#end = time.clock()
#print "run time: %f s" % (end - start)
#

start = time.clock()    
print "run start"
minhash_k(10,20,11)
print "run over"
end = time.clock()
print "run time: %f s" % (end - start)