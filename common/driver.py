from appium import webdriver

class Driver:

    def __init__(self, desired_caps, host='127.0.0.1', port=4723):
        self.desired_caps = desired_caps
        self.driver = None
        self.host = host
        self.port = port
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)