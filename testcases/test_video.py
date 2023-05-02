import unittest
from app.app import App
from common.log import log

class TestVideo(unittest.TestCase):
    def setUp(self):
        self.app = App('caps_bili.json', 'bili_video.json')
    
    def tearDown(self):
        self.app.driver.quit()

    # def test_all(self):
    #     all_tasks = self.app.app_func.get_task_list()
    #     for task in all_tasks:
    #         log(self.app.app_func('china', task), 'log/video_log.txt')
    
    def test_error_finding_element(self):
        log(self.app.app_func('chinese', 'bad_thumb_up'))
    
    def test_search(self):
        log(self.app.app_func.search('china'))
    
    def test_thumb_up(self):
        log(self.app.app_func('chinese', 'thumb_up'))
    
    def test_get_desc(self):
        log(self.app.app_func('American', 'get_desc'), 'log/video_decs_log.txt')