# -*- coding: utf-8 -*-
# @Time : 2024/9/25 14:42
# @Author : cmh
# @File : novel_zz.py
# @Project : python
from system.novel.novel import Novel


class NovelZZ(Novel):

    def __init__(self, name, start_suffix):
        super().__init__(name, "http://www.zzs5.info/", start_suffix, True)
        self.set_re_str()
        # self._chapter_idx = 200

    def set_re_str(self):
        self.title_re_str = r'<h1>(.*?)</h1>'
        self.next_url_re_str = r'&rarr; <a href="(.*?)">下一章<'
        self.content_re_str = r'                    <div class="content">([\s\S]*?)</div>'
        self.part_re_str = r'<p>([\s\S]*?)</p>'

    def get_title1(self, response):
        title = self.get_re_result(response, self.title_re_str).strip()
        strs = title.split(" ")
        if len(strs) < 2:
            return title
        return "第" + strs[0] + "章 " + strs[1]

    def get_parts(self, content):
        content = content.replace("&nbsp;", "")
        if "<p>" in content:
            tmp_parts = content.split("<p>")
        else:
            content = content.replace("<br />", "<br/>")
            tmp_parts = content.split("<br/>")
        parts = []
        for part in tmp_parts:
            part = part.strip()
            if not part:
                continue
            parts.append(part + "\n")
        return parts
