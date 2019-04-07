import unittest
import queries


class TestFilter(unittest.TestCase):
    def test_when_one_key_word_argument_is_passed_then_return_array_of_data_filtered_by_that_key_word(self):
        expr = "Diana Harris"
        file = 'example_data.csv'
        expected_result = [['lime', '5354', '1-860-251-9980x6941', 'timothy81@gmail.com', 'Martin-Barnes', 'Diana Harris']]
        self.assertEqual((queries.filter(file, full_name = expr)).sort(), expected_result.sort())

    def test_when_more_then_one_key_word_arguments_are_passed_then_return_array_of_arrays_filtered_by_all_of_arguments(self):
        expr_1 = "Diana Harris"
        expr_2 = 'lime'
        file = 'example_data.csv'
        expected_result = [['lime', '5354', '1-860-251-9980x6941', 'timothy81@gmail.com', 'Martin-Barnes', 'Diana Harris']]
        self.assertEqual((queries.filter(file, full_name = expr_1, favoutite_color='lime')).sort(), expected_result.sort())

    def test_when_filter_by_first_name_then_return_array_of_data_filtered_by_first_name(self):
        expr = "Diana"
        file = 'example_data.csv'
        expected_result = [['1-860-251-9980x6941', 'Martin-Barnes', '5354', 'Diana Harris', 'lime', 'timothy81@gmail.com'], ['659-155-8389x092', 'Hart, Ray and Wagner', '8587', 'Diana May', 'olive', 'eileen88@hotmail.com']]
        self.assertEqual((queries.filter(file, full_name_startswith = expr)).sort(), expected_result.sort())

    def test_filter_by_type_of_email_and_return_array_of_arrays_with_records_that_are_using_this_type(self):
        expr = "@yahoo"
        file = 'example_data.csv'
        expected_result = [['Michael Olson', 'zacharymcdonald@yahoo.com', 'olive', '114-116-1124x315', '2151', 'Scott, Young and King'], ['Marilyn Maldonado', 'gmcintosh@yahoo.com', 'black', '+49(1)7897611670', '7158', 'Walker PLC'], ['Courtney Lowery DVM', 'sharris@yahoo.com', 'lime', '(826)821-7107x2319', '169', 'Rogers PLC']]
        self.assertEqual((queries.filter(file, full_name_startswith = expr)).sort(), expected_result.sort())
    
    def test_filter_by_salary_grater_then_given_one_and_less_then_another_one_and_return_array_of_arrays_with_records_that_are_having_salary_in_given_interval(self):
        expr_1 = 3000
        expr_2 = 6000
        file = 'example_data.csv'
        expected_result = [['lime', 'timothy81@gmail.com', 'Martin-Barnes', '5354', '1-860-251-9980x6941', 'Diana Harris'], ['black', 'catherine64@gmail.com', 'Wilson, Smith and Vance', '5985', '(448)095-7360x318', 'Karen Lucas']]
        self.assertEqual((queries.filter(file, salary_gt = expr_1, salary_lt=expr_2)).sort(), expected_result.sort())
    
    def test_filter_when_is_passed_order_element_then_return_result_ordered_by_given_value(self):
        expr_1 = 3000
        expr_2 = 6000
        expr_3 = 'salary'
        file = 'example_data.csv'
        expected_result = [['Martin-Barnes', '5354', '1-860-251-9980x6941', 'timothy81@gmail.com', 'Diana Harris', 'lime'], ['Wilson, Smith and Vance', '5985', '(448)095-7360x318', 'catherine64@gmail.com', 'Karen Lucas', 'black']]
        self.assertEqual((queries.filter(file, salary_gt = expr_1, salary_lt=expr_2, order_by = expr_3)).sort(), expected_result.sort())
    
    def test_count_function_that_behaves_the_exact_same_way_as_filter_but_returns_only_count_of_results(self):
        expr = 'Diana'
        file = 'example_data.csv'
        expected_result = 2
        self.assertEqual(queries.count(file, full_name_startswith=expr), expected_result)

    def test_function_first_that_behaves_the_exact_same_way_as_filter_but_returns_only_first_element_of_result(self):
        expr = 'Diana'
        file = 'example_data.csv'
        expected_result = ['lime', 'Martin-Barnes', '5354', 'Diana Harris', 'timothy81@gmail.com', '1-860-251-9980x6941']
        self.assertEqual((queries.first(file, full_name_startswith=expr)).sort(), expected_result.sort())

    def test_function_last_that_behaves_the_exact_same_way_as_filter_but_returns_only_last_element_of_result(self):
        expr = 'Diana'
        file = 'example_data.csv'
        expected_result = ['Diana May', '8587', '659-155-8389x092', 'Hart, Ray and Wagner', 'eileen88@hotmail.com', 'olive']
        self.assertEqual((queries.last(file, full_name_startswith=expr)).sort(), expected_result.sort())
if __name__ =='__main__':
    unittest.main()