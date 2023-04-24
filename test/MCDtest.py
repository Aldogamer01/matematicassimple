import unittest
from src.MCD import MCD, maximo_comun_divisor
class Testmaximo_comun_divisor(unittest.TestCase):
    def test_MCD(self):
        self.assertEqual(MCD(1, 5), 1)
        self.assertEqual(maximo_comun_divisor(4, 252652), 4)
        self.assertEqual(MCD(34, 45), 1)
        self.assertEqual(maximo_comun_divisor(12,18), 6)
        self.assertEqual(MCD(18,12), 6)

if __name__ == '__main__':
    unittest.main()