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
        search_keyword = 'ANIPLEX'
        r = log(self.app.app_func(search_keyword, 'add_cart'))
        self.assertTrue(isinstance(r, list))
        valid_names = []
        for i in r:
            if search_keyword in i:
                valid_names.append(i)
        self.assertTrue(len(valid_names) > 1)
        print("Normal test is passed")

#     def test_without_visiting_webview(self):
#         log(self.app.app_func('miku', 'vist_webview_bad'))

    def test_input_Chinese(self):
        search_keyword = u'尼禄'
        r = log(self.app.app_func(search_keyword, 'add_cart'))
        self.assertTrue(isinstance(r, list))
        valid_names = []
        for i in r:
            if search_keyword in i:
                valid_names.append(i)
        self.assertTrue(len(valid_names) > 1)
        print("Chinese search test is passed")
    
    
