import traceback
from appium import webdriver
# 引入刚刚创建的同目录下的desired_capabilities.py
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from unittestreport import TestRunner
# import sqltest
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
import PicMatch


# from time import *


def getTime():
    # tamp = int(time.time())
    # time_local = time.localtime(tamp)
    # dt = time.strftime("%H:%M:%S", time_local)
    nowtime = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    return nowtime


class MyTest(TestCase):
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

    def getScreenShot(self, name):
        """
        self.driver.screenshot = pyautogui.screenshot()
        image = self.driver.screenshot.save('%s.png' % name)
        return image

        #driver = self.driver
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/%s.png' % name
        self.driver.get_screenshot_as_file(image_file)
        """
        time.sleep(2)
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/Launcher_test/screenshots/%s.png' % name
        logging.info('get %s screenshot' % name)
        self.driver.get_screenshot_as_file(image_file)
        # full_path = os.path.abspath(image)
        return image_file

        # filename = 'D:/bug/%s.png' % nowtime
        # self.driver.get_screenshot_as_file(filename)

    def test_1_1(self):
        """1.搜索页面,搜索ob 2.检查搜素结果，并跳转播放"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("up", 5)
        time.sleep(2)
        board.remotecontrol("ok")
        board.remotecontrol("ok")
        time.sleep(2)
        image1 = self.getScreenShot("test_01")
        print(image1)
        score = PicMatch.calculate_pixel_difference("D:/bug/wjc_test/screen01.png", image1)
        print(f"Similarity Score: {score}")
        PicMatch.determine(self, "D:/bug/wjc_test/screen01.png", image1)

    def test_1_2(self):
        """1.拉起状态栏 2.进入我的应用 3.检查页面展示"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("up", 5)
        time.sleep(2)
        board.lianxu("right", 1)
        board.lianxu("ok", 1)
        image2 = self.getScreenShot("test_02")
        print(image2)
        score = PicMatch.calculate_pixel_difference("D:/bug/wjc_test/screen02.png", image2)
        print(f"Similarity Score: {score}")
        PicMatch.determine(self, "D:/bug/wjc_test/screen02.png", image2)

    def test_1_3(self):
        """1.拉起状态栏 2.点击天气 3.查看天气显示是否正常 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("up", 5)
        board.lianxu("right", 3)
        board.lianxu("ok", 1)
        board.lianxu("right", 2)
        board.lianxu("ok", 1)
        board.lianxu("back", 1)
        image3 = self.getScreenShot("test_03")
        print(image3)
        score = PicMatch.calculate_pixel_difference("D:/bug/wjc_test/screen03.png", image3)
        print(f"Similarity Score: {score}")
        PicMatch.determine(self, "D:/bug/wjc_test/screen03.png", image3)
        time.sleep(3)
        board.lianxu("up", 1)
        board.lianxu("ok", 2)

    def test_1_4(self):
        """1.拉起状态栏 2.点击模式切换 3.切换到长辈模式 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("up", 5)
        board.lianxu("right", 7)
        board.lianxu("ok", 1)
        image4 = self.getScreenShot("test_04")
        print(image4)
        score = PicMatch.calculate_pixel_difference("D:/bug/wjc_test/screen04.png", image4)
        print(f"Similarity Score: {score}")
        PicMatch.determine(self, "D:/bug/wjc_test/screen04.png", image4)

    def test_1_5(self):
        """1.进入组件添加页 2.添加观看记录大组件 3.检查组件添加是否成功 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("up", 2)
        board.lianxu("right", 7)
        board.lianxu("ok", 1)
        board.lianxu("down", 1)
        board.lianxu("right", 1)
        board.lianxu("ok", 1)
        board.lianxu("back", 1)
        image5 = self.getScreenShot("test_05")
        score = PicMatch.calculate_pixel_difference("D:/bug/wjc_test/screen05.png", image5)
        print(f"Similarity Score: {score}")
        PicMatch.determine(self, "D:/bug/wjc_test/screen05.png", image5)

    def test_1_6(self):
        """1.进入组件添加页 2.点击恢复组件按钮 3.检查组件是否恢复默认 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("up", 2)
        board.lianxu("right", 7)
        board.lianxu("ok", 1)
        board.lianxu("right", 13)
        board.lianxu("ok", 2)
        image6 = self.getScreenShot("test_06")
        score = PicMatch.calculate_pixel_difference("D:/bug/wjc_test/screen06.png", image6)
        print(f"Similarity Score: {score}")
        PicMatch.determine(self, "D:/bug/wjc_test/screen06.png", image6)

    def test_1_7(self):
        """1.进入组件桌面 2.切换热播电视剧组件类型 3.检查类型切换是否成功 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("up", 2)
        board.lianxu("right", 1)
        board.lianxu("menu", 1)
        board.lianxu("ok", 1)
        image7 = self.getScreenShot("test_07")
        score = PicMatch.calculate_pixel_difference("D:/bug/wjc_test/screen07.png", image7)
        print(f"Similarity Score: {score}")
        PicMatch.determine(self, "D:/bug/wjc_test/screen07.png", image7)

    def test_1_8(self):
        """1.进入组件桌面 2.移动组件 3.检查组件移动是否成功 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("up", 2)
        board.lianxu("menu", 1)
        board.lianxu("ok", 1)
        board.lianxu("right", 2)
        board.lianxu("ok", 1)
        image8 = self.getScreenShot("test_08")
        score = PicMatch.calculate_pixel_difference("D:/bug/wjc_test/screen08.png", image8)
        print(f"Similarity Score: {score}")
        PicMatch.determine(self, "D:/bug/wjc_test/screen08.png", image8)

    def test_1_9(self):
        """1.进入组件桌面 2.删除组件 3.检查组件删除是否成功 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("up", 1)
        board.lianxu("menu", 1)
        board.lianxu("down", 3)
        board.lianxu("ok", 1)
        image9 = self.getScreenShot("test_09")
        score = PicMatch.calculate_pixel_difference("D:/bug/wjc_test/screen09.png", image9)
        print(f"Similarity Score: {score}")
        PicMatch.determine(self, "D:/bug/wjc_test/screen09.png", image9)

    def test_2_1(self):
        """1.进入应用导航栏 2.移动应用 3.检查应用移动是否成功 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("up", 1)
        board.lianxu("right", 1)
        board.lianxu("menu", 1)
        board.lianxu("ok", 1)
        board.lianxu("right", 1)
        board.lianxu("ok", 1)
        image10 = self.getScreenShot("test_10")
        PicMatch.determine(self, "D:/bug/wjc_test/screen10.png", image10)

    def test_2_2(self):
        """1.进入应用导航栏 2.删除应用 3.检查应用删除是否成功 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("up", 1)  # 按1次上键
        board.lianxu("right", 5)  # 按5次右键
        board.lianxu("menu", 1)  # 按1次菜单键
        board.lianxu("down", 3)  # 按3次下键
        board.lianxu("ok", 1)  # 按1次OK键
        image11 = self.getScreenShot("test_11")  # 截取当前页面，并命名为test_11.png
        PicMatch.determine(self, "D:/bug/wjc_test/screen11.png",
                           image11)  # 将预期结果的图片D:/bug/wjc_test/screen11.png与截取的图片进行对比

    def test_2_3(self):
        """1.进入应用导航栏 2.替换应用 3.检查应用替换是否成功 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("up", 1)
        board.lianxu("right", 4)
        board.lianxu("menu", 1)
        board.lianxu("down", 1)
        board.lianxu("ok", 1)
        image12 = self.getScreenShot("test_12")
        PicMatch.determine(self, "D:/bug/wjc_test/screen12.png", image12)

    def test_2_4(self):
        """1.进入我的应用 2.下载应用 3.检查应用下载是否成功 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("up", 1)
        board.lianxu("ok", 1)
        board.lianxu("up", 1)
        board.lianxu("ok", 1)
        board.lianxu("right", 1)
        board.lianxu("ok", 1)
        image13 = self.getScreenShot("test_13")
        PicMatch.determine(self, "D:/bug/wjc_test/screen13.png", image13)

    def test_2_5(self):
        """1.标准模式首页拉起状态栏 2.查看状态栏展示 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("up", 6)
        image14 = self.getScreenShot("test_14")
        PicMatch.determine(self, "D:/bug/wjc_test/screen14.png", image14)

    def test_2_6(self):
        """1.进入个人中心 2.拉起登录二维码 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("ok", 1)
        board.lianxu("up", 1)
        board.lianxu("ok", 1)
        image15 = self.getScreenShot("test_15")
        PicMatch.determine(self, "D:/bug/wjc_test/screen15.png", image15)

    def test_2_7(self):
        """1.进入个人中心 2.跳转观看记录 3.点击去看一看 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("ok", 1)
        board.lianxu("down", 2)
        image16 = self.getScreenShot("test_16")
        PicMatch.determine(self, "D:/bug/wjc_test/screen16.png", image16)

    def test_2_8(self):
        """1.进入个人中心 2.跳转收藏的影片 3.点击去看一看 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("ok", 1)
        board.lianxu("down", 3)
        image17 = self.getScreenShot("test_17")
        PicMatch.determine(self, "D:/bug/wjc_test/screen17.png", image17)

    def test_2_9(self):
        """1.进入个人中心 2.跳转收藏的专题 3.点击去看一看 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("ok", 1)
        board.lianxu("down", 3)
        image18 = self.getScreenShot("test_18")
        PicMatch.determine(self, "D:/bug/wjc_test/screen18.png", image18)

    def test_3_1(self):
        """1.进入个人中心 2.跳转收藏的明星 3.点击去看一看 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("ok", 1)
        board.lianxu("down", 4)
        image19 = self.getScreenShot("test_19")
        PicMatch.determine(self, "D:/bug/wjc_test/screen19.png", image19)

    def test_3_2(self):
        """1.进入个人中心 2.跳转我的预约 3.点击去看一看 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("ok", 1)
        board.lianxu("down", 5)
        image20 = self.getScreenShot("test_20")
        PicMatch.determine(self, "D:/bug/wjc_test/screen20.png", image20)

    def test_3_3(self):
        """1.进入我的tab 2.跳转首页选择 3.切换首页 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 6)
        board.lianxu("ok", 1)
        image21 = self.getScreenShot("test_21")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen21.png", image21)

    def test_3_4(self):
        """1.进入我的tab 2.跳转设置 3.检查拉起设置页面 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 6)
        board.lianxu("left", 2)
        board.lianxu("ok", 1)
        image22 = self.getScreenShot("test_22")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen22.png", image22)

    def test_3_5(self):
        """1.进入我的tab 2.跳转帮助与反馈 3.检查拉起页面 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 6)
        board.lianxu("left", 1)
        board.lianxu("ok", 1)
        image23 = self.getScreenShot("test_23")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen23.png", image23)

    def test_3_6(self):
        """1.进入我的tab 2.跳转消息设置 3.检查拉起页面 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 6)
        board.lianxu("right", 1)
        board.lianxu("ok", 1)
        image24 = self.getScreenShot("test_24")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen24.png", image24)

    def test_3_7(self):
        """1.进入我的tab 2.跳转自定义背景 3.检查拉起页面 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 6)
        board.lianxu("right", 2)
        board.lianxu("ok", 1)
        image25 = self.getScreenShot("test_25")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen25.png", image25)

    def test_3_8(self):
        """1.进入我的tab 2.跳转皮肤 3.检查拉起页面 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 6)
        board.lianxu("right", 3)
        board.lianxu("ok", 1)
        image26 = self.getScreenShot("test_26")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen26.png", image26)

    def test_3_9(self):
        """1.进入我的tab 2.跳转播放器 3.检查拉起页面 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 7)
        board.lianxu("ok", 1)
        image27 = self.getScreenShot("test_27")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen27.png", image27)

    def test_4_1(self):
        """1.进入我的tab 2.跳转订购信息 3.检查拉起页面 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 7)
        board.lianxu("left", 1)
        board.lianxu("ok", 1)
        image28 = self.getScreenShot("test_28")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen28.png", image28)

    def test_4_2(self):
        """1.进入我的tab 2.跳转屏保 3.检查拉起页面 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 7)
        board.lianxu("left", 2)
        board.lianxu("ok", 1)
        image29 = self.getScreenShot("test_29")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen29.png", image29)

    def test_4_3(self):
        """1.进入我的tab 2.跳转关于本机 3.检查拉起页面 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 7)
        board.lianxu("right", 1)
        board.lianxu("ok", 1)
        image30 = self.getScreenShot("test_30")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen30.png", image30)

    def test_4_4(self):
        """1.进入我的tab 2.跳转用户协议 3.检查拉起页面 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 7)
        board.lianxu("right", 2)
        board.lianxu("ok", 1)
        image31 = self.getScreenShot("test_31")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen31.png", image31)

    def test_4_5(self):
        """1.进入我的tab 2.跳转影视会员收银台 3.查看单个会员信息 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 1)
        board.lianxu("ok", 1)
        #board.lianxu("back", 1)
        image32 = self.getScreenShot("test_32")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen32.png", image32)

    def test_4_6(self):
        """1.进入我的tab 2.跳转音乐会员收银台 3.查看单个会员信息 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 1)
        board.lianxu("right", 1)
        board.lianxu("ok", 1)
        #board.lianxu("back", 1)
        image33 = self.getScreenShot("test_33")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen33.png", image33)

    def test_4_7(self):
        """1.进入我的tab 2.跳转K歌会员收银台 3.查看单个会员信息 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 1)
        board.lianxu("right", 2)
        board.lianxu("ok", 1)
        #board.lianxu("back", 1)
        image34 = self.getScreenShot("test_34")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen34.png", image34)

    def test_4_8(self):
        """1.进入我的tab 2.跳转少儿会员收银台 3.查看单个会员信息 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 1)
        board.lianxu("right", 3)
        board.lianxu("ok", 1)
        #board.lianxu("back", 1)
        image35 = self.getScreenShot("test_35")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen35.png", image35)

    def test_4_9(self):
        """1.进入我的tab 2.跳转体育会员收银台 3.查看单个会员信息 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 1)
        board.lianxu("right", 4)
        board.lianxu("ok", 1)
        #board.lianxu("back", 1)
        image36 = self.getScreenShot("test_36")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen36.png", image36)

    def test_5_1(self):
        """1.进入我的tab 2.跳转少儿会员收银台 3.查看单个会员信息 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 6)
        board.lianxu("down", 1)
        board.lianxu("right", 5)
        board.lianxu("ok", 1)
        #board.lianxu("back", 1)
        image37 = self.getScreenShot("test_37")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen37.png", image37)

    def test_5_2(self):
        """1.进入首页 2.首页媒资点击菜单键 3.点击收藏影片 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("down", 1)
        board.lianxu("menu", 1)
        board.lianxu("down", 1)
        board.lianxu("ok", 1)
        image38 = self.getScreenShot("test_38")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen38.png", image38)

    def test_5_3(self):
        """1.进入播放详情页 2.移动到最上方 3.点击收藏影片 """
        driver = self.driver
        time.sleep(10)
        board.lianxu("down", 1)
        board.lianxu("ok", 1)
        board.lianxu("up", 3)
        board.lianxu("up", 3)
        board.lianxu("ok", 1)
        image39 = self.getScreenShot("test_39")
        board.lianxu("back", 1)
        PicMatch.determine(self, "D:/bug/wjc_test/screen39.png", image39)

    def test_5_4(self):
        """1.进入导航栏 2.删除导航"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("right", 9)
        board.lianxu("menu", 1)
        board.lianxu("down", 2)
        board.lianxu("ok", 1)
        board.lianxu("right", 4)
        board.lianxu("ok", 1)
        image40 = self.getScreenShot("test_40")
        PicMatch.determine(self, "D:/bug/wjc_test/screen40.png", image40)

    def test_5_5(self):
        """1.进入导航栏 2.移动导航"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("right", 5)
        board.lianxu("menu", 1)
        board.lianxu("ok", 1)
        board.lianxu("right", 1)
        board.lianxu("ok", 1)
        image41 = self.getScreenShot("test_41")
        PicMatch.determine(self, "D:/bug/wjc_test/screen41.png", image41)

    def test_5_6(self):
        """1.进入导航栏 2.添加导航"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("right", 12)
        board.lianxu("ok", 1)
        board.lianxu("down", 2)
        board.lianxu("ok", 1)
        image42 = self.getScreenShot("test_42")
        PicMatch.determine(self, "D:/bug/wjc_test/screen42.png", image42)

    def test_5_7(self):
        """1.播放短剧 2.查看播放是否正常及是否是沉浸式详情页"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("up", 6)
        board.lianxu("ok", 1)
        board.lianxu("left", 1)
        board.lianxu("down", 1)
        board.lianxu("ok", 1)
        board.lianxu("up", 2)
        board.lianxu("right", 2)
        board.lianxu("ok", 2)
        board.lianxu("up", 1)
        board.lianxu("left", 1)
        board.lianxu("ok", 1)
        board.lianxu("right", 5)
        board.lianxu("up", 1)
        board.lianxu("right", 4)
        board.lianxu("down", 1)
        board.lianxu("ok", 1)
        board.lianxu("left", 1)
        board.lianxu("ok", 2)
        board.lianxu("back", 2)
        image43 = self.getScreenShot("test_43")
        PicMatch.determine(self, "D:/bug/wjc_test/screen43.png", image43)

    def test_5_8(self):
        """1.进入少儿二级页 2.检查少儿二级页页面展示"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 1)
        board.lianxu("ok", 1)
        image44 = self.getScreenShot("test_44")
        PicMatch.determine(self, "D:/bug/wjc_test/screen44.png", image44)

    def test_5_9(self):
        """1.进入首页导航二级页 2.检查二级页页面展示"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("ok", 1)
        image45 = self.getScreenShot("test_45")
        PicMatch.determine(self, "D:/bug/wjc_test/screen45.png", image45)

    def test_6_1(self):
        """1.进入电影导航二级页 2.检查二级页页面展示"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("right", 1)
        board.lianxu("ok", 1)
        image46 = self.getScreenShot("test_46")
        PicMatch.determine(self, "D:/bug/wjc_test/screen46.png", image46)

    def test_6_2(self):
        """1.进入电视剧导航二级页 2.检查二级页页面展示"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("right", 2)
        board.lianxu("ok", 1)
        image47 = self.getScreenShot("test_47")
        PicMatch.determine(self, "D:/bug/wjc_test/screen47.png", image47)

    def test_6_3(self):
        """1.进入综艺导航二级页 2.检查二级页页面展示"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("right", 3)
        board.lianxu("ok", 1)
        image48 = self.getScreenShot("test_48")
        PicMatch.determine(self, "D:/bug/wjc_test/screen48.png", image48)

    def test_6_4(self):
        """1.进入动漫导航二级页 2.检查二级页页面展示"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("right", 4)
        board.lianxu("ok", 1)
        image49 = self.getScreenShot("test_49")
        PicMatch.determine(self, "D:/bug/wjc_test/screen49.png", image49)

    def test_6_5(self):
        """1.进入播放详情页 2.点击会员按钮跳转收银台"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("down", 1)
        board.lianxu("ok", 1)
        board.lianxu("right", 1)
        board.lianxu("ok", 1)
        image50 = self.getScreenShot("test_50")
        PicMatch.determine(self, "D:/bug/wjc_test/screen50.png", image50)

    def test_6_6(self):
        """1.进入普通播放详情页 2.点击会员banner位跳转收银台"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("down", 1)
        board.lianxu("ok", 1)
        board.lianxu("right", 2)
        board.lianxu("ok", 1)
        image51 = self.getScreenShot("test_51")
        PicMatch.determine(self, "D:/bug/wjc_test/screen51.png", image51)

    def test_6_7(self):
        """1.进入应用中心导航-搜索 2.搜索应用并点击进行下载"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("left", 2)
        board.lianxu("down", 3)
        board.lianxu("ok", 3)
        board.lianxu("right", 5)
        board.lianxu("ok", 1)
        board.lianxu("ok", 2)
        image52 = self.getScreenShot("test_52")
        PicMatch.determine(self, "D:/bug/wjc_test/screen52.png", image52)

    def test_6_8(self):
        """1.进入首页导航 2.进入排行榜 3.查看排行榜内容展示"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("down", 12)
        board.lianxu("up", 2)
        board.lianxu("ok", 1)
        image53 = self.getScreenShot("test_53")
        PicMatch.determine(self, "D:/bug/wjc_test/screen53.png", image53)

    def test_6_9(self):
        """1.进入首页导航 2.进入vip专区 3.查看专区内容展示"""
        driver = self.driver
        time.sleep(10)
        board.lianxu("down", 1)
        board.lianxu("ok", 1)
        time.sleep(5)
        board.lianxu("back", 1)
        board.lianxu("down", 8)
        board.lianxu("right", 3)
        board.lianxu("ok", 1)
        image54 = self.getScreenShot("test_54")
        PicMatch.determine(self, "D:/bug/wjc_test/screen54.png", image54)




    def tearDown(self):
        self.driver.quit()
    # 测试结束，退出会话。


if __name__ == '__main__':
    unittest.main()
