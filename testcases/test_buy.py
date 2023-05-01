import unittest
from app.app import App

class TestBuy(unittest.TestCase):
    def setUp(self):
        self.app = App('caps_bili.json', 'bili_buy.json')
    
    def tearDown(self):
        self.app.driver.quit()

    def test_all(self):
        all_tasks = self.app.app_func.get_task_list()
        for task in all_tasks:
            self.app.app_func('miku', task)