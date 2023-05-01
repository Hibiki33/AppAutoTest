import unittest
from app.app import App

class TestVideo(unittest.TestCase):
    def setUp(self):
        self.app = App('caps_bili.json', 'bili_video.json')
    
    def tearDown(self):
        self.app.driver.quit()

    def test_all(self):
        all_tasks = self.app.app_func.get_task_list()
        for task in all_tasks:
            self.app.app_func('china', task)
    
    def test_search(self):
        self.app.app_func.search('china')
    
    def test_thumb_up(self):
        self.app.app_func('chinese', 'thumb_up')
    
    def test_get_desc(self):
        self.app.app_func('russia', 'get_desc')