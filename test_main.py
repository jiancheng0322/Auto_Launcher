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
        # 找到包含”Tab4”字符串的控件。
        """搜索页面"""
        driver = self.driver
        # board.remotecontrol("backhome")
        try:
            while True:
                board.remotecontrol("back")
                if appium_oper.find_ele_by_text_contains(driver, "杭州"):
                    break
            time.sleep(5)
            if basic_oper.check_by_name_contains(driver, "跳过全部"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]")
            board.remotecontrol("up")
            board.remotecontrol("up")
            board.remotecontrol("up")
            if basic_oper.check_by_xpath(driver,
                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.View[2]"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.View[2]")
            # board.remotecontrol("up")
            time.sleep(2)
            # board.remotecontrol("ok")

            """搜索jlxj"""
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[4]/android.widget.TextView")
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[6]/android.widget.TextView")
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.FrameLayout[6]/android.widget.TextView")
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[4]/android.widget.TextView")
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView[2]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout")
            if basic_oper.check_by_name_contains(driver, "全屏"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView")
                print("播放视频成功")
                time.sleep(5)
                board.remotecontrol("back")
            time.sleep(2)
            board.remotecontrol("back")
            board.remotecontrol("back")
            board.remotecontrol("back")
            """清空搜索内容,重新搜索qmxq"""
            basic_oper.click_by_id(driver,
                                   "com.dangbei.leard.leradlauncher:id/view_search_key_board_search_keyboard_clear_v")
            time.sleep(2)
            basic_oper.click_by_xpath(driver,
                                      "	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.FrameLayout[5]/android.widget.TextView")
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.FrameLayout[1]/android.widget.TextView")
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.FrameLayout[6]/android.widget.TextView")
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.FrameLayout[5]/android.widget.TextView")
            """跳转到应用，点击全民象棋"""
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView")
            time.sleep(2)
            basic_oper.click_by_id(driver, "com.dangbei.leard.leradlauncher:id/app_rank_item_tag_view")
            board.remotecontrol("up")
            basic_oper.click_by_id(driver,
                                   "com.dangbei.leard.leradlauncher:id/view_tertical_app_header_item_download_text_tv")  # 点击下载
            time.sleep(5)
            if basic_oper.check_by_name_contains(driver, "隐私政策和用户协议"):
                basic_oper.click_by_text(driver, "同意")
                time.sleep(5)
        except:
            self.getScreenShot("test_search")
            return False

    def test_Personal1(self):
        """进入个人中心-观看记录，点击观看记录播放影片，播放成功后返回删除该条观看记录"""
        driver = self.driver
        # board.remotecontrol("backhome")
        try:
            board.remotecontrol("backhome")
            time.sleep(2)
            board.remotecontrol("down")
            """进入个人中心"""
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")

            basic_oper.is_toast_exist(driver, "会员中心")
            # basic_oper.click_by_text(driver,"观看记录")
            """查看观看记录"""
            if basic_oper.check_by_name_contains(driver, "观看记录"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.RelativeLayout/android.widget.TextView")
            time.sleep(2)
            board.remotecontrol("right")
            board.remotecontrol("ok")
            if basic_oper.check_by_name_contains(driver, "全屏"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView")
                print("播放视频成功")
            board.remotecontrol("back")
            board.remotecontrol("back")
            board.remotecontrol("right")
            text1 = public_methods.gettext(driver,
                                           "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView")
            time.sleep(2)
            board.remotecontrol("menu")
            if basic_oper.check_by_name_contains(driver, "删除本条记录"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
            text2 = public_methods.gettext(driver,
                                           "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView")
            self.assertNotEqual(text1, text2)
        except:
            self.getScreenShot("test_PersonalCenter")
            return False

    def test_Personal2(self):
        """进入个人中心，去收藏一部影片后删除；若已有收藏的影片，则先全部删除然后点击去看一看"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(5)
            board.remotecontrol("down")
            """进入个人中心"""
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
            if basic_oper.check_by_name_contains(driver, "收藏的影片"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.RelativeLayout/android.widget.TextView")
            if basic_oper.check_by_name_contains(driver, "去看一看"):
                basic_oper.click_by_id(driver,
                                       "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")  # 点击去看一看
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout")
                if basic_oper.check_by_name_contains(driver, "收藏"):
                    basic_oper.click_by_xpath(driver,
                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.TextView")
                board.remotecontrol("back")
                time.sleep(2)
                board.remotecontrol("back")
                board.remotecontrol("back")  # 返回到收藏的影片页
                time.sleep(2)
                board.remotecontrol("right")
                time.sleep(2)
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
                if basic_oper.check_by_name_contains(driver, "去看一看"):
                    basic_oper.click_by_id(driver,
                                           "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")  # 点击去看一看
                    basic_oper.click_by_xpath(driver,
                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout")
                    if basic_oper.check_by_name_contains(driver, "收藏"):
                        basic_oper.click_by_xpath(driver,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.TextView")
        except (NoSuchElementException, TimeoutException):
            return False, self.getScreenShot("test_Personal2")


    def test_Personal3(self):
        """进入收藏的专题，去收藏一个专题后删除，若已有收藏的专题，则先全部删除然后点击去看一看"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            board.remotecontrol("down")
            """进入个人中心"""
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
            if basic_oper.check_by_name_contains(driver, "收藏的专题"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[5]/android.widget.RelativeLayout/android.widget.TextView")
                if basic_oper.check_by_name_contains(driver, "去看一看"):
                    basic_oper.click_by_id(driver,
                                           "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")  # 点击去看一看
                    if basic_oper.check_by_name_contains(driver, "超燃科幻"):
                        basic_oper.click_by_xpath(driver,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.RelativeLayout/android.widget.TextView")
                    basic_oper.click_by_xpath(driver,
                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.ImageView")
                    basic_oper.click_by_id(driver,"com.dangbei.leard.leradlauncher:id/activity_film_topic_collection_rl")   #点击爱心
                    board.remotecontrol("back")
                    time.sleep(2)
                    board.remotecontrol("back")
                    board.remotecontrol("back")  # 返回到收藏的专题页
                    time.sleep(2)
                    board.remotecontrol("right")
                    time.sleep(2)
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
                    if basic_oper.check_by_name_contains(driver, "去看一看"):
                        basic_oper.click_by_id(driver,
                                               "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")  # 点击去看一看
                        if basic_oper.check_by_name_contains(driver,"超燃科幻"):
                            basic_oper.click_by_xpath(driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.RelativeLayout/android.widget.TextView")
                        basic_oper.click_by_xpath(driver,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.ImageView")
                        time.sleep(2)
                        basic_oper.click_by_id(driver,
                                               "com.dangbei.leard.leradlauncher:id/activity_film_topic_collection_rl")   #点击爱心
        except (NoSuchElementException, TimeoutException):
            return False, self.getScreenShot("test_Personal3")


    def test_Personal4(self):
        """进入收藏的明星，去收藏一个明星后删除，若已有收藏的明星，则先全部删除然后点击去看一看"""
        driver = self.driver
        try:
            board.remotecontrol("backhome")
            time.sleep(3)
            board.remotecontrol("down")
            """进入个人中心"""
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
            if basic_oper.check_by_name_contains(driver, "收藏的明星"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[6]/android.widget.RelativeLayout/android.widget.TextView")
                if basic_oper.check_by_name_contains(driver, "去看一看"):
                    basic_oper.click_by_id(driver,
                                           "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")  # 点击去看一看
                    basic_oper.click_by_xpath(driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout")
                    time.sleep(2)
                    board.remotecontrol("down")
                    time.sleep(2)
                    board.remotecontrol("down")
                    time.sleep(2)
                    board.remotecontrol("down")
                    if basic_oper.check_by_name_contains(driver, "相关艺人"):
                        basic_oper.click_by_id(driver,
                                                  "com.dangbei.leard.leradlauncher:id/base_people_item_select_name_tv")
                    basic_oper.click_by_id(driver,
                                              "com.dangbei.leard.leradlauncher:id/activity_star_topic_detail_collection_view")# 点击爱心

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
                    if basic_oper.check_by_name_contains(driver, "去看一看"):
                        basic_oper.click_by_id(driver,
                                               "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")  # 点击去看一看

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
                        basic_oper.click_by_id(driver,
                                               "com.dangbei.leard.leradlauncher:id/activity_star_topic_detail_collection_view")  # 点击爱心
        except Exception as e:
            self.getScreenShot("test_PersonalCenter")
            return False

    def test_Personal5(self):
        """进入我的预约，去预约一部影片，若已有预约的影片，则先全部删除然后点击去看一看"""
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
        except Exception as e:
            self.getScreenShot("test_PersonalCenter")
            return False

    def test_myjob1(self):
        """进入我的应用，移动应用，测试环境为：组件桌面，我的应用置于第一位下方"""
        driver = self.driver
        while True:
            board.remotecontrol("back")
            if appium_oper.find_ele_by_xpath(driver, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.TextView[4]"):
                break
        basic_oper.click_by_xpath(driver,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.view.View[2]")
        # text1=driver.find_element_by_xpath("aaa").text
        text1 = public_methods.gettext(driver,
                                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.TextView")
        print(text1)
        time.sleep(2)
        #basic_oper.click_by_xpath(driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.TextView")

        #board.remotecontrol("down") #是否有更新应用弹框
        board.remotecontrol("down")
        board.remotecontrol("down")
        time.sleep(1)
        board.remotecontrol("menu")
        basic_oper.click_by_xpath(driver,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.TextView")
        board.remotecontrol("right")
        board.remotecontrol("right")
        board.remotecontrol("ok")
        text2 = public_methods.gettext(driver,
                                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.FrameLayout/android.widget.TextView")
        print(text2)
        """
        if text1 == text2:
            print("应用移动成功")
        else:
            return False
        """
        self.assertEqual(self,text1,text2)

    def test_myjob2(self):
        """进入我的应用，去应用市场下载一个排行榜的应用，下载完成后卸载，查看是否卸载成功"""
        driver = self.driver
        try:
            while True:
                board.remotecontrol("back")
                if appium_oper.find_ele_by_text_contains(driver, "杭州"):
                    break
            basic_oper.click_by_xpath(driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.view.View[2]")
            basic_oper.click_by_xpath(driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.View[2]")

            basic_oper.click_by_xpath(driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.TextView")
            test1=public_methods.gettext(driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView")
            basic_oper.click_by_xpath(driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView")

            board.remotecontrol("down")
            #basic_oper.click_by_text(driver,"下载")
            basic_oper.click_by_id(driver,"com.dangbei.leard.leradlauncher:id/view_tertical_app_header_item_download_text_tv")
            if appium_oper.wait_ele_by_xpath(driver,"同意",20):
                board.remotecontrol("back")
                board.remotecontrol("left")
                board.remotecontrol("ok")
            board.remotecontrol("back")
            board.remotecontrol("back")
            if basic_oper.check_by_name_contains(driver,test1):
                #board.remotecontrol("down")
                board.remotecontrol("down")
                board.remotecontrol("menu")
                basic_oper.click_by_xpath(driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.TextView")


        except:
            self.getScreenShot("test")

    def test_movie1(self):
        driver = self.driver
        try:
            while True:
                board.remotecontrol("back")
                if appium_oper.find_ele_by_text_contains(driver, "杭州"):
                    break
            board.remotecontrol("down")
            basic_oper.click_by_xpath(driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.ImageView")
            basic_oper.click_by_xpath(driver,"com.dangbei.leard.leradlauncher:id/view_item_secondary_menu_filter_name")     #点击筛选
            basic_oper.click_by_text_contains(driver,"免费")
            basic_oper.click_by_xpath(driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout")
            basic_oper.click_by_text_contains(driver, "全屏")
            board.remotecontrol("back")

        except (NoSuchElementException, TimeoutException):
            return False, self.getScreenShot("test_movie1")





    def test_button(self):
        driver = self.driver
        self.getScreenShot("test")

    def tearDown(self):
        # 测试结束，退出会话。
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

