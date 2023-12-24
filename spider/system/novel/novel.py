# -*- coding: utf-8 -*-
# @Time : 2023/12/23 17:54
# @Author : cmh
# @File : novel.py
# @Project : python

import re
import time
from collections import defaultdict

from spider.request.request import Request
from utils.logger import LogManager


class Novel:
    def __init__(self, name, uri, start_suffix):
        super().__init__()
        self.uri = uri
        self.request = Request()
        self.name = name

        self.logger = LogManager.get_logger("Novel")

        self._chapter2content = defaultdict(list)
        self._chapters = []
        self._cur_suffix = start_suffix

        self._title_re_str = None
        self._next_url_re_str = None
        self._content_re_str = None
        self._part_re_str = None

    @property
    def title_re_str(self):
        return self._title_re_str

    @title_re_str.setter
    def title_re_str(self, re_str):
        self._title_re_str = re_str

    @property
    def next_url_re_str(self):
        return self._next_url_re_str

    @next_url_re_str.setter
    def next_url_re_str(self, re_str):
        self._next_url_re_str = re_str

    @property
    def content_re_str(self):
        return self._content_re_str

    @content_re_str.setter
    def content_re_str(self, re_str):
        self._content_re_str = re_str

    @property
    def part_re_str(self):
        return self._part_re_str

    @part_re_str.setter
    def part_re_str(self, re_str):
        self._part_re_str = re_str

    def set_next_url_re_str(self, next_url_re_str):
        self.next_url_re_str = next_url_re_str

    def get_cur_url(self):
        return self.uri + self._cur_suffix

    def get_cur_response(self):
        return self.request.get_response(self.get_cur_url())

    @staticmethod
    def get_re_result(content, re_str):
        match = re.compile(re_str)
        results = match.findall(content)
        return results[0] if results else ""

    def get_parts(self, content):
        part_re = re.compile(self.part_re_str)
        tmp_parts = part_re.findall(content)
        parts = []
        for part in tmp_parts:
            parts.append(part.strip() + "\n")
        return parts[:-1] if parts else parts

    def get_cur_chapter(self):
        response = self.get_cur_response()

        title = self.get_re_result(response, self.title_re_str).strip()

        content = self.get_re_result(response, self.content_re_str)
        parts = self.get_parts(content)

        self.logger.info(title)
        if title:
            self._chapter2content[title].extend(parts)
        if title not in self._chapters:
            self._chapters.append(title)

        self._cur_suffix = self.get_re_result(response, self.next_url_re_str)

    def get_total_novel(self):
        i = 0
        while self._cur_suffix:
            self.get_cur_chapter()
            time.sleep(0.1)
            i += 1
        self.write_to_file()

    def write_to_file(self):
        with open("../Download/Novel/%s.txt" % self.name, "w", encoding="UTF-8") as f:
            for chapter in self._chapters:
                f.write("%s\n" % chapter)
                contents = self._chapter2content.get(chapter, [])
                f.writelines(contents)
