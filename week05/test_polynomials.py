import unittest
import extract_from_string
from Polynomials import *

class TestPolynomialsImplementation(unittest.TestCase):
    def test_extract_variable_and_power_from_str_when_string_of_variable_on_power_is_passed_then_return_tuple_with_variable_and_power(self):
        expr = 'x^2'
        expected_result = ('x', 2)
        self.assertEqual(extract_from_string.extract_variable_and_power_from_string(expr), expected_result)

    def test_extract_term_from_string_when_string_of_term_is_passed_then_return_tuple_with_coefficient_variable_and_power(self):
        expr = '3*y^3'
        expected_result = (3, 'y', 3)
        self.assertEqual(extract_from_string.extract_term_from_string(expr), expected_result)

    def test_term_initial_value(self):
        term = Term(3, 'y', 3)
        assert term.coefficient == 3
        assert term.variable == 'y'
        assert term.power == 3

    def test_term_str_function(self):
        term = Term(3, 'y', 3)
        expected_result = '3*y^3'
        self.assertEqual(str(term), expected_result)

    def test_term_eq_function(self):
        term = Term(3, 'y', 3)
        term1 = Term(3, 'y', 3)
        expected_result = True
        self.assertEqual(term == term1, expected_result)

    def test_term_add_function(self):
        term = Term(3, 'y', 3)
        term1 = Term(5, 'y', 3)
        expected_result = Term(8, 'y', 3)
        self.assertEqual(term + term1, expected_result)

    def test_term_derivative_function(self):
        term = Term(3, 'y', 3) 
        expected_result = Term(9, 'y', 2)
        self.assertEqual(term.derivative(), expected_result)

    def test_term_class_function_extract_from_string_when_positive_coefficient_should_be_extracted(self):
        expr = '3*x^2'
        expected_result = Term(3, 'x', 2)
        self.assertEqual(Term.extract_from_string(expr, 1), expected_result)

    def test_term_class_function_extract_from_string_when_negative_coefficient_should_be_extracted(self):
        expr = '3*x^2'
        expected_result = Term(-3, 'x', 2)
        self.assertEqual(Term.extract_from_string(expr, -1), expected_result)

    def test_polynom_str_function(self):
        poly = Polynom.extract_from_string('2*x^2-3*x')
        expected_result = '2*x^2-3*x^1'
        self.assertEqual(str(poly), expected_result)

    def test_polynom_eq_function(self):
        poly = Polynom.extract_from_string('2*x^2-3*x')
        poly2 = Polynom.extract_from_string('2*x^2-3*x')
        assert poly == poly2

    def test_polynom_derivative_function(self):
        poly = Polynom.extract_from_string('2*x^2-3*x')
        derivative = str(poly.derivative())
        assert derivative == '4*x^1-3'

    def test_polynom_class_function_extract_from_string(self):
        expr = '3*x^2+7*x^3-2*x'
        expected_result = Polynom([Term.extract_from_string('3*x^2', 1), Term.extract_from_string('7*x^3', 1), Term.extract_from_string('2*x', -1)])
        self.assertEqual(Polynom.extract_from_string(expr), expected_result)


if __name__ == '__main__':
    unittest.main()