import traceback
from appium import webdriver
# 引入刚刚创建的同目录下的desired_capabilities.py
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from unittestreport import TestRunner
import sqltest
import sftp
import desired_capabilities
import board
from unittest import TestCase
# 我们使用python的unittest作为单元测试工具
import unittest
# 使用time.sleep(xx)函数进行等待
import appium_oper
import basic_oper
import public_methods
import time
import random
import re
import logging
import os
import datetime


# from time import *


def getTime():
    # tamp = int(time.time())
    # time_local = time.localtime(tamp)
    # dt = time.strftime("%H:%M:%S", time_local)
    nowtime = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    return nowtime


class MyTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(1, 1)

    def test_two(self):
        self.assertEqual(2, 2)

    def test_fail(self):
        self.assertEqual(1, 2)  # 这会导致测试失败

    def test_error(self):
        raise ValueError("这是一个错误")  # 这会导致测试产生错误


if __name__ == '__main__':
    unittest.main()
