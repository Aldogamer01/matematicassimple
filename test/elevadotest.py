import unittest
from src.elevado import elevado
class TestElevado(unittest.TestCase):
    def test_elevado(self):
        self.assertEqual(elevado(1, 6742), 6742)
        self.assertEqual(elevado(2,3), 9)
        self.assertEqual(elevado(2,5), 25)
        self.assertEqual(elevado(3,2), 8)
        self.assertEqual(elevado(3,4), 64)

if __name__ == '__main__':
    unittest.main()