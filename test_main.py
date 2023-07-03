import traceback

from appium import webdriver
# 引入刚刚创建的同目录下的desired_capabilities.py
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from unittestreport import TestRunner

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


class MqcTest(TestCase):
    global automationName

    def setUp(self):
        # 获取我们设定的capabilities，通知Appium Server创建相应的会话。
        desired_caps = desired_capabilities.get_desired_capabilities()
        # 获取server的地址。
        uri = desired_capabilities.get_uri()
        # 获取使用的测试框架
        self.automationName = desired_caps.get('automationName')
        # 创建会话，得到driver对象，driver对象封装了所有的设备操作。
        self.driver = webdriver.Remote(uri, desired_caps)

    def getScreenShot(self, module):
        errtime = getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, errtime)

        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)
        # log = os.path.join(os.getcwd(), 'err_png\\err_{}.log'.format(errtime))
        log = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/err_{}.log'.format(errtime)
        with open(log, 'w') as f:
            traceback.print_exc(file=f)
        traceback.print_exc()
        return False

        # filename = 'D:/bug/%s.png' % nowtime
        # self.driver.get_screenshot_as_file(filename)

    def test_1_search(self):
        """1.搜索页面,搜索jlxj去播放视频 2.清除所有搜索 3.搜索qmxq去下载应用 4.返回搜索页面"""
        driver = self.driver
        board.remotecontrol("backhome")
        time.sleep(8)
        try:
            for i in range(0, 4):
                board.remotecontrol("up")
                time.sleep(1)
            board.remotecontrol("ok")
            time.sleep(1)
            """搜索nc"""
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.FrameLayout[2]/android.widget.TextView")
            time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]/android.widget.TextView")
            time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView[2]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout")
            time.sleep(3)
            num1 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.TextView[1]")
            text1 = num1.text
            print(text1)
            time.sleep(1)
            self.assertEqual(text1, "怒潮")
            time.sleep(2)
            for i in range(0, 3):
                board.remotecontrol("back")
                time.sleep(1)
            # 清空搜索内容,重新搜索qmxq
            basic_oper.click_by_id(driver,
                                   "com.dangbei.leard.leradlauncher:id/view_search_key_board_search_keyboard_clear_v")
            time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.FrameLayout[5]/android.widget.TextView")
            time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.FrameLayout[1]/android.widget.TextView")
            time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.FrameLayout[6]/android.widget.TextView")
            time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.FrameLayout[5]/android.widget.TextView")
            time.sleep(1)
            """跳转到应用，点击全民象棋"""
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView")
            time.sleep(1)
            basic_oper.click_by_id(driver, "com.dangbei.leard.leradlauncher:id/app_rank_item_tag_view")
            board.remotecontrol("up")
            basic_oper.click_by_id(driver,
                                   "com.dangbei.leard.leradlauncher:id/view_tertical_app_header_item_download_text_tv")  # 点击下载
            time.sleep(10)
            if basic_oper.check_by_xpath(driver,
                                         "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.Button[1]")

        except (NoSuchElementException, TimeoutException):
            self.getScreenShot("test_search")
            return False

    def test_Personal1(self):
        """1.进入个人中心-观看记录 2.点击观看记录播放影片 3.播放成功后返回删除该条观看记录"""
        driver = self.driver
        # board.remotecontrol("backhome")
        try:
            board.remotecontrol("backhome")
            time.sleep(8)
            """进入个人中心"""
            board.remotecontrol("left")
            time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
            time.sleep(1)
            basic_oper.is_toast_exist(driver, "会员中心")
            time.sleep(1)
            # basic_oper.click_by_text(driver,"观看记录")
            """查看观看记录"""
            if basic_oper.check_by_name_contains(driver, "观看记录"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.RelativeLayout/android.widget.TextView")
            time.sleep(2)
            board.remotecontrol("right")
            time.sleep(1)
            board.remotecontrol("ok")
            if basic_oper.check_by_name_contains(driver, "全屏"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView")
                print("播放视频成功")
            board.remotecontrol("back")
            time.sleep(1)
            board.remotecontrol("back")
            time.sleep(1)
            board.remotecontrol("right")
            time.sleep(1)
            num1 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView")
            text1 = num1.text
            print(text1)
            time.sleep(2)
            board.remotecontrol("menu")
            time.sleep(1)
            if basic_oper.check_by_name_contains(driver, "删除本条记录"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")

            time.sleep(1)
            num2 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView")
            text2 = num2.text
            print(text2)
            self.assertNotEqual(text1, text2)
        except (NoSuchElementException, TimeoutException):
            self.getScreenShot("test_Personal1")
            return False

    def test_Personal2(self):
        """1.进入个人中心，去收藏一部影片后删除；2.若已有收藏的影片，则先全部删除然后点击去看一看"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(8)
            board.remotecontrol("left")
            time.sleep(1)
            """进入个人中心"""
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
            if basic_oper.check_by_name_contains(driver, "收藏的影片"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.RelativeLayout/android.widget.TextView")
            time.sleep(1)
            if basic_oper.check_by_name_contains(driver, "去看一看"):
                basic_oper.click_by_id(driver,
                                       "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")  # 点击去看一看
                time.sleep(1)
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout")
                time.sleep(1)
                if basic_oper.check_by_name_contains(driver, "收藏"):
                    basic_oper.click_by_xpath(driver,
                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.TextView")
                    time.sleep(1)
            else:
                board.remotecontrol("right")
                time.sleep(1)
                board.remotecontrol("menu")
                time.sleep(1)
                if basic_oper.check_by_name_contains(driver, "删除全部收藏"):
                    basic_oper.click_by_xpath(driver,
                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.TextView")
                    time.sleep(1)
                if basic_oper.check_by_name_contains(driver, "去看一看"):
                    basic_oper.click_by_id(driver,
                                           "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")  # 点击去看一看
                    time.sleep(1)
                    basic_oper.click_by_xpath(driver,
                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout")
                    time.sleep(1)
                    if basic_oper.check_by_name_contains(driver, "收藏"):
                        basic_oper.click_by_xpath(driver,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.TextView")
        except (NoSuchElementException, TimeoutException):
            self.getScreenShot("test_Personal2")
            # return False,

    def test_Personal3(self):
        """
        1.进入收藏的专题，去收藏一个专题后删除
        2.若已有收藏的专题，则先全部删除然后点击去看一看"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(8)
            board.remotecontrol("left")
            time.sleep(1)
            """进入个人中心"""
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
            if basic_oper.check_by_name_contains(driver, "收藏的专题"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[5]/android.widget.RelativeLayout/android.widget.TextView")
                time.sleep(2)
                if basic_oper.check_by_name_contains(driver, "去看一看"):
                    basic_oper.click_by_id(driver,
                                           "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")  # 点击去看一看
                    time.sleep(1)
                    if basic_oper.check_by_name_contains(driver, "超燃科幻"):
                        board.remotecontrol("down")
                        time.sleep(2)
                        basic_oper.click_by_text_contains(driver, "超燃科幻")
                        time.sleep(2)
                    basic_oper.click_by_xpath(driver,
                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.ImageView")
                    time.sleep(5)
                    board.remotecontrol("right")
                    time.sleep(1)
                    basic_oper.click_by_id(driver,
                                           "com.dangbei.leard.leradlauncher:id/activity_film_topic_collection_rl")  # 点击爱心
                    time.sleep(1)
                else:
                    board.remotecontrol("right")
                    time.sleep(2)
                    board.remotecontrol("menu")
                    time.sleep(2)
                    if basic_oper.check_by_name_contains(driver, "删除全部收藏"):
                        basic_oper.click_by_xpath(driver,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.TextView")
                        time.sleep(2)
                    if basic_oper.check_by_name_contains(driver, "去看一看"):
                        basic_oper.click_by_id(driver,
                                               "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")  # 点击去看一看
                        time.sleep(2)
                        if basic_oper.check_by_name_contains(driver, "超燃科幻"):
                            basic_oper.click_by_xpath(driver,
                                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.RelativeLayout/android.widget.TextView")
                        time.sleep(2)
                        basic_oper.click_by_xpath(driver,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.ImageView")
                        time.sleep(5)
                        board.remotecontrol("right")
                        time.sleep(1)
                        basic_oper.click_by_id(driver,
                                               "com.dangbei.leard.leradlauncher:id/activity_film_topic_collection_rl")  # 点击爱心
        except (NoSuchElementException, TimeoutException):
            # return False,
            self.getScreenShot("test_Personal3")

    def test_Personal4(self):
        """
        1.进入收藏的明星，去收藏一个明星后删除
        2.若已有收藏的明星，则先全部删除然后点击去看一看"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(8)
            board.remotecontrol("left")
            time.sleep(1)
            """进入个人中心"""
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
            if basic_oper.check_by_name_contains(driver, "收藏的明星"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[6]/android.widget.RelativeLayout/android.widget.TextView")
                time.sleep(1)
                if basic_oper.check_by_name_contains(driver, "去看一看"):
                    basic_oper.click_by_id(driver,
                                           "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")  # 点击去看一看
                    time.sleep(1)
                    basic_oper.click_by_xpath(driver,
                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout")
                    time.sleep(2)
                    board.remotecontrol("down")
                    time.sleep(2)
                    board.remotecontrol("down")
                    time.sleep(2)
                    board.remotecontrol("down")
                    time.sleep(1)
                    if basic_oper.check_by_name_contains(driver, "相关艺人"):
                        basic_oper.click_by_id(driver,
                                               "com.dangbei.leard.leradlauncher:id/base_people_item_select_name_tv")
                    basic_oper.click_by_id(driver,
                                           "com.dangbei.leard.leradlauncher:id/activity_star_topic_detail_collection_view")  # 点击爱心

                    board.remotecontrol("back")
                    time.sleep(1)
                    board.remotecontrol("back")
                    time.sleep(1)
                    board.remotecontrol("back")
                    time.sleep(1)
                    board.remotecontrol("back")  # 返回到收藏的专题页
                    time.sleep(1)
                    board.remotecontrol("right")
                    time.sleep(1)
                    board.remotecontrol("menu")
                    if basic_oper.check_by_name_contains(driver, "删除全部收藏"):
                        basic_oper.click_by_xpath(driver,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.TextView")
                else:
                    board.remotecontrol("right")
                    board.remotecontrol("menu")
                    if basic_oper.check_by_name_contains(driver, "删除全部收藏"):
                        basic_oper.click_by_xpath(driver,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.TextView")
                    time.sleep(1)
                    if basic_oper.check_by_name_contains(driver, "去看一看"):
                        basic_oper.click_by_id(driver,
                                               "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")  # 点击去看一看
                        time.sleep(1)
                        basic_oper.click_by_xpath(driver,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout")
                        time.sleep(2)
                        board.remotecontrol("down")
                        time.sleep(2)
                        board.remotecontrol("down")
                        time.sleep(2)
                        board.remotecontrol("down")
                        if basic_oper.check_by_name_contains(driver, "相关艺人"):
                            basic_oper.click_by_id(driver,
                                                   "com.dangbei.leard.leradlauncher:id/base_people_item_select_name_tv")
                        time.sleep(1)
                        basic_oper.click_by_id(driver,
                                               "com.dangbei.leard.leradlauncher:id/activity_star_topic_detail_collection_view")  # 点击爱心
        except (NoSuchElementException, TimeoutException):
            self.getScreenShot("test_Personal4")

    def test_Personal5(self):  # 没有预约页面了，改用例删除
        """
        1.进入我的预约，去预约一部影片
        2.若已有预约的影片，则先全部删除然后点击去看一看"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            board.remotecontrol("down")
            """进入个人中心"""
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
            if basic_oper.check_by_name_contains(driver, "我的预约"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[7]/android.widget.RelativeLayout/android.widget.TextView")
                if basic_oper.check_by_name_contains(driver, "去看一看"):
                    basic_oper.click_by_id(driver,
                                           "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")  # 点击去看一看
                    basic_oper.click_by_xpath(driver,
                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout")
                    if basic_oper.check_by_name_contains(driver, "预约"):
                        basic_oper.click_by_xpath(driver,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.TextView")

                    board.remotecontrol("back")
                    time.sleep(1)
                    board.remotecontrol("back")  # 返回到收藏的专题页
                    time.sleep(1)
                    board.remotecontrol("right")
                    time.sleep(2)
                    board.remotecontrol("menu")
                    if basic_oper.check_by_name_contains(driver, "取消全部预约"):
                        basic_oper.click_by_xpath(driver,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.TextView")
                else:
                    board.remotecontrol("right")
                    board.remotecontrol("menu")
                    if basic_oper.check_by_name_contains(driver, "取消全部预约"):
                        basic_oper.click_by_xpath(driver,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.TextView")
                    if basic_oper.check_by_name_contains(driver, "去看一看"):
                        basic_oper.click_by_id(driver,
                                               "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")  # 点击去看一看
                        basic_oper.click_by_xpath(driver,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout")
                        time.sleep(1)
                        basic_oper.click_by_id(driver,
                                               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.TextView")  # 点击预约
        except (NoSuchElementException, TimeoutException):
            self.getScreenShot("test_Personal5")

    def test_myjob1(self):
        """
        1.进入我的应用，移动应用"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(8)
            for i in range(0, 5):
                board.remotecontrol("left")
                time.sleep(1)
            board.remotecontrol("down")
            time.sleep(1)
            board.remotecontrol("down")
            time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[6]/android.widget.TextView")
            time.sleep(2)
            board.remotecontrol("ok")
            time.sleep(1)
            # text1=driver.find_element_by_xpath("aaa").text
            num1 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.TextView")
            text1 = num1.text
            print(text1)
            time.sleep(2)
            board.remotecontrol("menu")
            time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.TextView")
            board.remotecontrol("right")
            time.sleep(1)
            board.remotecontrol("ok")
            num2 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.FrameLayout/android.widget.TextView")
            text2 = num2.text
            print(text2)
            time.sleep(2)
            self.assertEqual(self, text1, text2)

        except (NoSuchElementException, TimeoutException):
            self.getScreenShot("test_myjob1")

    # TODO 弹出下载弹窗后，点击ok键出现异常
    def test_myjob2(self):
        """
        1.进入我的应用，去应用市场下载一个排行榜的应用
        2.下载完成后卸载，查看是否卸载成功"""
        driver = self.driver
        try:
            # 进入我的应用
            board.remotecontrol("backhome")
            time.sleep(8)
            for i in range(0, 5):
                board.remotecontrol("left")
                time.sleep(1)
            board.remotecontrol("down")
            time.sleep(1)
            board.remotecontrol("down")
            time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[6]/android.widget.TextView")
            time.sleep(2)
            board.remotecontrol("ok")
            time.sleep(1)
            # 进入应用市场
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.View[2]")
            time.sleep(2)
            # 获取下载的应用名称
            num1 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.TextView")
            text1 = num1.text
            print(text1)
            time.sleep(1)
            # 点击下载该应用
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout")
            time.sleep(2)
            basic_oper.click_by_id(driver,
                                   "com.dangbei.leard.leradlauncher:id/view_tertical_app_header_item_download_text_tv")
            time.sleep(1)
            # 弹出确认下载弹窗，点击确认
            # board.remotecontrol("ok")
            basic_oper.click_by_xpath(driver, "com.dangbei.leard.leradlauncher:id/dialog_remind_confirm_tv")
            time.sleep(1)
            board.remotecontrol("back")
            # 等待下载成功
            time.sleep(5)
            for i in range(0, 3):
                board.remotecontrol("back")
                time.sleep(1)
            num2 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.FrameLayout/android.widget.TextView")
            text2 = num2.text
            print(text2)
            time.sleep(2)
            self.assertEqual(self, text1, text2)
            print("下载成功")
            # 执行删除下载的应用
            time.sleep(1)
            board.remotecontrol("down")
            time.sleep(1)
            board.remotecontrol("menu")
            time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.TextView")
            time.sleep(2)
        except (NoSuchElementException, TimeoutException):
            self.getScreenShot("test_myjob2")

    def test_movie1(self):
        """进入芒果tv二级页播放视频"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(2)
            board.remotecontrol("down")
            board.remotecontrol("down")
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[7]/android.widget.TextView")
            text1 = public_methods.gettext(driver,
                                           "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[3]")
            if self.assertEqual(text1, "芒果专区"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.View[2]")
                time.sleep(2)
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView")
                board.remotecontrol("back")
                board.remotecontrol("back")
        except (NoSuchElementException, TimeoutException):
            # return False, \
            self.getScreenShot("test_movie1")

    # 以下模块调试成功

    def test_desktop1(self):
        """在卡片桌面移动组件"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(8)
            for i in range(0, 4):
                board.remotecontrol("up")
                time.sleep(1)
            board.remotecontrol("down")
            time.sleep(1)
            board.remotecontrol("right")
            time.sleep(1)
            board.remotecontrol("menu")
            """移动组件"""
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
            time.sleep(1)
            board.remotecontrol("right")
            time.sleep(1)
            board.remotecontrol("ok")

        except (NoSuchElementException, TimeoutException):
            # return False, \
            self.getScreenShot("test_desktop1")

    def test_desktop2(self):
        """在卡片桌面添加组件"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(8)
            for i in range(0, 4):
                board.remotecontrol("up")
                time.sleep(1)
            board.remotecontrol("down")
            time.sleep(1)
            for i in range(0, 5):
                board.remotecontrol("right")
                time.sleep(1)
            board.remotecontrol("ok")
            time.sleep(1)
            for i in range(0, 4):
                board.remotecontrol("down")
                time.sleep(1)
            board.remotecontrol("right")
            time.sleep(1)
            board.remotecontrol("ok")
            time.sleep(2)
            board.remotecontrol("back")
            board.remotecontrol("back")
        except (NoSuchElementException, TimeoutException):
            # return False, \
            self.getScreenShot("test_desktop2")

    def test_desktop3(self):
        """在卡片桌面移除组件"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(8)
            for i in range(0, 4):
                board.remotecontrol("up")
                time.sleep(1)
            board.remotecontrol("down")
            for i in range(0, 6):
                board.remotecontrol("right")
                time.sleep(1)
            board.remotecontrol("left")
            time.sleep(1)
            board.remotecontrol("menu")
            time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.TextView")
        except (NoSuchElementException, TimeoutException):
            # return False, \
            self.getScreenShot("test_desktop3")

    def test_changemode1(self):
        """标准模式切换到长辈模式"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(8)
            for i in range(0, 4):
                board.remotecontrol("up")
                time.sleep(1)
            for i in range(0, 3):
                board.remotecontrol("right")
                time.sleep(1)
            board.remotecontrol("ok")
            time.sleep(2)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.TextView")
            time.sleep(2)
            num = driver.find_element_by_id("com.dangbei.leard.leradlauncher:id/elder_home_record_view_title_tv")
            text = num.text
            print(text)
            self.assertEqual(text, "观看记录")
            """恢复环境：回到标准模式"""
            time.sleep(2)
            for i in range(0, 4):
                board.remotecontrol("up")
                time.sleep(1)
            board.remotecontrol("ok")
            time.sleep(1)
            board.remotecontrol("ok")
        except (NoSuchElementException, TimeoutException):
            # return False, \
            self.getScreenShot("test_changemode1")

    def test_deskchoice(self):
        """进入我的tab下，进行桌面选择"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(8)
            for i in range(0, 5):
                board.remotecontrol("left")
                time.sleep(1)
            for i in range(0, 7):
                board.remotecontrol("down")
                time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.FrameLayout[3]/android.view.View")
            print("切换为瀑布流桌面")
            time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.ImageView")

        except (NoSuchElementException, TimeoutException):
            # return False,
            self.getScreenShot("my_deskchoice")

    def test_messageSetting(self):
        """进入消息设置，关闭消息提示"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(8)
            for i in range(0, 4):
                board.remotecontrol("left")
                time.sleep(1)
            for i in range(0, 7):
                board.remotecontrol("down")
                time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.FrameLayout[4]/android.widget.TextView")
            print("关闭消息提示")
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.View")
            time.sleep(2)
            print("确认关闭")
            basic_oper.click_by_id(driver, "com.dangbei.leard.leradlauncher:id/dialog_remind_confirm_tv")

            """关闭后恢复环境，重新打开消息提示开关"""
            time.sleep(2)
            basic_oper.click_by_id(driver, "com.dangbei.leard.leradlauncher:id/dialog_remind_confirm_tv")

        except (NoSuchElementException, TimeoutException):
            # return False,
            self.getScreenShot("test_messageSetting")

    def test_background(self):
        """进入自定义背景，更换背景"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(8)
            for i in range(0, 4):
                board.remotecontrol("left")
                time.sleep(1)
            for i in range(0, 7):
                board.remotecontrol("down")
                time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.FrameLayout[5]/android.widget.TextView")
            time.sleep(2)
            """切换到静态背景"""
            board.remotecontrol("up")
            time.sleep(1)
            board.remotecontrol("right")
            time.sleep(1)
            board.remotecontrol("down")
            time.sleep(1)
            board.remotecontrol("ok")
            time.sleep(1)
            """设为背景"""
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView")
            if basic_oper.check_by_name_contains(driver, "背景设置成功"):
                print("背景切换成功")
        except (NoSuchElementException, TimeoutException):
            # return False,
            self.getScreenShot("test_background")

    def test_skin(self):
        """来回切换珍珠白、暗夜黑皮肤"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(8)
            for i in range(0, 4):
                board.remotecontrol("left")
                time.sleep(1)
            for i in range(0, 7):
                board.remotecontrol("down")
                time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.FrameLayout[6]/android.widget.TextView")
            time.sleep(1)
            board.remotecontrol("down")
            time.sleep(1)
            board.remotecontrol("ok")
            """切回珍珠白"""
            board.remotecontrol("up")
            time.sleep(1)
            board.remotecontrol("ok")
        except (NoSuchElementException, TimeoutException):
            # return False,
            self.getScreenShot("test_skin")

    def test_order(self):
        """进入订购信息页，跳转到收银台；断言为收银台页面的“立即登录"，在收银台跳转回订购信息页，断言为订购信息页的”订单信息"。"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(8)
            for i in range(0, 4):
                board.remotecontrol("left")
                time.sleep(1)
            for i in range(0, 7):
                board.remotecontrol("down")
                time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.FrameLayout[8]/android.widget.TextView")
            time.sleep(2)
            for i in range(0, 2):
                board.remotecontrol("down")
                time.sleep(1)
            board.remotecontrol("ok")
            time.sleep(1)
            """进入收银台，检验当前页面"""
            num1 = driver.find_element_by_id("com.dangbei.leard.leradlauncher:id/activity_vip_transaction_login_tv")
            text1 = num1.text
            print(text1)
            self.assertEqual(text1, "立即登录")
            """从收银台进入订购信息页"""
            time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.TextView")
            time.sleep(1)
            num2 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.TextView")
            text2 = num2.text
            print(text2)
            self.assertEqual(text2, "订单信息")
        except (NoSuchElementException, TimeoutException):
            # return False,
            self.getScreenShot("test_order")

    def test_Player(self):
        """播放器功能：切换软解播放器、系统播放器，重启后检查是否切换成功"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(8)
            for i in range(0, 4):
                board.remotecontrol("left")
                time.sleep(1)
            for i in range(0, 7):
                board.remotecontrol("down")
                time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.FrameLayout[9]/android.widget.TextView")
            time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.view.View")
            time.sleep(1)
            board.remotecontrol("back")
            # 切换播放器后，等待桌面重启
            if basic_oper.check_by_name_contains(driver, "设置成功"):
                print("切换播放器成功")
            time.sleep(5)
            board.remotecontrol("back")
            time.sleep(1)
            board.remotecontrol("back")
            time.sleep(1)
            board.remotecontrol("down")
            time.sleep(1)
            for i in range(0, 4):
                board.remotecontrol("left")
                time.sleep(1)
            for i in range(0, 7):
                board.remotecontrol("down")
                time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.FrameLayout[9]/android.widget.TextView")
            time.sleep(1)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.View")
        except (NoSuchElementException, TimeoutException):
            # return False,
            self.getScreenShot("test_Player")

    def test_About(self):
        """关于本机：确认是否能打开关于本机，并检验其中型号"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(8)
            public_methods.moreFunction()
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.FrameLayout[10]/android.widget.TextView")
            time.sleep(1)
            num = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.FrameLayout[2]/android.widget.TextView[2]")
            text = num.text
            print(text)
            self.assertEqual(text, "DBX3A")
        except (NoSuchElementException, TimeoutException):
            # return False,
            self.getScreenShot("test_Player")

    def test_bug(self):
        """回归用例：恢复出厂设置后，查看首页下方tab是否为空白"""
        driver = self.driver
        board.remotecontrol("backhome")
        time.sleep(2)
        board.remotecontrol("up")
        board.remotecontrol("up")
        board.remotecontrol("right")
        board.remotecontrol("ok")
        # basic_oper.click_by_xpath(driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.TextView")
        time.sleep(2)
        '''点击系统'''
        board.remotecontrol("down")
        board.remotecontrol("down")
        board.remotecontrol("down")
        board.remotecontrol("down")
        board.remotecontrol("down")
        board.remotecontrol("down")
        board.remotecontrol("down")
        # board.remotecontrol("ok")
        # basic_oper.click_by_text("系统")
        '''点击系统升级'''
        board.remotecontrol("left")
        board.remotecontrol("ok")
        '''点击系统版本升级'''
        board.remotecontrol("ok")
        time.sleep(10)
        '''点击立即下载'''
        basic_oper.click_by_id(driver, "com.dangbei.otaupgrade:id/main_center_common_btn")
        time.sleep(240)  # 等待下载完成，时间较长，预计4分钟
        '''点击立即升级'''
        basic_oper.click_by_id(driver, "com.dangbei.otaupgrade:id/main_center_common_btn")
        time.sleep(240)  # 等待验证完成并更新系统，更新完后等待开机，时间较长，预计4分钟
        board.remotecontrol("right")
        board.remotecontrol("ok")

        basic_oper.click_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")

    def test_button(self):
        """调试用"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(2)
            board.remotecontrol("up")
            board.remotecontrol("up")
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]")
            time.sleep(2)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[8]/android.widget.FrameLayout[2]")
            time.sleep(2)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]")
        except (NoSuchElementException, TimeoutException):
            # return False, \
            self.getScreenShot("test_button")

    def tearDown(self):
        self.driver.quit()
    # 测试结束，退出会话。


if __name__ == '__main__':
    unittest.main()
