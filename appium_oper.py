'''
此接口针对Appium的相关调用进行封装，主要包括：
1.元素查找相关接口
2.模拟物理按键
3.屏幕坐标点击和滑动操作

作者：wangjiancheng
说明：首次完善基本方法
selenium==3.141
Appium-Python-Client==1.2.0
'''
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from appium.webdriver.common.touch_action import TouchAction


def find_ele_by_id(driver, id_info, alias=None):
    '''
    通过元素的id进行查找，此函数返回数组，0位bool值表示成功或失败，1位成功则表示找到的对象，失败则返回错误信息
    driver:连接Appium的对象
    id_info:输入元素的id信息
    alias:输入元素别名，这是为了当发生错误时可以返回别名信息减少错误后的定位难度
    return:元组，第1位为true时，第2位为结果，第1位为false，第2位为出错信息
    '''
    if alias is None:
        info = str(id_info)
    else:
        info = str(alias)
    try:
        el = driver.find_element_by_id(id_info)
        return True, el
    except NoSuchElementException:
        return False, "“" + info + "”此元素在当前界面未找到"
def wait_ele_by_id(driver, id_info, timeout=10, alias=None):
    '''
    等待元素的出现，此函数返回数组，0位bool值表示成功或失败，1位成功则表示找到的对象，失败则返回错误信息
    driver:连接Appium的对象
    id_info:输入元素的id信息
    timeout:超时时间（int型），当超过超时间仍未找到此元素则返回异常
    alias:输入元素别名，这是为了当发生错误时可以返回别名信息减少错误后的定位难度
    return:元组，第1位为true时，第2位为结果，第1位为false，第2位为出错信息
    '''
    if alias is None:
        info = id_info
    else:
        info = str(alias)

    try:
        WebDriverWait(driver, timeout).until(
            lambda x: x.find_element_by_id(id_info))
        el = driver.find_element_by_id(id_info)
        return True, el
    except (NoSuchElementException, TimeoutException):
        return False, "“" + info + "”到达超时时间后仍未找到此元素"
def find_ele_by_xpath(driver, xpath_info, alias=None):
    '''
    通过元素的xpath进行查找，此函数返回数组，0位bool值表示成功或失败，1位成功则表示找到的对象，失败则返回错误信息
    driver:连接Appium的对象
    xpath_info:输入元素的xpath信息
    alias:输入元素别名，这是为了当发生错误时可以返回别名信息减少错误后的定位难度
    return:元组，第1位为true时，第2位为结果，第1位为false，第2位为出错信息
    '''
    if alias is None:
        info = xpath_info
    else:
        info = str(alias)

    try:
        el = driver.find_element_by_xpath(xpath_info)
        return True, el
    except NoSuchElementException:
        return False, "“" + info + "”此元素在当前界面未找到"
def wait_ele_by_xpath(driver, xpath_info, timeout, alias=None):
    '''
    等待元素的出现，此函数返回数组，0位bool值表示成功或失败，1位成功则表示找到的对象，失败则返回错误信息
    driver:连接Appium的对象
    xpath_info:输入元素的id信息
    timeout:超时时间（int型），当超过超时间仍未找到此元素则返回异常
    alias:输入元素别名，这是为了当发生错误时可以返回别名信息减少错误后的定位难度
    return:元组，第1位为true时，第2位为结果，第1位为false，第2位为出错信息
    '''
    if alias is None:
        info = xpath_info
    else:
        info = str(alias)

    try:
        WebDriverWait(driver, timeout).until(
            lambda x: x.find_element_by_xpath(xpath_info))
        el = driver.find_element_by_xpath(xpath_info)
        return True, el
    except (NoSuchElementException, TimeoutException):
        return False, "“" + info + "”到达超时时间后仍未找到此元素"
def find_ele_by_name(driver, name):
    '''
    通过Name来定位元素，对于android来说，name就是text属性值。
    如果需要直接查找界面所有符合的控件时，可以直接使用find_eles_by_text_contains或find_eles_by_text方法（适用于android）
    driver：Appium连接对象
    name：需要定位的名称（text），string类型
    return:元组，第1位为true时，第2位为结果，第1位为false，第2位为出错信息
    '''
    try:
        find = driver.find_ele_by_name(name)
        return True, find
    except NoSuchElementException:
        return False, "名称为'%s'的元素未找到" % name
def find_eles_by_text(driver, text):
    '''
    通过指定的文字来定位控件，比如需要当前页面所有“格式化”文字的控件（完全匹配方式），返回的是列表，为空表示未找到相关元素
    driver:连接Appium的对象
    text:需要查找的文字，string类型
    return:元组，第1位为true时，第2位为结果，第1位为false，第2位为出错信息
    '''
    try:
        find_list = []
        find_list = driver.find_elements_by_android_uiautomator(
            'new UiSelector().text("%s")' % text)
        return True, find_list
    except NoSuchElementException:
        return False, "未找到完全匹配'%s'的元素" % text
def find_ele_by_text(driver, text):
    '''
    通过指定的文字来定位控件，比如需要当前页面所有“格式化”文字的控件（完全匹配方式），成功的话返回的是元素对象
    driver:连接Appium的对象
    text:需要查找的文字，string类型
    return:元组，第1位为true时，第2位为结果，第1位为false，第2位为出错信息
    '''
    try:
        find = driver.find_element_by_android_uiautomator(
            'new UiSelector().text("%s")' % text)
        return True, find
    except NoSuchElementException:
        return False, "未找到元素:%s" % text
def wait_eles_by_text(driver, text, timeout):
    '''
    等待元素的出现，此函数返回数组，0位bool值表示成功或失败，1位成功则表示找到的对象，失败则返回错误信息
    driver:连接Appium的对象
    text:输入需要查找的文本信息
    timeout:超时时间（int型），当超过超时间仍未找到此元素则返回异常
    return:元组，第1位为true时，第2位为结果，第1位为false，第2位为出错信息
    '''
    try:
        find_list = []
        WebDriverWait(driver, timeout).until(
            lambda x: x.find_elements_by_android_uiautomator('new UiSelector().text("%s")' % text))
        find_list = driver.find_elements_by_android_uiautomator(
            'new UiSelector().text("%s")' % text)
        return True, find_list
    except (NoSuchElementException, TimeoutException):
        return False, "“" + text + "”到达超时时间后仍未找到此元素"


def find_eles_by_text_contains(driver, text):
    '''
    通过指定的文字来定位控件，比如需要当前页面所有“格式化”文字的控件（模糊匹配方式，只要包含关键字即可），返回的是列表
    driver:连接Appium的对象
    text:需要查找的文字，string类型
    return:元组，第1位为true时，第2位为结果，第1位为false，第2位为出错信息
    '''
    try:
        find_list = []
        find_list = driver.find_elements_by_android_uiautomator(
            'new UiSelector().textContains("%s")' % text)
        if find_list == []:
            return False, "未找到包含'%s'的元素" % text
        else:
            return True, find_list
    except NoSuchElementException:
        return False, "未找到包含'%s'的元素" % text


def find_ele_by_text_contains(driver, text):
    '''
    通过指定的文字来定位控件，比如需要当前页面所有“格式化”文字的控件（模糊匹配方式，只要包含关键字即可），返回的单个元素
    driver:连接Appium的对象
    text:需要查找的文字，string类型
    return:元组，第1位为true时，第2位为结果，第1位为false，第2位为出错信息
    '''
    try:
        find = driver.find_element_by_android_uiautomator(
            'new UiSelector().textContains("%s")' % text)
        return True, find
    except NoSuchElementException:
        return False, "未找到包含'%s'的元素" % text


def wait_eles_by_text_contains(driver, text, timeout):
    '''
    等待元素的出现，此函数返回数组，0位bool值表示成功或失败，1位成功则表示找到的对象，失败则返回错误信息
    driver:连接Appium的对象
    text:输入需要查找的文本信息
    timeout:超时时间（int型），当超过超时间仍未找到此元素则返回异常
    return:元组，第1位为true时，第2位为结果，第1位为false，第2位为出错信息
    '''
    try:
        find_list = []
        WebDriverWait(driver, timeout).until(
            lambda x: x.find_elements_by_android_uiautomator('new UiSelector().textContains("%s")' % text))
        find_list = driver.find_elements_by_android_uiautomator(
            'new UiSelector().textContains("%s")' % text)
        return True, find_list
    except (NoSuchElementException, TimeoutException):
        return False, "“" + text + "”到达超时时间后仍未找到此元素"


def find_eles_by_class_name(driver, class_name):
    '''
    通过控件的类名来定位控件，返回符合条件的列表
    driver:连接Appium的对象
    class_name：控件类名，比如：android.widget.ImageView
    return:元组，第1位为true时，第2位为结果，第1位为false，第2位为出错信息
    '''
    try:
        find_list = []
        find_list = driver.find_elements_by_class_name(class_name)
        if find_list == []:
            return False, "未找到类名为'%s'的元素" % class_name
        else:
            return True, find_list
    except NoSuchElementException:
        return False, "未找到类名为'%s'的元素" % class_name


def find_ele_by_class_name(driver, class_name):
    '''
    通过控件的类名来定位控件，返回符合条件的单个对象
    driver:连接Appium的对象
    class_name：控件类名，比如：android.widget.ImageView
    return:元组，第1位为true时，第2位为结果，第1位为false，第2位为出错信息
    '''
    try:
        find = driver.find_element_by_class_name(class_name)
        return True, find
    except NoSuchElementException:
        return False, "未找到类名为'%s'的元素" % class_name


def wait_eles_by_class_name(driver, class_name, timeout):
    '''
    等待元素的出现，此函数返回数组，0位bool值表示成功或失败，1位成功则表示找到的对象，失败则返回错误信息
    driver:连接Appium的对象
    text:输入需要查找的文本信息
    timeout:超时时间（int型），当超过超时间仍未找到此元素则返回异常
    return:元组，第1位为true时，第2位为结果，第1位为false，第2位为出错信息
    '''
    try:
        find_list = []
        WebDriverWait(driver, timeout).until(
            lambda x: x.find_element_by_class_name(class_name))
        find_list = driver.find_element_by_class_name(class_name)
        return True, find_list
    except (NoSuchElementException, TimeoutException):
        return False, "“" + class_name + "”到达超时时间后仍未找到此元素"


def find_eles_by_resourceID(driver, ID_name):
    '''
    通过指定的ResourceID来定位控件，搜索成功时结果为列表
    driver:连接Appium的对象
    ID_name:需要查找的resourceID,如：com.hikistor.histor:id/iv_image
    return:元组，第1位为true时，第2位为结果，第1位为false，第2位为出错信息
    '''
    try:
        find_list = []
        find_list = driver.find_elements_by_android_uiautomator(
            'new UiSelector().resourceId("%s")' % ID_name)
        if find_list == []:
            return False, "未找到包含'%s'的元素" % ID_name
        else:
            return True, find_list
    except NoSuchElementException:
        return False, "未找到包含'%s'的元素" % ID_name


def wait_eles_by_resourceID(driver, ID_name, timeout):
    '''
    等待元素的出现，此函数返回数组，0位bool值表示成功或失败，1位成功则表示找到的对象，失败则返回错误信息
    driver:连接Appium的对象
    ID_name:输入需要查找的id
    timeout:超时时间（int型），当超过超时间仍未找到此元素则返回异常
    return:元组，第1位为true时，第2位为结果，第1位为false，第2位为出错信息
    '''
    try:
        find_list = []
        WebDriverWait(driver, timeout).until(
            lambda x: x.find_elements_by_android_uiautomator('new UiSelector().resourceId("%s")' % ID_name))
        find_list = driver.find_elements_by_android_uiautomator(
            'new UiSelector().resourceId("%s")' % ID_name)
        return True, find_list
    except (NoSuchElementException, TimeoutException):
        return False, "“" + ID_name + "”到达超时时间后仍未找到此元素"


def key_press(driver, key_code):
    '''
    操作手机硬件
    driver:连接Appium的对象
    key_code:硬件码，int型。常用硬件码如下
    拨号键：5
    挂机键：6
    Home键：3
    菜单键：82
    返回键：4
    电源键：26
    音量+：24
    音量-：25
    '''
    driver.keyevent(key_code)


def long_press(driver, ele_object, duration=2000):
    '''
    长按操作，默认时间长按2秒
    driver:appium连接对象
    ele_object:控件对象
    duration:默认2000毫秒，长按的时长
    '''
    TouchAction(driver).long_press(ele_object, duration=duration).perform()


def send_keys(ele_object, key_info):
    '''向输入框输入信息
    ele_object:获取到的控件对象
    key_info:需要输入的信息'''
    ele_object.send_keys(key_info)


def swipe_common(driver, swipe_type, start_loct=1, speed=1500):
    '''
    滑动屏幕操作，此操作支持向上、下、左、右4个方向滑动，滑动距离约为3/4屏的距离
    *注意：如果要在屏幕内精确的位置滑动，可以直接调用webdriver中的swipe方法
    driver:连接APP的对象
    swipe_type:滑动的方向（整型），约定0:向上，1:向下，2:向右，3:向左
    start_loct:起始位置标定。默认为1
    speed:滑动的速度(毫秒)，默认为1500，数值越大，滑动速度越慢
    '''
    screen_size = driver.get_window_size()
    x = screen_size['width']
    y = screen_size['height']

    if swipe_type == 0:  # 向上滑动
        x1 = int(x * 0.5)
        y1 = int(y * 0.85 * start_loct)
        # y2 = int(y * 0.15)
        y2 = int(y * 0.45)
        driver.swipe(x1, y1, x1, y2, speed)
    elif swipe_type == 1:  # 向下滑动
        x1 = int(x * 0.5)
        y1 = int(y * 0.2 * start_loct)
        y2 = int(y * 0.85)
        driver.swipe(x1, y1, x1, y2, speed)
    elif swipe_type == 2:  # 向右滑动
        x1 = int(x * 0.05 * start_loct)
        y1 = int(y * 0.5)
        x2 = int(y * 0.8)
        driver.swipe(x1, y1, x2, y1, speed)
    else:  # 向左滑动
        x1 = int(x * 0.8 * start_loct)
        y1 = int(y * 0.5)
        x2 = int(y * 0.05)
        driver.swipe(x1, y1, x2, y1, speed)
