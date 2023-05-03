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
    
#     def test_error_finding_element(self):
#         log(self.app.app_func('chinese', 'bad_thumb_up'))
    
    def test_search(self):
        search_keyword = 'china'
        r = log(self.app.app_func(search_keyword, 'get_title'))
        self.assertTrue(isinstance(r, list))
        self.assertTrue(len(r) > 0)
    
    def test_search_special_Arabic(self):
        search_keyword = u'الكتاب يقرأ من عنوانه'
        r = log(self.app.app_func(search_keyword, 'get_title'))
        self.assertTrue(isinstance(r, list))
        self.assertTrue(len(r) > 0)

    def test_search_special_characters(self):
        search_keyword = u'##*()(*32)'
        r = log(self.app.app_func(search_keyword, 'get_title'))
        self.assertTrue(isinstance(r, list))
        self.assertTrue(len(r) > 0)
    
    def test_thumb_up(self):
        r = log(self.app.app_func('chinese', 'thumb_up'))
        self.assertTrue(r == 0)

    def test_thumb_up_10(self):
        r = log(self.app.app_func('chinese', 'thumb_up_10'))
        self.assertTrue(r == 0)
    
    def test_get_desc(self):
        search_keyword = 'China Daily'
        r = log(self.app.app_func(search_keyword, 'get_desc'), 'log/video_decs_log.txt')
        self.assertTrue(isinstance(r, list))
        # self.assertTrue(len(r) > 5)
    
    def test_get_desc_bad(self):
        search_keyword = u'新中国成立视频'
        r = log(self.app.app_func(search_keyword, 'get_desc'), 'log/video_decs_log.txt')
        self.assertTrue(isinstance(r, list))
        # self.assertTrue(len(r) > 5)
    
