import unittest
from app.app import App

class TestBuy(unittest.TestCase):
    def setUp(self):
        self.app = App('caps_bili.json', 'bili_buy.json')

    def test_buy1(self):
        print("buy1")

    def test_buy2(self):
        print("buy2")

    def test_buy3(self):
        print("buy3"