import weasyprint
from pathlib import Path
import os
import time

class HtmlToPdf:
    fileName=str()
    
    def __init__(self,fileName,htmlContent):
        self.fileName+=f"{fileName}.pdf"
        self.htmlContent=htmlContent
        
    def generatePdf(self):
        print("Generating pdf...")
        time.sleep(2)
        currPath=Path.cwd()
        try:
            os.mkdir(f"{currPath}/chapters-pdf")
        except Exception as e:
            print(e)
        weasyprint.HTML(string=self.htmlContent).write_pdf(f"{currPath}/chapters-pdf/{self.fileName}")
        print("Pdf Generated Successfuly!")
            
        
    
    
    