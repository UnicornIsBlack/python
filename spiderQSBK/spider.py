__author__ = "chai"
__copyright__ = "Copyright 2017"
__version__ = "0.0.1"

import urllib.request as urllib2

class QSBK:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) '\
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            url = 'http://www.baidu.com/'
            # url = 'https://www.google.com/'
            request = urllib2.Request(url, headers = self.headers)
            # request.set_proxy('127.0.0.1:10800', 'http')
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf8')
            print(pageCode)

        except urllib2.URLError as e:
            print(e)


q = QSBK()
q.getPage(1)