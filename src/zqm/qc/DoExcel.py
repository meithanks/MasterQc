#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015-12-2

@author: zqm
'''
import xlrd
from xlutils.copy import copy

filename='D:\WorkSpaces\MasterQc\doc\Sample10.xls'

def open_excel(file):
    '''打开excel'''
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
        
def read_excel(row,col=1,file=filename,sheet_index=0):
    '''读excel,读取特定单元格的内容'''
    data = open_excel(file)
    #获取表单
    table = data.sheets()[sheet_index]
    #nrows = table.nrows ;ncols = table.ncols ;print "行数%d,列数%d" %(nrows,ncols)
    txt=""
    #获取第i行的字段值(list)
    row_i_values = table.row_values(row)     
    if row_i_values:
        txt=table.cell_value(row,col)#table.cell_value(i,2)是unicode类型的 ,转化为字符串类型: str(table.cell_value(i,2))
    return txt

def write_excel(value,row,col=7,file= filename,sheet_index=0):
    '''写excel，想特定单元格内书写value'''
    old_excel = xlrd.open_workbook(file, formatting_info=True);
    new_excel = copy(old_excel);
    new_excel_sheet = new_excel.get_sheet(sheet_index);
    new_excel_sheet.write(row, col, value);
    new_excel.save(file); 