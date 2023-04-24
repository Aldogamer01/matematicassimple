import unittest
from src.leibniz import leibniz
class TestLeibniz(unittest.TestCase):
    def test_leibniz(self):
        self.assertEqual(leibniz(100), 3.1315929035585537)
        self.assertEqual(leibniz(200), 3.136592684838816)
        self.assertEqual(leibniz(300), 3.138592903409963)
        self.assertEqual(leibniz(400), 3.139592655589785)
        self.assertEqual(leibniz(500), 3.140092653621041)

if __name__ == '__main__':
    unittest.main()