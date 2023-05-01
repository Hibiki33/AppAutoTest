from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os
import _thread
import time
    
class BiliOperator(object):
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
        time.sleep(10) # wait for app to start
        self.pass_adolescent_protection()

    def pass_adolescent_protection(self):
        try:
            iknow = self.driver.find_element_by_id('text2')
            if iknow:
                iknow = self.driver.find_element_by_id('button')
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
        descs = []
        for keyword in keywords:
            print("Searching for " + keyword + "...")
            sbox = self.driver.find_element(By.ID, ('search_src_text'))
            sbox.send_keys(keyword)
            time.sleep(1)
            self.driver.press_keycode(AndroidKey.ENTER)
            time.sleep(3)
            eles = self.wait(lambda d: d.find_elements(By.ID, 'title'), 10)
            for ele in eles:
                titles.append(ele.text)
            # time.sleep(15)
            # self.driver.find_element(By.ID, ('title')).click()
            ele = self.wait(lambda d: d.find_element(By.ID, 'title'), 3)
            ele.click()
            # time.sleep(3)
            # self.driver.find_element(By.ID, ('frame_recommend')).click()
            ele = self.wait(lambda d: d.find_element(By.ID, ('frame_recommend')), 1)
            ele.click()
            time.sleep(1)
            # self.driver.find_element(By.ID, ('tab_sub_title')).click()
            ele = self.wait(lambda d: d.find_element(By.ID, ('tab_sub_title')), 1)
            ele.click()
            time.sleep(1)
            desctext = self.driver.find_elements(By.CLASS_NAME, ('android.widget.TextView'))
            foundcmt = False
            for desc in desctext:
                if not foundcmt:
                    if ":" in desc.text:
                        foundcmt = True
                    else:
                        continue
                if len(desc.text) < 5:
                    continue
                descs.append(desc.text)
            time.sleep(3)
            self.driver.press_keycode(AndroidKey.BACK)
            time.sleep(1)
            self.driver.press_keycode(AndroidKey.BACK)
            time.sleep(1)
        self.quit_search()
        return titles, descs
    
    def access_buy(self):
        print("Accessing buy page...")
        eles = self.driver.find_elements(By.CLASS_NAME, ('android.widget.TextView'))
        eles[-2].click()
        time.sleep(10)
        print(eles[-2].text)

    def quit_buy(self):
        print("Quitting buy page...")
        self.driver.press_keycode(AndroidKey.BACK)
        time.sleep(1)

    def search_buy(self, keywords):
        self.access_buy()
        self.access_search('mall_home_search_v2_layout')
        titles = []
        for keyword in keywords:
            print("Searching for " + keyword + "...")
            sbox = self.driver.find_element(By.ID, ('search_edit'))
            sbox.send_keys(keyword)
            time.sleep(6)
            # self.driver.press_keycode(AndroidKey.ENTER)
            self.driver.find_element(By.ID, ('mall_id_search_page_actionbar_commit')).click()
            time.sleep(10)
            # self.driver.press_keycode(AndroidKey.BACK)
            # time.sleep(1)
            # sbox = self.driver.find_element(By.ID, ('search_edit'))
            # sbox.send_keys(keyword)
            # time.sleep(6)
            # self.driver.find_element(By.ID, ('mall_id_search_page_actionbar_commit')).click()
            # time.sleep(6)
            # text_contains = 'new UiSelector().textContains("png")'
            # self.driver.find_elements(By.android_uiautomator(text_contains)).click()
            self.driver.find_elements(By.CLASS_NAME, ('android.webkit.WebView'))
            time.sleep(10)
            eles = self.driver.find_elements(By.CLASS_NAME, ('android.widget.Image'))
            eles[4].click()
            # eles = self.driver.find_elements(By.CLASS_NAME, ('android.widget.TextView'))
            # passing = True
            # for ele in eles:
            #     if keyword in ele.text:
            #         if passing:
            #             passing = False
            #             continue
            #         ele.click()
            #         break
            # eles[-1].click()
            time.sleep(8)
            # eles = self.driver.find_elements(By.CLASS_NAME, ('android.view.View'))
            eles = self.wait(lambda d: d.find_elements(By.CLASS_NAME, ('android.view.View')), 10)
            for ele in eles:
                if u"购物车" in ele.text:
                    ele.click()
                    break
            time.sleep(5)
            self.driver.press_keycode(AndroidKey.BACK)
            time.sleep(1)
            self.driver.press_keycode(AndroidKey.BACK)
            time.sleep(1)
        self.quit_search()
        self.quit_buy()
        return titles
    
    def wait(self, func, time=10):
        res = WebDriverWait(self.driver, timeout=time).until(func)
        return res

class RunAppium():
    def __init__(self):
        _thread.start_new_thread(self.run_appium, ())
        time.sleep(15)
    
    def run_appium(self):
        os.system('adb kill-server')
        os.system('appium -a localhost -p 4723')


if __name__ == '__main__':
    f = open('log.txt', 'w', encoding='utf-8')
    ra = RunAppium()
    bili = BiliOperator()
    # results = bili.search_video(["china daily", "spaceX"])
    # print(str(results[0]))
    # print(str(results[1]))
    # f.write(results)
    bili.access_buy()
    # results = str(bili.search_buy(["bakuen", "konosuba"]))
    # f.writelines(results)
    