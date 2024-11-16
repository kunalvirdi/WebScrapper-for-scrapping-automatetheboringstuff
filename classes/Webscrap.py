from bs4 import BeautifulSoup
import re
import time

class ScrapWeb:
    headingToProgramsMap={}
    startingRange=None
    endingRange=None
    htmlContent=None
    headingPattern=re.compile(r'^h[1-6]$')
    
    def __init__(self,**kwargs):
        self.htmlContent=BeautifulSoup(kwargs['htmlContent'],'html.parser')
        self.startingRange=kwargs['startingRange']
        self.endingRange=kwargs['endingRange']
        
    
    def buildMapping(self):
        print("Parsing website and getting neccessary details!")
        time.sleep(2)
        try:
            for i in range(self.startingRange,self.endingRange+1):
                heading=self.htmlContent.find(self.headingPattern,id='calibre_link-'+str(i))
                programs=[]
                element=heading.next_sibling
                while True:
                    if element.name!=None:
                        if bool(re.search(self.headingPattern,element.name)):
                            break
                        if 'programs' in element['class']:
                            programs.append(element)
                    element=element.next_sibling
                self.headingToProgramsMap[heading] = programs
        except Exception as e:
            print(f"{e}")
    
    def getHtmlDetails(self):
        print("Generating HTML...")
        time.sleep(2)
        try:
            scrappedHtmlContent=str()
            scrappedHtmlContent+="<html><body>"
            for heading, programs in self.headingToProgramsMap.items():
                scrappedHtmlContent+=str(heading)
                for program in programs:
                    scrappedHtmlContent+=str(program)
            scrappedHtmlContent+="</body></html>"
            return scrappedHtmlContent
        except Exception as e:
            print(f"{e}")
    
    