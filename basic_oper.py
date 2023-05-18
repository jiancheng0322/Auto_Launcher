"""
针对测试用例中的常见操作进行封装，包括：
元素点击
元素名称获取
"""
import appium_oper
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import board



def click_by_id(driver,id_info):
    '''
    通过id查找元素并点击
    '''
    get_target=appium_oper.wait_ele_by_id(driver,id_info)
    if get_target[0]:
        if type(get_target[1]) == str:
            raise Exception('元素%s对象获取失败'%(id_info))
        else:
            get_target[1].click()
            return True
    else:
        raise Exception('元素%s对象获取失败'%(id_info))

def sendtext_by_id(driver,id_info,text):
    '''
    通过id查找元素并输入文本
    '''
    get_target=appium_oper.wait_ele_by_id(driver,id_info)
    if get_target[0]:
        if type(get_target[1]) == str:
            raise Exception('元素%s对象获取失败'%(id_info))
        else:
            get_target[1].send_keys(text)
            return True
    else:
        raise Exception('元素%s对象获取失败'%(id_info))
def check_by_name_contains(driver,id_info):
    '''
    通过name查找元素并判断
    '''
    get_target=appium_oper.find_ele_by_text_contains(driver,id_info)
    if get_target[0]:
        if type(get_target[1]) == str:
            return False
        else:
            return True
    else:
        return False
def check_by_id(driver,id_info):
    '''
    通过id查找元素并判断
    '''
    get_target = appium_oper.wait_ele_by_id(driver, id_info)
    if get_target[0]:
        if type(get_target[1]) == str:
            raise Exception('元素%s对象获取失败'%(id_info))
        else:
            return True
    else:
        raise Exception('元素%s对象获取失败'%(id_info))

def check_by_xpath(driver,id_info):
    '''
    通过id查找元素并判断
    '''
    get_target = appium_oper.wait_ele_by_xpath(driver, id_info,5)
    if get_target[0]:
        if type(get_target[1]) == str:
            raise Exception('元素%s对象获取失败'%(id_info))
        else:
            return True
    else:
        raise Exception('元素%s对象获取失败'%(id_info))

def click_by_xpath(driver,xpath_info):
    '''
    通过xpath查找元素并点击
    '''
    get_target = appium_oper.wait_ele_by_xpath(driver,xpath_info,5)
    if get_target[0]:
        if type(get_target[1]) == str:
            raise Exception('元素%s对象获取失败' % (xpath_info))
        else:
            get_target[1].click()
            return True
    else:
        raise Exception('元素%s对象获取失败' % (xpath_info))
def get_id_is_checked(driver,id_info):
    """
    通过ID查找到元素，并且判断该对象是否被选择
    :param driver:
    :param id_info:
    :return:
    """
    get_target = appium_oper.wait_ele_by_id(driver, id_info)
    if get_target[0]:
        if type(get_target[1]) == str:
            raise Exception('元素%s对象获取失败'%(id_info))
        else:
            ischecked = get_target[1].get_attribute("checked")
            if ischecked =="true":
                return True,"元素已被选择"
            else:
                return False, "元素已被选择"
    else:
        raise Exception('元素%s对象获取失败'%(id_info))
def get_xpath_is_checked(driver,xpath_info):
    """
    通过xpath查找到元素，并且判断该对象是否被选择
    :param driver:
    :param xpath_info:
    :return:
    """
    get_target = appium_oper.wait_ele_by_id(driver, xpath_info)
    if get_target[0]:
        if type(get_target[1]) == str:
            raise Exception('元素%s对象获取失败'%(xpath_info))
        else:
            ischecked = get_target[1].get_attribute("checked")
            if ischecked =="true":
                return True,"元素已被选择"
            else:
                return False, "元素已被选择"
    else:
        raise Exception('元素%s对象获取失败'%(xpath_info))
def click_by_text(driver,name):
    '''
    通过id查找元素并点击
    '''
    get_target=appium_oper.find_ele_by_text_contains(driver,name)
    time.sleep(2)
    if get_target[0]:
        if type(get_target[1]) == str:
            raise Exception('元素%s对象获取失败'%(name))
        else:
            get_target[1].click()
            return True
    else:
        raise Exception('元素%s对象获取失败'%(name))
def swipe_and_find(driver,swipe_type=0,text=""):
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    if swipe_type==0:
        x1 = int(x*0.5)
        y1 = int(y*0.5)
        y2 = int(y*0.25)
        for i in range(30):
            driver.swipe(x1,y1,x1,y2,800)
def click_by_tap(driver,tap1,tap2):
    driver.tap([(int(tap1),int(tap2))])
def click_by_text_contains(driver, id_info):
    '''
    通过name查找元素并判断
    '''
    get_target=appium_oper.wait_eles_by_text_contains(driver,id_info,5)
    if get_target[0]:
        if type(get_target[1]) == str:
            raise Exception('元素%s对象获取失败'%(id_info))
        else:
            get_target[1][0].click()
    else:
        raise Exception('元素%s对象获取失败'%(id_info))

def check_by_id_fal(driver,id_info):
    '''
    通过id查找元素并判断
    '''
    get_target = appium_oper.wait_ele_by_id(driver, id_info)
    if get_target[0]:
        if type(get_target[1]) == str:
            return False
        else:
            return True
    else:
        return False

# coding=utf-8
def is_toast_exist(driver, text, timeout=5, poll_frequency=0.5):
    '''
	is toast exist, return True or False

    :Agrs:

    - driver - 传driver

    - text   - 页面上看到的文本内容

    - timeout - 最大超时时间，默认5s

    - poll_frequency  - 间隔查询时间，默认0.5s查询一次

   :Usage:

    is_toast_exist(driver, "看到的内容")

    '''
    try:
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
        WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
        return True
    except:
        return False