from parse_money_tracker_data import ParseData
from category import Category
from category import Income
from category import Expense


class AggregatedObject:

    def __init__(self, parsed_data, list_of_incomes = [], list_of_expenses = []):
        self.parsed_data = parsed_data
        self.list_of_incomes = list_of_incomes
        self.list_of_expenses = list_of_expenses

    def create_dictionary(self):
        key = self.parsed_data[0]
        key = key[:len(key) - 1]
        val = {}
        all_user_data = {}
        for line in self.parsed_data[1:]:
            current_line = line.split(', ')
            if line[0] == '=' :
                all_user_data.update({key: val})
                key = line[:len(line) - 1]
                val = {}
            else:
                first, second = current_line[2].split(' ')
                if line == self.parsed_data[-1]:
                    val_key = str(second.lower())
                else:
                    val_key = str(second[:len(second) - 1]).lower()

                list_of_tuple = [(float(current_line[0]), current_line[1])]
                if val_key in val:
                    val[val_key].append((float(current_line[0]), current_line[1]))
                else:
                    val.update({val_key: list_of_tuple})
        all_user_data.update({key: val})

        return all_user_data

    def incomes(self):
        data_dictionary = self.create_dictionary()
        lst_incomes = []
        for key in data_dictionary:
            if 'income' in data_dictionary[key]:
                for tuple_from_val in data_dictionary[key]['income']:
                    lst_incomes.append(tuple_from_val)
            else:
                pass
        
        self.list_of_incomes = lst_incomes

        return lst_incomes

    def expenses(self):
        data_dictionary = self.create_dictionary()
        lst_expenses = []
        for key in data_dictionary:
            if 'expense' in data_dictionary[key]:
                for tuple_from_val in data_dictionary[key]['expense']:
                    lst_expenses.append(tuple_from_val)
            else:
                pass
        self.list_of_expenses = lst_expenses
        return lst_expenses

    
def main():
    parsed_data = ParseData('money_tracker.txt')
    obj = AggregatedObject(parsed_data.list_of_rows())
    print(obj.incomes())
    print(obj.expenses())
    
    

if __name__ == '__main__':
    main()



