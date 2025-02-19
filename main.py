import pyinputplus as pyip
from classes.index import FetchDetails, ScrapWeb, HtmlToPdf,customURL, chapterPattern
import re

url=pyip.inputCustom(customURL,prompt="Enter URL from Automate Boring Stuff With python website: ")
startingRange=pyip.inputNum("Enter starting range of heading want to get: ",min=1)
endingRange=pyip.inputNum("Enter ending range of heading want to get: ",min=1)
    
chapterNo = re.search(chapterPattern,url).group()

htmlContent = FetchDetails.getHtmlContent(url)

scrapWeb=ScrapWeb(htmlContent=htmlContent,startingRange=startingRange,endingRange=endingRange)
scrapWeb.buildMapping()
htmlDetails=scrapWeb.getHtmlDetails()

htmlToPdf = HtmlToPdf(chapterNo,htmlDetails)

htmlToPdf.generatePdf()
    




