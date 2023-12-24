# -*- coding: utf-8 -*-
# @Time : 2023/12/23 20:16
# @Author : cmh
# @File : logger.py
# @Project : python
import logging
import sys
import time
import traceback
from types import MethodType

# log级别定义，从高到低
CRITICAL = logging.CRITICAL
ERROR = logging.ERROR
WARNING = logging.WARN
WARN = logging.WARN
INFO = logging.INFO
DEBUG = logging.DEBUG

# 日志输出流
STREAM = "stream"
SYSLOG = "syslog"
FILE = "file"
CUSTOME = "custom"


def log_compact_traceback(self):
    self.error(traceback.format_exc())


class LogManager(object):
    created_modules = set()
    log_level = DEBUG
    log_handle = STREAM
    log_tag = ''
    sa_log_tag = ''
    run_tag = ''
    sys_logger = None
    custom_handler = None
    asyncwrite = False

    @staticmethod
    def set_asyncwrite(asyncwrite):
        pass

    @staticmethod
    def set_run_tag(run_tag):
        LogManager.run_tag = run_tag

    @staticmethod
    def run_message(message):
        if LogManager.run_tag:
            with open(LogManager.run_tag, "wa") as f:
                f.write(message)
                f.write('\n')
        print(message, sys.stderr)

    @staticmethod
    def get_logger(moduleName):
        # If we have it already, return it directly
        if LogManager.log_handle == SYSLOG and LogManager.sys_logger is not None:
            return logging.LoggerAdapter(LogManager.sys_logger, {'modulename': moduleName})

        if moduleName in LogManager.created_modules:
            return logging.getLogger(moduleName)
        logger = logging.getLogger(moduleName)
        logger.log_last_except = MethodType(log_compact_traceback, logger)
        logger.setLevel(LogManager.log_level)
        # add the handlers to logger
        logger.addHandler(LogManager._create_handler(logger))
        LogManager.created_modules.add(moduleName)

        if LogManager.log_handle == SYSLOG and LogManager.sys_logger is not None:
            return logging.LoggerAdapter(LogManager.sys_logger, {'modulename': moduleName})

        return logger

    @staticmethod
    def _create_handler(logger):
        formatlist = ['%(asctime)s', LogManager.log_tag, '%(name)s', '%(levelname)s', '%(message)s']
        if LogManager.log_handle == SYSLOG:
            ch = logging.FileHandler(LogManager.log_tag + "_" + time.strftime("%Y%m%d_%H%M%S") + '.log',
                                     encoding='utf8')
        elif LogManager.log_handle == FILE:
            ch = logging.FileHandler(LogManager.log_tag + "_" + time.strftime("%Y%m%d_%H%M%S") + '.log',
                                     encoding='utf8')
        elif LogManager.log_handle == CUSTOME:
            ch = LogManager.custom_handler()
        else:
            ch = logging.StreamHandler()

        ch.setLevel(LogManager.log_level)
        # create formatter and add it to the handlers
        formatter = logging.Formatter(' - '.join(formatlist))
        ch.setFormatter(formatter)

        return ch

    @staticmethod
    def set_log_level(lv):
        LogManager.log_level = lv
        for name in LogManager.created_modules:
            logging.getLogger(name).setLevel(lv)

    @staticmethod
    def set_log_handle(handle):
        LogManager.log_handle = handle
        for name in LogManager.created_modules:
            logger = logging.getLogger(name)
            logger.handlers = []
            logger.addHandler(LogManager._create_handler(logger))

    @staticmethod
    def set_log_tag(log_tag):
        LogManager.log_tag = log_tag
        for name in LogManager.created_modules:
            logger = logging.getLogger(name)
            logger.handlers = []
            logger.addHandler(LogManager._create_handler(logger))

    @staticmethod
    def set_sa_log_tag(tag):
        """设置运维日志tag"""
        LogManager.sa_log_tag = tag

    @staticmethod
    def set_custom_handler(handler):
        LogManager.log_handle = CUSTOME
        LogManager.custom_handler = handler