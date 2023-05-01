from app.app import App
from testcases import test_buy, test_video
import unittest

if __name__ == '__init__':
    bilibili = App('caps_bili.json')
    bilibili.app_replace_install()
    unittest.main()
    bilibili.uninstall()