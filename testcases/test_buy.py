import unittest
from app.app import App
from common.log import log

class TestBuy(unittest.TestCase):
    def setUp(self):
        self.app = App('caps_bili.json', 'bili_buy.json')
    
    def tearDown(self):
        self.app.driver.quit()

    # def test_all(self):
    #     all_tasks = self.app.app_func.get_task_list()
    #     for task in all_tasks:
    #         log(self.app.app_func('miku', task), 'log/buy_log.txt')

    def test_good(self):
        log(self.app.app_func(u'尼禄', 'add_cart'))

    def test_without_visiting_webview(self):
        log(self.app.app_func('miku', 'vist_webview_bad'))

    def test_bad(self):
        log(self.app.app_func('miku', 'add_cart_bad'))
    
    