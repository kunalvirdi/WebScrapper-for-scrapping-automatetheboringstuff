from classes.Regex import urlPattern
import re
def customURL(url):
    if bool(re.search(urlPattern,url))==False:
        raise Exception('This url is not from Automate Boring Stuff With python website')