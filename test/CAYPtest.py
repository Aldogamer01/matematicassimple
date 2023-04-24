import unittest
from src.CAYP import CAYP
class TestCAYP(unittest.TestCase):
    def test_CAYP(self):
        self.assertEqual(CAYP(figura="cuadrado", AP=1, lado=40), 1600)
        self.assertEqual(CAYP(figura="rectangulo", AP=2, lado=25, lado2=50), 150)
        self.assertEqual(CAYP(figura="circulo", AP=1, radio=36), 4071.50394945237)
        self.assertEqual(CAYP(figura="pentagono", AP=1, lado=60, radio=51), 7650)
        self.assertEqual(CAYP(figura="triangulo", AP=2, lado=30, lado2=26, lado3=34), 90)

if __name__ == '__main__':
    unittest.main()