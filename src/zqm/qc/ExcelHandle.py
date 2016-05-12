#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016-5-11

@author: zqm
'''
import xlrd
from xlutils.copy import copy

class ExcelHandle():
    '''
             处理Excel
    '''
    def __init__(self,filepath,sheet_index=0):
        self.filepath=filepath
        self.sheet_index=sheet_index
        #打开Excel文件
        self.data=xlrd.open_workbook(self.filepath,formatting_info=True)
        #获取表单
        self.table = self.data.sheets()[self.sheet_index]
        #nrows = table.nrows ;ncols = table.ncols ;print "行数%d,列数%d" %(nrows,ncols)
        self.nrows = self.table.nrows
        self.ncols = self.table.ncols
        
    def read_cell(self,row,col=3,sheet_index=0):
        '''
                        读excel,读取指定单元格的内容
        '''
        txt=""
        #获取第i行的字段值(list)
        row_i_values = self.table.row_values(row)     
        if row_i_values:
            txt=self.table.cell_value(row,col)#table.cell_value(i,2)是unicode类型的 ,转化为字符串类型: str(table.cell_value(i,2))
        return txt
    
    def write_cell(self,row,col,value):
        '''
                        写excel，向指定单元格内书写value
        '''
        new_excel = copy(self.data);
        new_excel_sheet = new_excel.get_sheet(self.sheet_index);
        new_excel_sheet.write(row, col, value);
        new_excel.save(self.filepath); 
        #写完之后更新成员变量
        self.data=xlrd.open_workbook(self.filepath,formatting_info=True)
        self.table = self.data.sheets()[self.sheet_index]
        self.nrows = self.table.nrows
        self.ncols = self.table.ncols
        
    def count_wrong_miss_num(self,col0,col1,col2):
        ridTxts=dict()
        for i in range(1,self.nrows):
            #获取第i行的字段值(list)
            row_i_values = self.table.row_values(i)
            if row_i_values:
                col1_num=self.table.cell_value(i,col1)
                if(col1_num!=""):
                    col0_num=self.table.cell_value(i,col0)
                    if col1_num not in ridTxts.keys():
                        Txts=list()
                        Txts.append(col0_num) 
                        ridTxts[col1_num]=Txts
                    else:
                        Txts=ridTxts[col1_num]
                        Txts.append(col0_num)
                        ridTxts[col1_num]=Txts 
        #print   ridTxts  
        wrong_num=0
        miss_num=0
        for i in range(1,self.nrows):
            #获取第i行的字段值(list)
            row_i_values = self.table.row_values(i)     
            if row_i_values:
                col0_num=self.table.cell_value(i,col0)
                col1_num=self.table.cell_value(i,col1)
                col2_num=self.table.cell_value(i,col2)
                if(col1_num!="" and col2_num!=""  and (col1_num==col2_num)):
                    continue
                elif((col1_num=="" and col2_num!="") or \
                   (col1_num!="" and col2_num!="" and col2_num not in ridTxts[col1_num])):
                    print "wrong",col0_num
                    wrong_num+=1
                elif(col1_num!="" and col2_num==""):
                    print "miss",col0_num
                    miss_num+=1
        return (wrong_num,miss_num)
            

        
        