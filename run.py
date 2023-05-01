# -*- coding:utf-8 -*-
import unittest
import os
import time
import HTMLTestRunner

from app.app import App

# 用例路径
case_path = os.path.join(os.getcwd(), 'testcases')
# 报告存放路径
report_path = os.path.join(os.getcwd(), 'report')

if __name__ == '__main__':
    bilibili = App('caps_bili.json')
    bilibili.app_replace_install()
    load_case = unittest.defaultTestLoader.discover(case_path, "test_*.py")
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_abspath = os.path.join(report_path, "result_"+now+".html")
    with open(report_abspath, "wb") as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='App Auto Test', description='Test Results:')
        runner.run(load_case)
    bilibili.app_uninstall()
