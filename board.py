import os
import time

"""
   遥控器操作 up, down, left, right, back, backhome, ok
   
   """


def remotecontrol(send):
    if send == 'up':
        # up
        os.system('adb shell input keyevent 19')

    if send == 'down':
        # down
        os.system('adb shell input keyevent 20')

    if send == 'left':
        # left
        os.system('adb shell input keyevent 21')

    if send == 'right':
        # right
        os.system('adb shell input keyevent 22')

    if send == 'ok':
        # ok
        os.system('adb shell input keyevent 23')

    if send == 'back':
        # back
        os.system('adb shell input keyevent BACK')
    if send == "menu":
        os.system('adb shell input keyevent 82')

    if send == 'backhome':
        # backhome 返回首页
        os.system('com.dangbei.leard.leradlauncher/.ui.splash.SplashActivity')


    if send == 'screenshots':
        # screenshots 截图
        os.system('adb shell screencap -p /sdcard/01.png')
        os.system('adb pull /sdcard/01.png')

    if send == 'left2':
        # left2 执行两次
        os.system('adb shell input keyevent 21')
        os.system('adb shell input keyevent 21')

    if send == 'right4':
        os.system('adb shell input keyevent 22')
        time.sleep(1)
        os.system('adb shell input keyevent 22')
        time.sleep(1)
        os.system('adb shell input keyevent 22')
        time.sleep(1)
        os.system('adb shell input keyevent 22')

    if send == 'down10':
        # down
        os.system('adb shell input keyevent 20')
        time.sleep(1)
        os.system('adb shell input keyevent 20')
        time.sleep(1)
        os.system('adb shell input keyevent 20')
        time.sleep(1)
        os.system('adb shell input keyevent 20')
        time.sleep(1)
        os.system('adb shell input keyevent 20')
        time.sleep(1)
        os.system('adb shell input keyevent 20')
        time.sleep(1)
        os.system('adb shell input keyevent 20')
        time.sleep(1)
        os.system('adb shell input keyevent 20')
        time.sleep(1)
        os.system('adb shell input keyevent 20')
        time.sleep(1)
        os.system('adb shell input keyevent 20')
        time.sleep(1)
        os.system('adb shell input keyevent 20')
        time.sleep(1)
        os.system('adb shell input keyevent 20')
        time.sleep(1)

    else:
        pass
