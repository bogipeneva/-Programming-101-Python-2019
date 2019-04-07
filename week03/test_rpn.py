import unittest
from rpn import rpn_calculate

class TestReversePolishNotation(unittest.TestCase):
    def test_when_single_digit_is_passed_then_return_same_digit(self):
        expr = '45'
        expected_result = 45
        self.assertEqual(rpn_calculate(expr), expected_result)
    def test_when_two_digit_are_passed_then_return_sum_of_them(self):
        expr = '4 8 +'
        expected_result = 12
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_substraction_of_two_numbers_then_return_the_different(self):
        expr = '7 3 -'
        expected_result = 4
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_multiplication_of_two_numbers_then_return_the_product(self):
        expr = '2 2 *'
        expected_result = 4
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_devision_of_two_numbers_then_return_the_difference(self):
        expr = '8 2 /'
        expected_result = 4
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_sqrt_and_digit_are_passed_then_return_square_of_digit(self):
        expr = '16 SQRT'
        expected_result = 4
        self.assertEqual(rpn_calculate(expr), expected_result)





if __name__ =='__main__':
    unittest.main()