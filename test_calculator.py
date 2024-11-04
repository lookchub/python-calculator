import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        
    def test_add_neg(self):
        self.assertEqual(self.calc.add(-4, -5), -9)



    def test_sub_zero(self):
        self.assertEqual(self.calc.subtract(4, 2), 2) #wrong
    def test_sub_neg(self):
        self.assertEqual(self.calc.subtract(4, -2), 6) #wrong


    def test_multi_zero(self):
        self.assertEqual(self.calc.multiply(6, -2), -12) #wrong
    def test_multi_neg(self):
        self.assertEqual(self.calc.multiply(-3, -3), 9) #wrong


    def test_div_zero(self):
        self.assertEqual(self.calc.divide(10, 0), None) #wrong
    def test_div_positive(self):
        self.assertEqual(self.calc.divide(10, 2), 5) #wrong


    def test_mod_zero(self):
        self.assertEqual(self.calc.modulo(4, 2), 0) #wrong
    def test_mod_zero(self):
        self.assertEqual(self.calc.modulo(4, 3), 1) #wrong

    




    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()