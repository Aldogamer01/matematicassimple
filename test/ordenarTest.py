import unittest
from src.ordenar import ordenar
class TestOrdenar(unittest.TestCase):
    def test_ordenar(self):
        self.assertEqual(ordenar(alreves=False, numeros=[13, 25, 31, 90, 98, 72, 6, 12, 16, 100, 44, 65, 19, 95, 43]), sorted(ordenar(alreves=False, numeros=[13, 25, 31, 90, 98, 72, 6, 12, 16, 100, 44, 65, 19, 95, 43])))
        self.assertEqual(ordenar(alreves=False, numeros=[13, 25, 31, 90, 98, 72, 6, 12, 16, 100, 44, 65, 19, 95, 43]), sorted(ordenar(alreves=False, numeros=[13, 25, 31, 90, 98, 72, 6, 12, 16, 100, 44, 65, 19, 95, 43])))
        self.assertEqual(ordenar(alreves=True, numeros=[50, 38, 21, 17, 33, 17, 31, 35, 55, 16, 93, 66, 7, 94, 27, 98, 34, 53, 76, 18]), sorted(ordenar(alreves=True, numeros=[50, 38, 21, 17, 33, 17, 31, 35, 55, 16, 93, 66, 7, 94, 27, 98, 34, 53, 76, 18]), reverse=True))
        self.assertEqual(ordenar(alreves=True, numeros=[47, 81, 85, 85, 28, 83, 25, 52, 4, 50, 25, 67, 47, 1, 98, 47, 41, 5, 4, 13, 92, 88, 6, 74, 56]), sorted(ordenar(alreves=True, numeros=[47, 81, 85, 85, 28, 83, 25, 52, 4, 50, 25, 67, 47, 1, 98, 47, 41, 5, 4, 13, 92, 88, 6, 74, 56]), reverse=True))
        self.assertEqual(ordenar(alreves=True, numeros=[40, 94, 2, 61, 80, 99, 86, 24, 25, 13, 84, 47, 58, 43, 2, 54, 30, 77, 66, 86, 84, 0, 66, 27, 24, 94, 13, 63, 35, 39]), sorted(ordenar(alreves=True, numeros=[40, 94, 2, 61, 80, 99, 86, 24, 25, 13, 84, 47, 58, 43, 2, 54, 30, 77, 66, 86, 84, 0, 66, 27, 24, 94, 13, 63, 35, 39]), reverse=True))

if __name__ == '__main__':
    unittest.main()