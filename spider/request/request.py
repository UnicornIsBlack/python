# -*- coding: utf-8 -*-
# @Time : 2023/12/23 17:26
# @Author : cmh
# @File : request.py
# @Project : python
import gzip
import os
import socket
import urllib.request as urllib2
from contextlib import contextmanager
from http.cookiejar import CookieJar

import socks

from utils.singleton import SingletonClass


class Request(SingletonClass):

    def __init__(self):
        super().__init__()
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        self.headers = {
            "User-Agent": self.user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip",
        }
        self.timeout = float(os.getenv("NOVEL_REQUEST_TIMEOUT", "20"))
        self.use_proxy = os.getenv("NOVEL_USE_SOCKS", "1").lower() not in {
            "0", "false", "no", "off"
        }
        self.proxy_host = os.getenv("NOVEL_SOCKS_HOST", "127.0.0.1")
        self.proxy_port = int(os.getenv("NOVEL_SOCKS_PORT", "10800"))
        self.opener = urllib2.build_opener(
            urllib2.HTTPCookieProcessor(CookieJar())
        )

    @contextmanager
    def _socks_proxy(self):
        """Route urllib's socket through the configured SOCKS5 proxy."""
        if not self.use_proxy:
            yield
            return

        original_socket = socket.socket
        previous_proxy = socks.get_default_proxy()
        socks.set_default_proxy(socks.SOCKS5, self.proxy_host, self.proxy_port)
        socket.socket = socks.socksocket
        try:
            yield
        finally:
            socket.socket = original_socket
            if previous_proxy is None:
                socks.set_default_proxy(None)
            else:
                socks.set_default_proxy(*previous_proxy)

    def ungzip(self, data):
        try:
            data = gzip.decompress(data)
        except:
            pass
        return data

    def get_response(self, url):
        request = urllib2.Request(url, headers=self.headers)
        with self._socks_proxy():
            try:
                response = self.opener.open(request, timeout=self.timeout)
                data = response.read()
                encoding = response.headers.get("Content-Encoding", "")
            except urllib2.HTTPError as error:
                if error.code == 403:
                    raise RuntimeError(
                        "HTTP 403 Forbidden: %s (请确认 SOCKS5 代理 %s:%s 可用)"
                        % (url, self.proxy_host, self.proxy_port)
                    ) from error
                raise

        if "gzip" in encoding.lower():
            data = self.ungzip(data)
        return data.decode("utf-8", "ignore")
