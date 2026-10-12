# -*- coding: utf-8 -*-
# @Time : 2024/2/15 21:03
# @Author : cmh
# @File : novel_uukanshu.py
# @Project : python
import re

from system.novel.novel import Novel


class NovelCZ(Novel):

    def __init__(self, name, start_suffix):
        super().__init__(name, "", start_suffix, True)
        self.set_re_str()

    def set_re_str(self):
        self.title_re_str = r'<div\s+class\s*=\s*"name"[^>]*>([\s\S]*?)</div>'
        self.next_url_re_str = r'<a\s+class\s*=\s*"next-chapter"\s+href="(.*?)"'
        self.content_re_str = r'<div\s+class\s*=\s*"content"[^>]*>([\s\S]*?)</div>'
        self.part_re_str = r'<p>([\s\S]*?)</p>'

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
