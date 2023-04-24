import unittest
from src.cuadratica import cuadratica
class TestCuadratica(unittest.TestCase):
    def test_cuadratica(self):
        self.assertEqual(cuadratica(2,3,-5), (1, -2.5))
        self.assertEqual(cuadratica(1,-6,8), (4,2))
        self.assertEqual(cuadratica(-1,1,6), (-2,3))
        self.assertEqual(cuadratica(1,1,-12), (3,-4))
        self.assertEqual(cuadratica(-3,1,4), (-1,4/3))

if __name__ == '__main__':
    unittest.main()