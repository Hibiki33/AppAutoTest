from appium import webdriver
    
class Driver(object):
    def __init__(self):
        self.desired_caps = {}
        self.desired_caps["platformName"] = "Android"
        self.desired_caps["platformVersion"] = "9"
        self.desired_caps["deviceName"] = "emulator-5554 device"
        self.desired_caps["appPackage"] = "com.jingdong.app.mall"
        self.desired_caps["appActivity"] = ".MainFrameActivity"
        self.desired_caps["unicodeKeyboard"] = True
        self.desired_caps["resetKeyboard"] = True
        self.host = '127.0.0.1'
        self.port = 4723

    def getDriver(self):
        url = 'http://%s:%s/wd/hub' % (self.host, str(self.port))
        try:
            driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
            return driver
        except Exception as msg:
            print (msg)
            raise

if __name__ == '__main__':
    driver = Driver()
    d = driver.getDriver()