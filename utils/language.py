# -*- coding: utf-8 -*-
# @Time : 2024/2/16 11:54
# @Author : cmh
# @File : language.py
# @Project : python


from opencc import OpenCC

from utils.singleton import SingletonClass


class Language(SingletonClass):

    def __init__(self):
        super().__init__()
        self._t2s = OpenCC("t2s")

    def traditional_to_simplified(self, text):
        return self._t2s.convert(text)
