import traceback

from appium import webdriver
# 引入刚刚创建的同目录下的desired_capabilities.py
import desired_capabilities
# 我们使用python的unittest作为单元测试工具
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
            time.sleep(2)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[6]/android.widget.TextView")
            time.sleep(2)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.FrameLayout[6]/android.widget.TextView")
            time.sleep(2)
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[4]/android.widget.TextView")
            time.sleep(2)
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

    def test_PersonalCenter(self):
        """个人中心"""
        driver = self.driver
        # board.remotecontrol("backhome")
        try:
            while True:
                board.remotecontrol("back")
                if appium_oper.find_ele_by_text_contains(driver, "杭州"):
                    break
            time.sleep(5)
            board.remotecontrol("down")
            """进入个人中心"""
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")

            basic_oper.is_toast_exist(driver, "会员中心")
            time.sleep(2)
            # basic_oper.click_by_text(driver,"观看记录")
            """查看观看记录"""
            if basic_oper.check_by_name_contains(driver, "观看记录"):
                basic_oper.click_by_xpath(driver,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.RelativeLayout/android.widget.TextView")
            time.sleep(2)
            basic_oper.check_by_name_contains(driver, "按菜单键删除记录")
            """进入收藏的影片，去收藏一部影片，并菜单键取消收藏"""
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.RelativeLayout")
            basic_oper.click_by_id(driver,
                                   "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")  # 点击去看一看
            time.sleep(2)
            board.remotecontrol("right")
            time.sleep(2)
            board.remotecontrol("ok")  # 搜索电影进行收藏
            basic_oper.click_by_text(driver, "收藏")
            if basic_oper.check_by_name_contains(driver, "收藏成功"):
                print("收藏电影成功")
            board.remotecontrol("back")
            time.sleep(2)
            board.remotecontrol("back")
            time.sleep(2)
            board.remotecontrol("back")
            """回到收藏的影片页面"""
            board.remotecontrol("right")
            # basic_oper.click_by_xpath(driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout")
            time.sleep(2)
            board.remotecontrol("menu")
            # basic_oper.click_by_xpath(driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]")
            basic_oper.click_by_xpath(driver,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
            if basic_oper.check_by_name_contains(driver, "去看一看"):
                print("删除影片成功")
        except:
            self.getScreenShot("test_PersonalCenter")

    def test_collect1(self):
        """进入收藏的专题，去收藏一个专题，并菜单键取消"""
        driver = self.driver
        board.remotecontrol("backhome")
        board.remotecontrol("down")
        """进入个人中心"""
        basic_oper.click_by_xpath(driver,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")

        basic_oper.click_by_xpath(driver,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[5]/android.widget.RelativeLayout")
        basic_oper.click_by_id(driver, "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")  # 点击去看一看
        board.remotecontrol("down")
        basic_oper.click_by_xpath(driver,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout")
        board.remotecontrol("up")
        time.sleep(2)
        board.remotecontrol("ok")
        if basic_oper.check_by_name_contains(driver, "收藏成功"):
            print("收藏专题成功")
        board.remotecontrol("back")
        board.remotecontrol("back")
        board.remotecontrol("back")
        """返回到收藏的专题页面"""
        board.remotecontrol("right")
        time.sleep(2)
        board.remotecontrol("menu")
        basic_oper.click_by_xpath(driver,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
        if basic_oper.check_by_name_contains(driver, "去看一看"):
            print("删除专题成功")

    def test_collect2(self):
        """进入收藏的明星，去收藏一个明星，并菜单键取消"""
        driver = self.driver
        board.remotecontrol("backhome")
        board.remotecontrol("down")
        """进入个人中心"""
        basic_oper.click_by_xpath(driver,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")

        basic_oper.click_by_xpath(driver,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[6]/android.widget.RelativeLayout")
        basic_oper.click_by_id(driver, "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")
        board.remotecontrol("down")
        board.remotecontrol("down")
        basic_oper.click_by_xpath(driver,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout")
        board.remotecontrol("down")
        board.remotecontrol("down")
        board.remotecontrol("ok")  # 点击明星
        board.remotecontrol("left")
        if basic_oper.check_by_name_contains(driver, "收藏成功"):
            print("收藏明星成功")
        board.remotecontrol("back")
        board.remotecontrol("back")
        board.remotecontrol("back")
        board.remotecontrol("back")
        board.remotecontrol("back")  # 回到收藏的明星页面
        board.remotecontrol("right")
        time.sleep(2)
        board.remotecontrol("menu")
        basic_oper.click_by_xpath(driver,
                                  "	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
        if basic_oper.check_by_name_contains(driver, "去看一看"):
            print("删除明星成功")

    def test_collect3(self):
        """进入我的预约，去预约一部影片，并菜单键取消"""
        driver = self.driver
        board.remotecontrol("backhome")
        board.remotecontrol("down")
        """进入个人中心"""
        basic_oper.click_by_xpath(driver,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")

        basic_oper.click_by_xpath(driver,
                                  "	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[7]/android.widget.RelativeLayout")
        basic_oper.click_by_id(driver, "com.dangbei.leard.leradlauncher:id/view_user_center_empty_look_btn")

        # basic_oper.click_by_xpath(driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout")
        board.remotecontrol("menu")
        basic_oper.click_by_id(driver, "com.dangbei.leard.leradlauncher:id/item_auto_location_option_tv")  # 点击预约
        if basic_oper.check_by_name_contains(driver, "您已预约，有更新讲为您短信提醒"):
            print("预约影片成功")
        board.remotecontrol("back")
        board.remotecontrol("right")
        board.remotecontrol("menu")
        basic_oper.click_by_xpath(driver,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
        if basic_oper.check_by_name_contains(driver, "去看一看"):
            print("删除预约成功")

    def test_myjob_move(self):
        """进入我的应用，移动应用，测试环境为：组件桌面，我的应用置于第一位下方"""
        driver = self.driver
        while True:
            board.remotecontrol("back")
            if appium_oper.find_ele_by_text_contains(driver, "杭州"):
                break
        basic_oper.click_by_xpath(driver,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[2]")
        # text1=driver.find_element_by_xpath("aaa").text
        text1 = public_methods.gettext(driver,
                                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.TextView")
        print(text1)
        time.sleep(2)
        board.remotecontrol("menu")
        basic_oper.click_by_xpath(driver,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.TextView")
        board.remotecontrol("right")
        board.remotecontrol("right")
        board.remotecontrol("ok")
        text2 = public_methods.gettext(driver,
                                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.FrameLayout/android.widget.TextView")
        if text1 == text2:
            print("应用移动成功")
        else:
            return False

    def test_myjob_delete(self):
        driver = self.driver
        try:
            while True:
                board.remotecontrol("back")
                if appium_oper.find_ele_by_text_contains(driver, "杭州"):
                    break
            basic_oper.click_by_xpath(driver, "")


        except:
            self.getScreenShot("test")

    def test_majob_delete(self):
        driver = self.driver
        while True:
            board.remotecontrol("back")
            if appium_oper.find_ele_by_text_contains(driver, "杭州"):
                break

    def test_button(self):
        driver = self.driver
        self.getScreenShot("test")


    def tearDown(self):
        # 测试结束，退出会话。
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()
