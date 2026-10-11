# -*- coding: utf-8 -*-
# @Time : 2023/12/23 17:27
# @Author : cmh
# @File : runner.py
# @Project : python
import ssl

from system.novel.novel_38xs import Novel38XS
from system.novel.novel_cz import NovelCZ
from system.novel.novel_uukanshu import NovelUU
from system.novel.novel_zz import NovelZZ
from utils.logger import LogManager


def init_ssl():
    ssl._create_default_https_context = ssl._create_unverified_context


class Runner:

    def __init__(self):
        super().__init__()
        self.logger = LogManager.get_logger("Runner")

    def get_novel(self):
        # novel = Novel38XS("我为长生仙", "/197880/85097155.html")
        # novel = NovelUU("仙路至尊", "/b/29893/55519.html")
        novel = NovelCZ("捞尸人", "https://czbooks.net/n/s6168f/s664m59h?chapterNumber=0")
        novel.get_total_novel()

if __name__ == "__main__":
    init_ssl()
    runner = Runner()
    runner.get_novel()

