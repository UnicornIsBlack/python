# -*- coding: utf-8 -*-
# @Time : 2023/12/23 17:54
# @Author : cmh
# @File : novel.py
# @Project : python

import re
from collections import defaultdict
from pathlib import Path

from request.request import Request
from utils.language import Language
from utils.logger import LogManager


class Novel:
    def __init__(self, name, uri, start_suffix, is_t2s=False):
        super().__init__()
        self.uri = uri
        self.request = Request()
        self.name = name

        self.logger = LogManager.get_logger("Novel")

        self._chapter2content = defaultdict(list)
        self._chapters = []
        self._cur_suffix = start_suffix
        self._is_t2s = is_t2s        # 繁体转简体
        self._language = Language()

        self._chapter_idx = -1
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
        if self._cur_suffix.startswith(("http://", "https://")):
            return self._cur_suffix
        if self._cur_suffix.startswith("//"):
            return "https:" + self._cur_suffix
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

    def get_cur_content(self, response):
        return self.get_re_result(response, self.content_re_str)

    def get_title(self, response):
        return self.get_re_result(response, self.title_re_str).strip()

    def get_cur_chapter(self):
        response = self.get_cur_response()
        if self._is_t2s:
            response = self._language.traditional_to_simplified(response)
        # self.logger.info(response)
        title = self.get_title(response)
        self.logger.info(title)

        content = self.get_cur_content(response)
        # self.logger.info(content)
        parts = self.get_parts(content)
        if not parts:
            self.logger.warn(content)

        if title:
            self._chapter2content[title].extend(parts)
        if title not in self._chapters:
            self._chapters.append(title)

        self._cur_suffix = self.get_re_result(response, self.next_url_re_str)
        # self.logger.info(self._cur_suffix)

    def get_total_novel(self):
        i = 0
        re_try_cnt = 0
        while self._cur_suffix and (self._chapter_idx == -1 or i < self._chapter_idx):
            try:
                self.get_cur_chapter()
                is_exception = False
            except Exception as e:
                is_exception = True
                self.logger.error(e)
            # time.sleep(0.1)
            if is_exception:
                if re_try_cnt < 10:
                    re_try_cnt += 1
                    continue
                else:
                    break
            re_try_cnt = 0
            i += 1
        self.write_to_file()

    def write_to_file(self):
        output_dir = Path(__file__).resolve().parents[3] / "Download" / "Novel"
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / ("%s.txt" % self.name)
        with output_file.open("w", encoding="UTF-8") as f:
            for chapter in self._chapters:
                f.write("\n%s\n" % chapter)
                contents = self._chapter2content.get(chapter, [])
                f.writelines(contents)
