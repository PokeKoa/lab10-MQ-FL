import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    
    def test_multiply(self): # 3 assertions
         self.assertEqual(mul(3,2), 6)
         self.assertEqual(mul(3,-2), -6)
         self.assertEqual(mul(5,47), 5*47)

    def test_divide(self): # 3 assertions
         self.assertEqual(div(3,2), 1.5)
         self.assertEqual(div(3,-2), -1.5)
         self.assertEqual(div(5,47), 5/47)
    

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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