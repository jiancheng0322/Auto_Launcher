import os
import time

"""
   遥控器操作 up, down, left, right, back, backhome, ok

   """


def remotecontrol(send):
    if send == 'up':
        # up
        time.sleep(1)
        os.system('adb shell input keyevent 19')
        return send

    if send == 'down':
        # down
        time.sleep(1)
        os.system('adb shell input keyevent 20')
        return send

    if send == 'left':
        # left
        time.sleep(1)
        os.system('adb shell input keyevent 21')
        return send

    if send == 'right':
        # right
        time.sleep(1)
        os.system('adb shell input keyevent 22')
        return send

    if send == 'ok':
        # ok
        time.sleep(1)
        os.system('adb shell input keyevent 23')
        return send

    if send == 'back':
        # back
        time.sleep(1)
        os.system('adb shell input keyevent BACK')
        return send

    if send == "menu":
        time.sleep(1)
        os.system('adb shell input keyevent 82')
        return send

    if send == 'backhome':
        # backhome 返回首页
        time.sleep(1)
        os.system('com.dangbei.leard.leradlauncher/.ui.splash.SplashActivity')
        return send

    if send == 'screenshots':
        # screenshots 截图
        time.sleep(1)
        os.system('adb shell screencap -p /sdcard/01.png')
        os.system('adb pull /sdcard/01.png')
        return send

    else:
        pass


def lianxu(send, i):
    for content in range(0, i):
        remotecontrol(send)
