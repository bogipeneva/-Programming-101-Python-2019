import unittest
import fractions


class TestSimplifyFractions(unittest.TestCase):

    def test_validate_function_object_is_a_tuple(self):
        #self.assertRaises(ValidationError, testing.simplify_fraction, (1, 2))
        with self.assertRaises(Exception) as exc:
            simplify_fraction([1, 2])
        print(str(exc.exception))
        self.assertTrue('not a tuple' in str(exc.exception))

    def test_when_are_passed_equal_digits_then_return_tuple_of_one(self):
        expr = (2, 2)
        expected_result = (1, 1)
        self.assertEqual(testing.simplify_fraction(expr), expected_result)
    def test_when_one_of_past_digits_in_tuple_is_one_then_return_same_tuple(self):
        expr = (1, 7)
        expected_result = (1, 7)
        self.assertEqual(testing.simplify_fraction(expr), expected_result)
    def test_when_is_passed_tuple_with_different_digits_then_return_tuple_of_them_devised_on_gcd(self):
        expr = (4, 10)
        expected_result = (2, 5)
        self.assertEqual(testing.simplify_fraction(expr), expected_result)
if __name__ =='__main__':
    unittest.main()