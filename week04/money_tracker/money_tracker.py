from aggregated_money_tracker import *

class MoneyTracker:
    def __init__(self, aggregated_object):
        self.aggregated_object = aggregated_object
        self.data_dictionary = self.aggregated_object.create_dictionary()

    def get_savings(self):
        list_of_savings = []
        for key in self.data_dictionary:
            for val_key in self.data_dictionary[key]:
                    for tuple_from_val in self.data_dictionary[key][val_key]:
                        if tuple_from_val[1] == 'Savings':
                            list_of_savings.append(tuple_from_val)
        return list_of_savings

    def get_deposits(self):
        list_of_deposits = []
        for key in self.data_dictionary:
            for val_key in self.data_dictionary[key]:
                    for tuple_from_val in self.data_dictionary[key][val_key]:
                        if tuple_from_val[1] == 'Deposit':
                            list_of_deposits.append(tuple_from_val)
        return list_of_deposits

    def get_all_data(self):
        list_of_user_data = []
        for key in self.data_dictionary:
            for val_key in self.data_dictionary[key]:
                for tuple_from_val in self.data_dictionary[key][val_key]:
                        list_of_user_data.append(tuple_from_val)
        return list_of_user_data


    def get_income_categories(self):
        list_of_income_categories = []
        for key in self.data_dictionary:
            if 'income' in self.data_dictionary[key]:
                for tuple_from_val in self.data_dictionary[key]['income']:
                    list_of_income_categories.append(tuple_from_val[1])
            else:
                pass
        return list_of_income_categories


    def get_expense_categories(self):
        list_of_expense_categories = []
        for key in self.data_dictionary:
            if 'expense' in self.data_dictionary[key]:
                for tuple_from_val in self.data_dictionary[key]['expense']:
                    list_of_expense_categories.append(tuple_from_val[1])
            else:
                pass
        return list_of_expense_categories

    def get_expenses_ordered_by_categories(self):
        list_of_expenses = self.aggregated_object.expenses()
        list_of_expenses.sort(key=lambda elem: elem[1])
        return list_of_expenses

    def add_new_income(self, new_income):
        key = '===' + ' ' + new_income.date + ' ' + '==='
        if key in self.data_dictionary:
            if 'income' in self.data_dictionary[key]:
                self.data_dictionary[key]['income'].append((new_income.amount, new_income.type))
            else:
                self.data_dictionary[key].update({'income':[(new_income.amount, new_income.type)]})
        else:
            self.data_dictionary.update({key:{'income':[(new_income.amount, new_income.type)]}})
        return self.data_dictionary[key]['income']

    def add_new_expense(self, new_expense):
        key = '===' + ' ' + new_expense.date + ' ' + '==='
        if key in self.data_dictionary:
            if 'expense' in self.data_dictionary[key]:
                self.data_dictionary[key]['expense'].append((new_expense.amount, new_expense.type))
            else:
                self.data_dictionary[key].update({'expense':[(new_expense.amount, new_expense.type)]})
        else:
            self.data_dictionary.update({key:{'expense':[(new_expense.amount, new_expense.type)]}})
        return self.data_dictionary[key]['expense']

    def get_data_per_date(self, date):
        list_of_user_data_per_date = []
        key = '===' + ' ' + date + ' ' + '==='
        if key in self.data_dictionary:
            for val_key in self.data_dictionary[key]:
                for tuple_from_val in self.data_dictionary[key][val_key]:
                    list_of_user_data_per_date.append(tuple_from_val)
        else:
            pass
        return list_of_user_data_per_date


def main():
    parsed_data = ParseData('money_tracker.txt')
    obj = AggregatedObject(parsed_data.list_of_rows())
    money_tracker = MoneyTracker(obj)
    expense = Expense(600, 'Food', "23-03-2018")
    print(money_tracker.add_new_expense(expense))
    print(money_tracker.get_all_data())
    
    

if __name__ == '__main__':
    main()



