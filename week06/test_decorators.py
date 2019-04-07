import unittest
from decorators import *

class TestDecorators(unittest.TestCase):

    def test_accepts_decorator_when_each_argument_matches_the_type_then_return_function_with_agruments_which_types_are_specified_by_decorator(self):
        expr1 = str
        expr2 = int
        expected_result1 = 'Hello, I am Anna'
        expected_result2 = True
        self.assertEqual(say_hello("Anna"), expected_result1)
        self.assertEqual(deposit("Rosi", 10), expected_result2)

    def test_encrypt_decorator_that_takes_an_integer_and_returns_encrypted_string_of_a_function(self):
        expr = 2
        expected_result = "Igv igv igv nqy"
        self.assertEqual(encrypt(expr)(get_low)(), expected_result)




if __name__ == '__main__':
    unittest.main()
