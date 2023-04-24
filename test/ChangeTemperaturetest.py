import unittest
from src.ChangeTemperature import temperatura
class TestChangeTemperature(unittest.TestCase):
    def test_temperatura(self):
        self.assertEqual(temperatura(conversion=1, grados=35), 95)
        self.assertEqual(temperatura(conversion=2, grados=95.9), 35.5)
        self.assertEqual(temperatura(conversion=1, grados=36), 96.8)
        self.assertEqual(temperatura(conversion=2, grados=93.7), 34.27777777777778)
        self.assertEqual(temperatura(conversion=1, grados=34.2), 93.56)

if __name__ == '__main__':
    unittest.main()