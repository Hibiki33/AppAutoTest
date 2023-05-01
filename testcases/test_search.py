import unittest

class TestSearch(unittest.TestCase):
    '''登录模块'''
    csv_data = ReadCsvData()

    # @unittest.skip("skip test_normal_case")
    def test_normal_case(self):
        '''正常用例'''
        logn = LoginPage(self.driver)
        data = self.csv_data.get_csv_data(1) #取配置文件中的第一行
        logn.loginView(data[0],data[1])
        self.assertTrue(logn.check_login_status())

    @unittest.skip("skip test2")
    def test2(self):
        pass