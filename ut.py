import unittest
from driver import BiliOperator, RunAppium

class TestCalculator(unittest.TestCase):
    # def testDivide01(self):
    #     cal = BiliOperator()
    #     cal.search_video(["china daily", "spaceX"])

    # def testDivide02(self):
    #     cal = BiliOperator()
    #     cal.search_buy([u'尼禄'])
        # self.assertEqual(cal.divide(), 3)
    
    def testALL(self):
        cal = BiliOperator()
        cal.search_video(['china daily', 'spaceX'])
        cal.search_buy([u'尼禄'])
        cal.driver.close_app()


if __name__ == '__main__':
    ra = RunAppium()
    unittest.main()
    