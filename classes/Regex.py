import re

class Regex:
    chapterPattern=re.compile(r'chapter\d{1,2}')
    urlPattern=re.compile(r'^https://automatetheboringstuff.com/2e/chapter\d{1,2}/?$')
    
    @staticmethod
    def searchUrl(self,url):
        return re.search(self.urlPattern,url)
    
    @staticmethod
    def getChapter(self,url):
        return re.search(self.chapterPattern,url)
        
    

