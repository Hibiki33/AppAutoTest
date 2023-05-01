from appium import webdriver
from selenium.webdriver.common.by import By
import time

class Driver:

    def __init__(self, desired_caps, host='127.0.0.1', port=4723):
        self.desired_caps = desired_caps
        self.driver = None
        self.host = host
        self.port = port
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        time.sleep(10)
        self.pass_privacy_protection()
        self.pass_adolescent_protection()

    def pass_adolescent_protection(self):
        try:
            iknow = self.driver.find_element(By.ID, ('text2'))
            if iknow:
                iknow = self.driver.find_element(By.ID, ('button'))
                print('Adolescent protect found!')
                iknow.click()
        except:
            print('Adolescent protect not found!')

    def pass_privacy_protection(self):
        try:
            self.driver.find_element(By.ID, ('agree')).click()
            print('Privacy protect found!')
        except:
            print('Privacy protect not found!')