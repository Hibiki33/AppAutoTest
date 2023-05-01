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

        # search test
        titles, descs = cal.search_video(['china daily', 'spaceX'])
        self.assertNotEqual(len(titles), 0)
        self.assertNotEqual(len(descs), 0)
        with open('search_results.txt', 'w', encoding = 'utf-8') as fp:
            for title in titles:
                fp.write(title + '\n')
        with open('comments.txt', 'w', encoding = 'utf-8') as fp:
            for desc in descs:
                fp.write(desc + '\n')

        # buy test
        cal.search_buy([u'尼禄'])
        cal.driver.close_app()


if __name__ == '__main__':
    ra = RunAppium()
    unittest.main()
    