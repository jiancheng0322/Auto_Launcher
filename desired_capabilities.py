from appium import webdriver
import xlrd


def get_desired_capabilities():
    """
    生成连接对象，caps信息为可变信息
    """
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "9",
        "appPackage": "com.dangbei.leard.leradlauncher",
        "appActivity": ".ui.splash.SplashActivity",
        "deviceName": "10.192.28.156:5555",
        "automationName": "Appium",
        "noReset": "True"
    }
    return desired_caps


def get_uri():
    return "http://localhost:4723/wd/hub"
