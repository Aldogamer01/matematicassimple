import unittest
from src.SDNN import SDNN
class TestSumaDeNumerosNaturales(unittest.TestCase):
    def test_SDNN(self):
        self.assertEqual(SDNN(10), 55)
        self.assertEqual(SDNN(20), 210)
        self.assertEqual(SDNN(30), 465)
        self.assertEqual(SDNN(40), 820)
        self.assertEqual(SDNN(50), 1275)

if __name__ == '__main__':
    unittest.main()