import unittest
from src.primo import primo
class TestPrimo(unittest.TestCase):
    def test_primo(self):
        self.assertEqual(primo(numero=5), True)
        self.assertEqual(primo(numero=3), True)
        self.assertEqual(primo(numero=9), False)
        self.assertEqual(primo(numero=6), False)
        self.assertEqual(primo(numero=4), False)

if __name__ == '__main__':
    unittest.main()