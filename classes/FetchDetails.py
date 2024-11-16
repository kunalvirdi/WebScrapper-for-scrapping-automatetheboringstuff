import requests

class FetchDetails:
        
    @staticmethod
    def getHtmlContent(url):
        return requests.get(url).text