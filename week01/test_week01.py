import unittest
from week01 import *

class TestFunctionsFromWeek01(unittest.TestCase):
    def test_sum_of_digits_that_calculate_the_sum_of_n_digits(self):
        self.assertEqual(sum_of_digits(1325132435356), 43)
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(6), 6)
        self.assertEqual(sum_of_digits(-10), 1)

    def test_to_digits_when_is_passed_integer_then_returns_a_list_that_contain_the_digits_of_n(self):
        self.assertEqual(to_digits(123), [1, 2, 3])
        self.assertEqual(to_digits(99999), [9, 9, 9, 9, 9])
        self.assertEqual(to_digits(123023), [1, 2, 3, 0, 2, 3])

    def test_to_number_when_list_of_digits_is_passed_then_returns_the_number_that_contain_those_digits(self):
        self.assertEqual(to_number([1,2,3]), 123)
        self.assertEqual(to_number([9, 9, 9, 9, 9]), 99999)
        self.assertEqual(to_number([1, 2, 3, 0, 2, 3]), 123023)
        self.assertEqual(to_number([2, 1, 2, 3, 3]), 21233)

    def test_fact_digits_that_takes_an_integer_and_returns_the_sum_of_the_fractorials_of_each_digit_of_the_number(self):

        self.assertEqual(fact_digits(111), 3)
        self.assertEqual(fact_digits(145), 145)
        self.assertEqual(fact_digits(999), 1088640)

if __name__ == '__main__':
    unittest.main()