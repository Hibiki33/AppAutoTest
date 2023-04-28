from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.by import By
    
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
        self.driver.implicitly_wait(20) # wait for app to start


    def pass_adolescent_protection(self):
        try:
            iknow = self.driver.find_element_by_id('text3')
            if iknow:
                print('Adolescent protect found!')
                iknow.click()
        except:
            print('Adolescent protect not found!')
    
    def search(self, keyword):
        self.driver.find_element(By.ID, ('expand_search')).click()
        sbox = driver.find_element(By.ID, ('search_src_text'))
        sbox.send_keys(keyword)
        driver.press_keycode(AndroidKey.ENTER)
        titles = driver.find_elements(By.ID, 'title')
        return titles



if __name__ == '__main__':
    bili = BiliOperator()
    results = str(bili.search("idol")) + str(bili.search("yoasobi"))
    print(results)
    