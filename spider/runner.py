# -*- coding: utf-8 -*-
# @Time : 2023/12/23 17:27
# @Author : cmh
# @File : runner.py
# @Project : python
import ssl

from spider.system.novel.novel_38xs import Novel38XS
from utils.logger import LogManager


def init_ssl():
    ssl._create_default_https_context = ssl._create_unverified_context


class Runner:

    def __init__(self):
        super().__init__()
        self.logger = LogManager.get_logger("Runner")

    def get_novel(self):
        novel = Novel38XS("择日飞升", "/138414/78596196.html")
        novel.get_total_novel()

if __name__ == "__main__":
    init_ssl()
    runner = Runner()
    runner.get_novel()

