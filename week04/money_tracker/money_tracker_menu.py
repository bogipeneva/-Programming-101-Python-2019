from money_tracker_OO import *



class Menu():#TODO да оправя менюто!
    @staticmethod
    def call_method_by_option(number, money_tracker_object):

        if number < 1 or number >6:
            raise ValueError("Oops!  That was not number between 1 and 6.  Try again...")

        if number == '1':
            print(money_tracker_object.get_all_data())
        elif number == '2':
            print('Choose data:')
            date = input()
            print(money_tracker_object.get_data_per_date(date))
        elif number == '3':
            print(money_tracker_object.get_expenses_ordered_by_categories())
        elif number == '4':
            print('New income amount:')
            income = input()
            print('New income type:')
            income_type = input()
            print('New income date:')
            income_date = input()
            new_eleme = Income(income,income_type, income_date)
            money_tracker_object.add_income(new_eleme)
        elif number == '5':
            print('New expense amount:')
            expense = input()
            print('New expense type:')
            expense_type = input()
            print('New expense date:')
            expense_date = input()
            new_eleme = Expense(expense,expense_type, expense_date)
            money_tracker_object.add_expense(new_eleme)
        else:
            open('money_tracker.txt', "w").close()
            f = open('money_tracker.txt', "a")
            all_user_data = money_tracker_object.data_dictionary
            for keys, values in all_user_data.items():
                f.writelines(keys+'\n')
                for keys1, values1 in all_user_data[keys].items():
                        for i in range(len(values1)):
                            f.writelines(str(values1[i][0])+', '+values1[i][1]+', '+'New'+' '+keys1+'\n')
                break

def main():
    parsed_data = ParseData('money_tracker.txt')
    aggr_object = AggregatedObject(parsed_data.list_of_rows())
    money_obj = MoneyTracker(aggr_object)
    menu = Menu()
    print(menu.call_method_by_option(2,money_obj))


if __name__ == '__main__':
    main()
