import urllib.request

def GetHtmlWithUA(url):
    req = urllib.request.Request(url,data=None,headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    result = urllib.request.urlopen(req)
    html = result.read().decode('utf-8')
    return html
