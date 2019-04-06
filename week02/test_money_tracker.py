import unittest
import money_tracker


class TestMoneyTracker(unittest.TestCase):

    def test_list_user_data_when_not_empty_dictionar_is_passed_then_return_list_of_tuples(self):
        expr = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]}, '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result = [(700, 'Salary'), (50, 'Savings'), (4, 'Eating Out'), (10, 'Deposit'), (27.7, 'Food')]
        self.assertCountEqual(money_tracker.list_user_data(expr), expected_result)

    def test_show_user_incomes_when_dictionari_with_no_incomes_is_passed_then_return_empty_list(self):
        expr = {'22-03-2019': {'expense': [(10, 'Deposit'), (200, 'Savings')]}}
        expected_result = []
        self.assertEqual(money_tracker.show_user_incomes(expr), expected_result)

    def test_show_user_incomes_when_dictionari_with_incomes_is_passed_then_return_list_of_incomes_tuples(self):
        expr = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]}}
        expected_result = [(10, 'Deposit')]
        self.assertEqual(money_tracker.show_user_incomes(expr), expected_result)

    def test_show_user_savings_when_dictionari_with_no_savings_is_passed_then_return_empty_list(self):
        expr = {'22-03-2019': {'income': [(10, 'Deposit')]}}
        expected_result = []
        self.assertEqual(money_tracker.show_user_savings(expr), expected_result)

    def test_show_user_savings_when_dictionar_is_passed_then_return_list_of_tuples_in_which_second_element_is_savings(self):
        expr = {'22-03-2019': {'income': [(10, 'Deposit'), (200, 'Savings')], 'expense': [(27.7, 'Food')]}}
        expected_result = [(200, 'Savings')]
        self.assertEqual(money_tracker.show_user_savings(expr), expected_result)

    def test_show_user_deposits_when_dictionari_with_no_deposits_is_passed_then_return_empty_list(self):
        expr = {'22-03-2019': {'income': [ (200, 'Savings')]}}
        expected_result = []
        self.assertEqual(money_tracker.show_user_deposits(expr), expected_result)

    def test_show_user_deposits_when_not_empty_dictionar_is_passed_then_return_list_of_tuples_in_which_second_element_is_deposit(self):
        expr = {'22-03-2019': {'income': [(10, 'Deposit'), (200, 'Savings')], 'expense': [(27.7, 'Food')]}}
        expected_result = [(10, 'Deposit')]
        self.assertEqual(money_tracker.show_user_deposits(expr), expected_result)

    def test_show_user_expenses_when_dictionari_with_no_expenses_is_passed_then_return_empty_list(self):
        expr = {'22-03-2019': {'income': [(10, 'Deposit'), (200, 'Savings')]}}
        expected_result = []
        self.assertEqual(money_tracker.show_user_expenses(expr), expected_result)

    def test_show_user_expenses_when_dictionary_with_expenses_is_passed_then_return_list_of_expenses_tuples_(self):
        expr = {'22-03-2019': {'income': [(10, 'Deposit'), (200, 'Savings')], 'expense': [(27.7, 'Food')]}}
        expected_result = [(27.7, 'Food')]
        self.assertEqual(money_tracker.show_user_expenses(expr), expected_result)

    def test_list_user_expenses_ordered_by_categories_when_dictionari_with_no_expenses_is_passed_then_return_empty_list(self):
        expr = {'22-03-2019': {'income': [(10, 'Deposit')]}}
        expected_result = []
        self.assertEqual(money_tracker.list_user_expenses_ordered_by_categories(expr), expected_result)

    def test_list_user_expenses_ordered_by_categories_when_dictionary_is_passed_then_return_list_of_expenses_tuples_ordered_by_categories(self):
        expr = {'22-03-2019': {'income': [(10, 'Deposit'), (200, 'Savings')], 'expense': [(27.7, 'Food'), (200, 'Air')]}}
        expected_result = [(200, 'Air'), (27.7, 'Food')]
        self.assertEqual(money_tracker.list_user_expenses_ordered_by_categories(expr), expected_result)

    def test_show_user_data_per_date_when_is_passed_date_that_do_not_exist_in_dictionary_then_return_empty_list(self):
        dictionary = {'=== 22-03-2019 ===': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]}, '=== 23-03-2019 ===': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        date = '24-03-2019'
        expected_result = []
        self.assertEqual(money_tracker.show_user_data_per_date(date, dictionary), expected_result)

    def test_show_user_data_per_date_when_is_passed_date_that_exist_in_dictionary_then_return_list_of_tuples_with_data_for_that_date(self):
        dictionary = {'=== 22-03-2019 ===': {'income': [(10, 'Deposit')]}, '=== 23-03-2019 ===': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        date = '22-03-2019'
        expected_result = [(10, 'Deposit')]
        self.assertEqual(money_tracker.show_user_data_per_date(date, dictionary), expected_result)

    def test_list_income_categories_when_is_passed_dictionary_with_no_income_data_then_return_empty_list(self):
        expr = {'=== 22-03-2019 ===': {'expense': [(27.7, 'Food')]}, '=== 23-03-2019 ===': {'expense': [(4, 'Eating Out')]}}
        expected_result = []
        self.assertEqual(money_tracker.list_income_categories(expr), expected_result)

    def test_list_income_categories_when_is_passed_dictionary_with_income_data_then_return_list_of_income_categories(self):
        expr = {'=== 23-03-2019 ===': {'income': [(700, 'Salary'), (380, 'Deposit')], 'expense': [(4, 'Eating Out')]}}
        expected_result = ['Salary', 'Deposit']
        self.assertEqual(money_tracker.list_income_categories(expr), expected_result)

    def test_list_expense_categories_when_is_passed_dictionary_with_no_expense_data_then_return_empty_list(self):
        expr = {'=== 22-03-2019 ===': {'income': [(27.7, 'Food')]}, '=== 23-03-2019 ===': {'income': [(4, 'Eating Out')]}}
        expected_result = []
        self.assertEqual(money_tracker.list_expense_categories(expr), expected_result)

    def test_list_expense_categories_when_is_passed_dictionary_with_expense_data_then_return_list_of_expense_categories(self):
        expr = {'=== 23-03-2019 ===': {'income': [(700, 'Salary'), (380, 'Deposit')], 'expense': [(4, 'Eating Out')]}}
        expected_result = ['Eating Out']
        self.assertEqual(money_tracker.list_expense_categories(expr), expected_result)

    def test_add_income_when_is_passed_date_that_do_not_exist_then_creat_new_date_and_save_incomes_there_and_return_them(self):
        expr = {'=== 23-03-2019 ===': {'income': [(700, 'Salary'), (380, 'Deposit')], 'expense': [(4, 'Eating Out')]}}
        date = '24-03-2018'
        categorie = 'Deposit'
        money = 200
        expected_result = [(200, 'Deposit')]
        self.assertEqual(money_tracker.add_income(categorie, money, date, expr), expected_result)

    def test_add_income_when_is_passed_date_that_exist_then_save_incomes_there_and_return_them(self):
        expr = {'=== 23-03-2019 ===': {'expense': [(4, 'Eating Out')]}}
        date = '23-03-2019'
        categorie = 'Deposit'
        money = 200
        expected_result = [(200, 'Deposit')]
        self.assertEqual(money_tracker.add_income(categorie, money, date, expr), expected_result)

    def test_add_expense_when_is_passed_date_that_do_not_exist_then_creat_new_date_and_save_expense_there_and_return_them(self):
        expr = {'=== 23-03-2019 ===': {'income': [(700, 'Salary'), (380, 'Deposit')], 'expense': [(4, 'Eating Out')]}}
        date = '24-03-2018'
        categorie = 'Food'
        money = 200
        expected_result = [(200, 'Food')]
        self.assertEqual(money_tracker.add_expense(categorie, money, date, expr), expected_result)

    def test_add_expense_when_is_passed_date_that_exist_then_save_expense_there_and_return_them(self):
        expr = {'=== 23-03-2019 ===': {'income': [(4, 'Eating Out')]}}
        date = '23-03-2019'
        categorie = 'food'
        money = 200
        expected_result = [(200, 'food')]
        self.assertEqual(money_tracker.add_expense(categorie, money, date, expr), expected_result)

if __name__ == '__main__':
    unittest.main()
