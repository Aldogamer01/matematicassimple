import unittest
from src.taylor import taylor
class TestTaylor(unittest.TestCase):
    def test_(self):
        self.assertEqual(taylor(x = 1, repeticiones=1000), 2.7182818284590455)
        self.assertEqual(taylor(x = 2, repeticiones=1500), 7.389056098930649)
        self.assertEqual(taylor(x = 3, repeticiones=2000), 20.08553692318766)
        self.assertEqual(taylor(x = 4, repeticiones=2500), 54.598150033144265)
        self.assertEqual(taylor(x = 5, repeticiones=3000), 148.41315910257657)

if __name__ == '__main__':
    unittest.main()