# -*- coding: utf-8 -*-
# @Time : 2023/12/23 20:17
# @Author : cmh
# @File : singleton.py
# @Project : python


class Singleton(type):

    def __init__(cls, name, bases, dic):
        super().__init__(name, bases, dic)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class SingletonClass(metaclass=Singleton):
    pass