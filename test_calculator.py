#https://github.com/PokeKoa/lab10-MQ-FL/tree/main
#Partner 1: Mike Quick
#Partner 2: Frankie Lin

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3,4),7)
        self.assertEqual(add(-1,-1),-2)
        self.assertEqual(add(0,0),0)

    def test_subtract(self):
        self.assertEqual(subtract(11,5),6)
        self.assertEqual(subtract(-1,-1),0)
        self.assertEqual(subtract(0,5),-5)


    
    def test_multiply(self): # 3 assertions
         self.assertEqual(mul(3,2), 6)
         self.assertEqual(mul(3,-2), -6)
         self.assertEqual(mul(5,47), 5*47)

    def test_divide(self): # 3 assertions
         self.assertEqual(div(3,2), 1.5)
         self.assertEqual(div(3,-2), -1.5)
         self.assertEqual(div(5,47), 5/47)
    

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5,0)
        with self.assertRaises(ZeroDivisionError):
            divide(0,0)

    def test_logarithm(self):
        self.assertEqual(logarithm(3,27),3)
        self.assertEqual(logarithm(10, 1),0)
        self.assertAlmostEqual(logarithm(10,100),2)



    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(8, -1)

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(4,3), 5)
        self.assertEqual(hypotenuse(13,84),85)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-64)
        self.assertEqual(square_root(64), 8)
        self.assertEqual(square_root(4096), 64)

# Do not touch this
if __name__ == "__main__":
    unittest.main()