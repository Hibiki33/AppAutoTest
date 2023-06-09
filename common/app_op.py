from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

class AppOp :

    def __init__(self, op_dict):
        self.op_dict = op_dict
        if op_dict['op'] == 'none':
            self.op = 'skip'
        if ('op' not in op_dict) or ('wait_time' not in op_dict):
            raise Exception('AppOp init failed need at least op and wait_time')
        for key in op_dict:
            setattr(self, key, op_dict[key])
        by_dict = {'id': By.ID, 'xpath': By.XPATH, 'class_name': By.CLASS_NAME}
        if 'type' in op_dict:
            if self.type not in by_dict:
                raise Exception('AppOp init failed type not in id, xpath, class_name')
            self.by = by_dict[self.type]

    def __call__(self, driver, keyword=None):
        func_dict = {'get_texts': self.get_texts, 'try_click': self.try_click, 'skip': self.skip, 'back': self.back, 'enter': self.enter, 'click': self.click, 'send_keys': self.send_keys, 'find': self.find, 'find_cart_and_click': self.find_cart_and_click}
        if self.op not in func_dict:
            raise Exception('AppOp run failed op not in skip, back, enter, click, send_keys, find, find_cart_and_click')
        if self.op == 'send_keys':
            if keyword is None:
                raise Exception('AppOp run failed op is send_keys but keyword is None')
            return func_dict[self.op](driver, keyword)
        else:
            return func_dict[self.op](driver)
    
    def try_click(self, driver):
        try:
            self.click(driver)
        except:
            pass
        return 0

    def skip(self, driver):
        time.sleep(self.wait_time)
        return 0
    
    def back(self, driver):
        driver.press_keycode(AndroidKey.BACK)
        time.sleep(self.wait_time)
        return 0
    
    def enter(self, driver):
        driver.press_keycode(AndroidKey.ENTER)
        time.sleep(self.wait_time)
        return 0

    def click(self, driver):
        r = self.get_element(driver, click=True)
        return r
    
    def send_keys(self, driver, keyword):
        try:
            self.get_element(driver).send_keys(keyword)
        except:
            return -1
        time.sleep(self.wait_time)
        return 0
    
    def find(self, driver):
        try:
            self.get_element(driver)
            time.sleep(self.wait_time)
            return 0
        except:
            return -1

    def get_texts(self, driver):
        res = []
        try:
            res += [ele.text for ele in self.get_elements(driver)]
        except:
            pass
        time.sleep(self.wait_time)
        return res
    
    def find_cart_and_click(self, driver):
        eles = self.get_elements(driver)
        try:
            for ele in eles:
                if u'购物车' in ele.text:
                    ele.click()
                    time.sleep(self.wait_time)
                    return 0
        except:
            return -1

    def get_element(self, driver, click=False):
        try:
            if click:
                if 'index' in self.op_dict:
                    self.wait(driver, lambda d: d.find_elements(self.by, (self.val)), 3)[self.index].click()
                else:
                    self.wait(driver, lambda d: d.find_element(self.by, (self.val)), 3).click()
                time.sleep(self.wait_time)
                return 0
            if 'index' in self.op_dict:
                return self.wait(driver, lambda d: d.find_elements(self.by, (self.val)), self.wait_time)[self.index]
            return self.wait(driver, lambda d: d.find_element(self.by, (self.val)), self.wait_time)
        except:
            return -1
    
    def get_elements(self, driver):
        return self.wait(driver, lambda d: d.find_elements(self.by, (self.val)), self.wait_time)
    
    def wait(self, driver, func, time):
        res = WebDriverWait(driver, timeout=time).until(func)
        return res
