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
        self.driver.implicitly_wait(20) # wait for app to start
        self.pass_adolescent_protection()

    def pass_adolescent_protection(self):
        try:
            iknow = self.driver.find_element_by_id('text3')
            if iknow:
                print('Adolescent protect found!')
                iknow.click()
        except:
            print('Adolescent protect not found!')
    
    def search_video(self, keyword):
        self.driver.press_keycode(AndroidKey.BACK)
        self.driver.find_element(By.ID, ('expand_search')).click()
        sbox = self.driver.find_element(By.ID, ('search_src_text'))
        sbox.send_keys(keyword)
        self.driver.press_keycode(AndroidKey.ENTER)
        titles = self.driver.find_elements(By.ID, 'title')
        return titles
    
    def access_buy(self):
        self.driver.find_element(By.XPATH, ('会员购')).click()

    def search_buy(self, keyword):
        self.driver.press_keycode(AndroidKey.BACK)
        self.driver.find_element(By.ID, ('mall_home_search_v2')).click()
        sbox = self.driver.find_element(By.ID, ('search_edit'))
        sbox.send_keys(keyword)
        self.driver.press_keycode(AndroidKey.ENTER)
        titles = self.driver.find_elements(By.ID, 'title')
        return titles


class RunAppium():
    def __init__(self):
        _thread.start_new_thread(self.run_appium, ())
        time.sleep(15)
    
    def run_appium(self):
        os.system('adb kill-server')
        os.system('appium -a localhost -p 4723')

if __name__ == '__main__':
    ra = RunAppium()
    bili = BiliOperator()
    results = str(bili.search_video("idol")) + str(bili.search_video("yoasobi"))
    print(results)
    bili.access_buy()
    results = str(bili.search_buy("会员")) + str(bili.search_buy("年度"))
    print(results)
    