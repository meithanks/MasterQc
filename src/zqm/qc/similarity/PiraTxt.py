'''
Created on 2016-5-11

@author: zqm
'''

class PiraTxt():
    '''
    classdocs
    '''
    def __init__(self,no,text):
        self.no=no
        self.text=text
        
    def getNo(self):
        return self.no
    
    def getHrefText(self):
        return self.hrefText
    
    def getText(self):
        return self.text
    
    def getUrl(self):
        return self.url
    
    def getRid(self):
        return self.rid

    def setNo(self,no):
        self.no=no
    
    def setHrefText(self,hrefText):
        self.hrefText=hrefText
    
    def setText(self,text):
        self.text=text
    
    def setUrl(self,url):
        self.url=url
    
    def setRid(self,rid):
        self.rid=rid
        