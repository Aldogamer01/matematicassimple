import unittest
from src.fibonacci import fibonacci
class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), [1,1,2,3,5])
        self.assertEqual(fibonacci(6), [1,1,2,3,5,8])
        self.assertEqual(fibonacci(7), [1,1,2,3,5,8,13])
        self.assertEqual(fibonacci(8), [1,1,2,3,5,8,13,21])
        self.assertEqual(fibonacci(9), [1,1,2,3,5,8,13,21,34])

if __name__ == '__main__':
    unittest.main()