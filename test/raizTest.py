import unittest
from src.raiz import raiz
class TestRaiz(unittest.TestCase):
    def test_raiz(self):
        self.assertEqual(raiz(raiz=2, numero=2), 1.41)
        self.assertEqual(raiz(raiz=2, numero=4), 2)
        self.assertEqual(raiz(raiz=3, numero=3), 1.44)
        self.assertEqual(raiz(raiz=3, numero=27), 3)
        self.assertEqual(raiz(raiz=3, numero=64), 4)
        self.assertEqual(raiz(raiz=2, numero=8), 2.83)
        self.assertEqual(raiz(raiz=3, numero=27), 3)

if __name__ == '__main__':
    unittest.main()