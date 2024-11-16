from Regex import Regex

def customURL(url):
    if bool(Regex.urlPattern(url))==False:
        raise Exception('This url is not from Automate Boring Stuff With python website')