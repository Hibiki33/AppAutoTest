from appium import webdriver
import time

class Driver:

    def __init__(self, desired_caps, host='127.0.0.1', port=4723):
        self.desired_caps = desired_caps
        self.driver = None
        self.host = host
        self.port = port
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        time.sleep(5)
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