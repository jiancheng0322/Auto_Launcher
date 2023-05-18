'''
模块名称：公共方法
方法列表：
1.

作者：wangjiancheng
版本记录：
'''
import appium_oper
from appium import webdriver
import time
import basic_oper
import re


def longpress(self):
        '''
        长按选中
        '''
def copy_to_other_place(driver,conf_get_mapId,path,strategy):
        '''
        复制到指定地方：目前地方仅限共享空间与硬盘根目录
        :param driver:
        :param path:目的路径：0：共享空间；1：硬盘根目录
        :param strategy:复制策略：0：跳过；1：替换；2：保留两者
        :return:
        '''
        listpath = [0,1]
        liststrategy = [0,1,2]
        try:
            if path not in listpath:
                raise Exception('输入path参数错误')
        finally:
            pass
        try:
            if  strategy not in liststrategy :
                raise  Exception('输入复制策略参数错误')
        finally:
            pass
        basic_oper.click_by_id(driver,conf_get_mapId["tvCopy3"])
        if(path==0):
            time.sleep(1)
            basic_oper.click_by_tap(driver,conf_get_mapId["共享空间X"],conf_get_mapId["共享空间Y"])
            time.sleep(1)
            basic_oper.click_by_id(driver, conf_get_mapId["btn_upload"])
            time.sleep(1)
            if(strategy==0):
                basic_oper.click_by_text(driver,"跳过")
            elif(strategy==1):
                basic_oper.click_by_text(driver, "替换")
            else:
                basic_oper.click_by_text(driver,"保留两者")
        else:
            basic_oper.click_by_tap(driver, conf_get_mapId["硬盘X"], conf_get_mapId["硬盘Y"])
            time.sleep(1)
            basic_oper.click_by_id(driver, conf_get_mapId["btn_upload"])
            time.sleep(1)
            if (strategy == 0):
                basic_oper.click_by_text(driver,"跳过")
            elif (strategy == 1):
                basic_oper.click_by_text(driver,"替换")
            else:
                basic_oper.click_by_text(driver,"保留两者")
def move_to_other_place(driver,conf_get_mapId,path,strategy):
        '''
        移动到指定地方：目前地方仅限共享空间与硬盘根目录
        :param driver:
        :param path:目的路径：0：共享空间；1：硬盘根目录
        :param strategy:复制策略：0：跳过；1：替换；2：保留两者
        :return:
        '''
        listpath = [0,1]
        liststrategy = [0,1,2]
        try:
            if path not in listpath:
                raise Exception('输入path参数错误')
        finally:
            pass
        try:
            if  strategy not in liststrategy :
                raise  Exception('输入复制策略参数错误')
        finally:
            pass
        basic_oper.click_by_id(driver,conf_get_mapId["tvMove3"])
        time.sleep(1)
        if(path==0):
            basic_oper.click_by_tap(driver, conf_get_mapId["共享空间X"], conf_get_mapId["共享空间Y"])
            time.sleep(1)
            basic_oper.click_by_id(driver, conf_get_mapId["btn_upload"])
            time.sleep(1)
            if(strategy==0):
                basic_oper.click_by_text(driver,"跳过")
            elif(strategy==1):
                basic_oper.click_by_text(driver, "替换")
            else:
                basic_oper.click_by_text(driver,"保留两者")
        else:
            basic_oper.click_by_tap(driver, conf_get_mapId["硬盘X"], conf_get_mapId["硬盘Y"])
            time.sleep(1)
            basic_oper.click_by_id(driver, conf_get_mapId["btn_upload"])
            time.sleep(1)
            if (strategy == 0):
                basic_oper.click_by_text(driver,"跳过")
            elif (strategy == 1):
                basic_oper.click_by_text(driver, "替换")
            else:
                basic_oper.click_by_text(driver, "保留两者")
def longpress_delete(driver, ele_object, conf_get_mapId):
        '''
        列表长按选中-删除
        '''
        appium_oper.long_press(driver, ele_object)
        basic_oper.click_by_id(driver, conf_get_mapId["tvDelete3"])
        basic_oper.click_by_id(driver, conf_get_mapId["positiveButton"])
def all_select(driver):
        '''
        列表（图片分类不使用；大于2个文件）全选：choiceid：选择圆点
                  selectallid：全选按钮
        '''
        basic_oper.click_by_id(driver, "com.hikistor.histor:id/imgMoreOperate")
        basic_oper.click_by_id(driver, "com.hikistor.histor:id/selectall")
def all_select_picture(driver,ele_object,conf_get_mapId):
    '''
    列表（图片分类不使用；大于2个文件）全选：choiceid：选择圆点
              selectallid：全选按钮
    '''
    appium_oper.long_press(driver,ele_object)
    basic_oper.click_by_id(driver, conf_get_mapId["select_all"])
def get_choice_num(driver, id_info):
        '''
        获取已选择数量
        :param id_info: 顶部已选择元素
        :return:
        '''
        get_target = appium_oper.wait_ele_by_id(driver, id_info)
        if get_target[0]:
            if type(get_target[1]) == str:
                raise Exception('元素%s对象获取失败' % (id_info))
            else:
                repstr = get_target[1].text
                count = re.findall("已选择(\([^\)]+\))", repstr)
                num = str(count[0])
                return True, int(num[1:-1])
        else:
            print(get_target[1])
            raise Exception('元素%s对象获取失败' % (id_info))
def search_file(driver, searchlist):
        '''
        内部方法：滑屏寻找对应文件，到底部或者最多滑屏30次未找到则断言失败
        searchlist为数组
        '''

        for i in range(30):
            lenth = len(searchlist)
            m = 0
            while m < lenth:
                filesearching = appium_oper.find_ele_by_text_contains(driver, searchlist[m])
                if (filesearching[0]):
                    searchfile = filesearching
                    return searchfile
                else:
                    m = m + 1

            llFooterView = appium_oper.find_ele_by_id(driver, "com.hikistor.histor:id/llFooterView", "底部文案")
            if (llFooterView[0]):
                return False, "已到页面底部"
            else:
                appium_oper.swipe_common(driver, 0)  # 根据手机分辩率大小，可能需要向上滑屏才能看到
            if i == 10:
                return False, "滑屏30次后仍未找到对应文件"
def type_text_by_id(driver,conf_get_mapId, editid, text):
        '''
        针对弹框的输入文字
        '''
        get_target = appium_oper.wait_ele_by_id(driver, editid)  # 寻找所选输入框
        if get_target[0]:
            if type(get_target[1]) == str:
                raise Exception('元素%s对象获取失败' % (editid))
            else:
                get_target[1].click()
                get_target[1].clear()
                get_target[1].send_keys(text)
                basic_oper.click_by_id(driver,conf_get_mapId["positiveButton"] )  # 确定按钮
        else:
            print(get_target[1])
            raise Exception('元素%s对象获取失败' % (editid))
def type_text_by_id_notframe(driver, editid, text):
    '''
    针对非弹框的输入文字
    '''
    get_target = appium_oper.wait_ele_by_id(driver, editid)  # 寻找所选输入框
    if get_target[0]:
        if type(get_target[1]) == str:
            raise Exception('元素%s对象获取失败' % (editid))
        else:
            get_target[1].click()
            get_target[1].clear()
            get_target[1].send_keys(text)
    else:
        print(get_target[1])
        raise Exception('元素%s对象获取失败' % (editid))
def createfolder(driver,conf_get_mapId,foldername):
    '''
    该方法用来新建文件夹
    '''
    basic_oper.click_by_id(driver, conf_get_mapId["doc_animate"])  # 点击文件tab
    all_select(driver, conf_get_mapId)  # 全选
    resultbefor = get_choice_num(driver, conf_get_mapId["selectcount"])  # 判断当前界面文件数量
    basic_oper.click_by_id(driver, conf_get_mapId["cancel"])  # 取消全选
    basic_oper.click_by_xpath(driver, conf_get_mapId["upload"])  # 点击上传
    basic_oper.click_by_id(driver, conf_get_mapId["choose_create"])  # 点击新建文件夹
    type_text_by_id(driver, conf_get_mapId["edit"], conf_get_mapId["positiveButton"], foldername)
    basic_oper.click_by_id(driver, conf_get_mapId["back"])
    all_select(driver, conf_get_mapId)  # 全选
    resultafter = get_choice_num(driver, conf_get_mapId["selectcount"])
    assert int(resultbefor[1]) == int(resultafter[1]) - 1, "新建文件夹失败"
    basic_oper.click_by_id(driver, conf_get_mapId["cancel"])  # 取消全选
def detail(driver,conf_get_mapId,type):
    '''
    内部方法：查看详细信息及详情；
    :type:1:图片;2.其他格式;3.文件夹
    '''
    attribute1 = appium_oper.wait_eles_by_text(driver, "查看详细信息", 5)
    attribute2 = appium_oper.wait_eles_by_text(driver, "重命名", 5)
    attribute3 = appium_oper.wait_eles_by_text(driver, "取消", 5)
    assert attribute1[0] and attribute2[0] and attribute3[0],"选项有误"
    if(type==1):
        attribute5 = appium_oper.wait_eles_by_text(driver, "添加到相簿", 5)
        attribute6 = appium_oper.wait_eles_by_text(driver, "分享", 5)
        assert attribute5[0] and attribute6[0],"选项有误"
    if(type == 2):
        attribute6 = appium_oper.wait_eles_by_text(driver, "分享", 5)
        assert attribute6[0], "选项有误"
    if(type == 3):
            attribute5 = appium_oper.find_ele_by_text_contains(driver, "创建快捷文件夹")
            assert attribute5[0], "没有创建快捷文件夹按钮"
    print("点击查看详情信息")
    attribute1[1][0].click()
    if(type == 3):
        basic_oper.check_by_id(driver, conf_get_mapId["tv_files_count"])

    basic_oper.check_by_id(driver, conf_get_mapId["tv_name"])
    basic_oper.check_by_id(driver, conf_get_mapId["tv_size"])
    basic_oper.check_by_id(driver, conf_get_mapId["tv_file_type"])
    basic_oper.check_by_id(driver, conf_get_mapId["tv_path"])
    basic_oper.check_by_id(driver, conf_get_mapId["tv_date"])
    print("关闭详情信息页面")
    basic_oper.click_by_id(driver, conf_get_mapId["iv_close"])
def editandmore(driver,conf_get_mapId,button):
    '''
     内部方法：点击进入编辑模式以及点击更多按钮，button为传入想要查看的元素
    '''
    print("点击进入编辑模式")
    appium_oper.long_press(driver, button[1], 3000)
    choose = appium_oper.wait_eles_by_text_contains(driver, "已选择", 5)
    assert choose[0], "未进入编辑模式"
    basic_oper.click_by_id(driver, conf_get_mapId["tvMore3"])
def gettext(driver,button):
    '''
    获取text
    :param driver:
    :param button:
    :return:
    '''
    tvTitle = appium_oper.wait_ele_by_xpath(driver,button, 5)
    title = tvTitle[1].text
    return title
def longpress_download(driver, type, where, ele_object):
    '''
    长按选中-下载（单选）
    type:1:id;2.xpath
    where:1:图片分类及文件列表中图片;2:视频/音乐/文档/文件列表
    '''
    if (type == 1):
        get_target = appium_oper.wait_ele_by_id(driver, ele_object)
        if (get_target[0]):
            appium_oper.long_press(driver, get_target[1])
        else:
            return False
    elif (type == 2):
        get_target = appium_oper.wait_ele_by_xpath(driver, ele_object, 5)
        if (get_target[0]):
            appium_oper.long_press(driver, get_target[1])
        else:
            return False
    else:
        return False
    if(where==1):
        basic_oper.click_by_id(driver, "com.hikistor.histor:id/tvDownload2")
    elif(where==2):
        basic_oper.click_by_id(driver,"com.hikistor.histor:id/tvDownLoad3")
    else:
        return False

def enter_picture(driver):
    basic_oper.click_by_id(driver, "com.hikistor.histor:id/doc_animate")
    basic_oper.click_by_id(driver, "com.hikistor.histor:id/category_entrance")
    basic_oper.click_by_id(driver, "com.hikistor.histor:id/img")

def enter_video(driver,conf_get_mapId):
    basic_oper.click_by_id(driver, conf_get_mapId["doc_animate"])
    basic_oper.click_by_id(driver, conf_get_mapId["category_entrance"])
    basic_oper.click_by_id(driver, conf_get_mapId["video"])

def enter_music(driver):
    basic_oper.click_by_id(driver, "com.hikistor.histor:id/doc_animate")
    basic_oper.click_by_id(driver, "com.hikistor.histor:id/category_entrance")
    basic_oper.click_by_id(driver, "com.hikistor.histor:id/music")

def enter_document(driver,conf_get_mapId):
    basic_oper.click_by_id(driver, conf_get_mapId["doc_animate"])
    basic_oper.click_by_id(driver, conf_get_mapId["category_entrance"])
    basic_oper.click_by_id(driver, conf_get_mapId["doc"])

def conf_get_mapId():
    book = xlrd.open_workbook("..\\excel\\mapid.xlsx")
    table = book.sheet_by_name("元素对应表")
    mapdict = {}
    row_Num = table.nrows
    col_Num = table.ncols
    if row_Num <= 1 or col_Num < 0:
        print("没有数据")
    else:
        firstcol = table.col_values(0)[1:]
        secondcol = table.col_values(1)[1:]
        for i in range(row_Num - 1):
            mapdict[firstcol[i]] = secondcol[i]
    return mapdict