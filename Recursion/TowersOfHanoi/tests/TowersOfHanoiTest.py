import unittest
from ..towersOfHanoi import towersOfHanoi

class TowersOfHanoiTest(unittest.TestCase):
    def test_success(self):
        result = towersOfHanoi()
        self.assertEqual(result,1)
