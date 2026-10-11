# -*- coding: utf-8 -*-
# @Time : 2023/12/23 17:26
# @Author : cmh
# @File : request.py
# @Project : python
import gzip
import urllib.request as urllib2

import socks

from utils.singleton import SingletonClass


class Request(SingletonClass):

    def __init__(self):
        super().__init__()
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        self.headers = {"User-Agent": self.user_agent}
        # socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 10800)

    def ungzip(self, data):
        try:
            data = gzip.decompress(data)
        except:
            pass
        return data

    def get_response(self, url):

        request = urllib2.Request(url, headers=self.headers)
        response = urllib2.urlopen(request)
        for key, val in response.getheaders():
            # print(key, val)
            if key != "Content-Encoding":
                continue
            if val == "gzip":
                return self.ungzip(response.read()).decode()
        return response.read().decode("utf8", 'ignore')