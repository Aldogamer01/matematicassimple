import unittest
from src.seno import seno
class TestSeno(unittest.TestCase):
    def test_seno(self):
        self.assertEqual(seno(numero=1,repeticiones=1000), 0.8414709848078965)
        self.assertEqual(seno(numero=2,repeticiones=1000), 0.9092974268256817)
        self.assertEqual(seno(numero=3,repeticiones=1000), 0.1411200080598671)
        self.assertEqual(seno(numero=4,repeticiones=1000), -0.7568024953079275)
        self.assertEqual(seno(numero=5,repeticiones=1000), -0.9589242746631357)

if __name__ == '__main__':
    unittest.main()