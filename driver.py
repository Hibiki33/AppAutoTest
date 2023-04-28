from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.by import By

import os
import _thread
import time
    
class BiliOperator():
    def __init__(self):
        self.desired_caps = {}
        self.desired_caps["platformName"] = "Android"
        self.desired_caps["platformVersion"] = "9"
        self.desired_caps["deviceName"] = "emulator-5554 device"
        self.desired_caps["appPackage"] = "tv.danmaku.bili"
        self.desired_caps["appActivity"] = "tv.danmaku.bili.MainActivityV2"
        self.desired_caps["unicodeKeyboard"] = True
        self.desired_caps["resetKeyboard"] = True
        self.desired_caps["noReset"] = True
        self.desired_caps["newCommandTimeout"] = 100000
        self.host = '127.0.0.1'
        self.port = 4723
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        time.sleep(1) # wait for app to start
        self.pass_adolescent_protection()

    def pass_adolescent_protection(self):
        try:
            iknow = self.driver.find_element_by_id('text3')
            if iknow:
                print('Adolescent protect found!')
                iknow.click()
        except:
            print('Adolescent protect not found!')

    def access_search(self, search_frame_id):
        print("Accessing search page...")
        self.driver.find_element(By.ID, (search_frame_id)).click()
        time.sleep(2)
    
    def quit_search(self):
        print("Quitting search page...")
        self.driver.press_keycode(AndroidKey.BACK)
        time.sleep(1)
    
    def search_video(self, keywords):
        self.access_search('expand_search')
        titles = []
        for keyword in keywords:
            print("Searching for " + keyword + "...")
            sbox = self.driver.find_element(By.ID, ('search_src_text'))
            sbox.send_keys(keyword)
            self.driver.press_keycode(AndroidKey.ENTER)
            titles.append(self.driver.find_elements(By.ID, 'title'))
            time.sleep(15)
            self.driver.press_keycode(AndroidKey.BACK)
        self.quit_search()
        return titles
    
    def access_buy(self):
        print("Accessing buy page...")
        self.driver.find_element(By.XPATH, ('4,')).click()
        time.sleep(2)

    def quit_buy(self):
        print("Quitting buy page...")
        self.driver.press_keycode(AndroidKey.BACK)
        time.sleep(1)

    def search_buy(self, keywords):
        self.access_buy()
        self.access_search('mall_home_search_v2')
        titles = []
        for keyword in keywords:
            print("Searching for " + keyword + "...")
            sbox = self.driver.find_element(By.ID, ('search_edit'))
            sbox.send_keys(keyword)
            self.driver.press_keycode(AndroidKey.ENTER)
            titles.append(self.driver.find_elements(By.ID, 'title'))
            time.sleep(15)
            self.driver.press_keycode(AndroidKey.BACK)
        self.quit_search()
        self.quit_buy()
        return titles


class RunAppium():
    def __init__(self):
        _thread.start_new_thread(self.run_appium, ())
        time.sleep(15)
    
    def run_appium(self):
        os.system('adb kill-server')
        os.system('appium -a localhost -p 4723')

if __name__ == '__main__':
    f = open('log.txt', 'w')
    ra = RunAppium()
    bili = BiliOperator()
    results = str(bili.search_video(["china", "USA", "Russia"]))
    f.writelines(results)
    bili.access_buy()
    results = str(bili.search_buy(["bakuen", "konosuba"]))
    f.writelines(results)
    