# -*- coding: utf-8 -*-
# @Time : 2023/12/23 22:12
# @Author : cmh
# @File : novel_38xs.py
# @Project : python
from spider.system.novel.novel import Novel


class Novel38XS(Novel):
    
    def __init__(self, name, start_suffix):
        super().__init__(name, "https://www.38xs.com", start_suffix)
        self.set_re_str()

    def set_re_str(self):
        self.title_re_str = r'<div class="bookname"><h1>(.*?)</h1>'
        self.next_url_re_str = r'<a id="pager_next" href="(.*?)"'
        self.content_re_str = r'<div id="content">(.*?)</div>'
        self.part_re_str = r'<p>(.*?)</p>'