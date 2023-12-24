# -*- coding: utf-8 -*-
# @Time : 2023/12/23 17:26
# @Author : cmh
# @File : request.py
# @Project : python

import urllib.request as urllib2

from utils.singleton import SingletonClass


class Request(SingletonClass):

    def __init__(self):
        super().__init__()
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        self.headers = {"User-Agent": self.user_agent}

    def get_response(self, url):
        request = urllib2.Request(url, headers=self.headers)
        response = urllib2.urlopen(request)
        return response.read().decode("utf8")