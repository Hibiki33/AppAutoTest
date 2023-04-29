import unittest
from driver import BiliOperator

class TestCalculator(unittest.TestCase):
    def testDivide01(self):
        cal = BiliOperator()
        self.assertEqual(cal.divide(), 2)

    def testDivide02(self):
        cal = BiliOperator()
        self.assertEqual(cal.divide(), 3)

if __name__ == '__main__':
    unittest.main()