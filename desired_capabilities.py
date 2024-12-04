from appium import webdriver
import xlrd

import argparse
"""
# 设置命令行参数
parser = argparse.ArgumentParser()
IP = parser.add_argument('--IP', type=str, help='IP parameter',default="10.192.110.137")
android = parser.add_argument('--android', type=str, help='android parameter',default="11")
args = parser.parse_args()
print(IP)
print(android)
"""
def get_desired_capabilities():
    """
    生成连接对象，caps信息为可变信息
    """

    desired_caps = {
        "platformName": "Android",
        "platformVersion": "9",
        "appPackage": "com.dangbei.leard.leradlauncher",
        "appActivity": ".ui.splash.SplashActivity",
        "deviceName": "10.192.35.60",
        "automationName": "Appium",
        "noReset": "True"
    }
    return desired_caps


def get_uri():
    # return "http://127.0.0.1:4724/wd/hub"
    return "http://localhost:4723/wd/hub"
