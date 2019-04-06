def list_user_data(all_user_data):
    list_of_user_data = []
    for key in all_user_data:
        for val_key in all_user_data[key]:
            for tuple_from_val in all_user_data[key][val_key]:
                    list_of_user_data.append(tuple_from_val)
    return list_of_user_data

def show_user_incomes(all_user_data):   
    list_of_incomes = []
    for key in all_user_data:
        if 'income' in all_user_data[key]:
            for tuple_from_val in all_user_data[key]['income']:
                list_of_incomes.append(tuple_from_val)
        else:
            pass
    return list_of_incomes

def show_user_savings(all_user_data):
    list_of_savings = []
    for key in all_user_data:
        for val_key in all_user_data[key]:
                for tuple_from_val in all_user_data[key][val_key]:
                    if tuple_from_val[1] == 'Savings':
                        list_of_savings.append(tuple_from_val)
    return list_of_savings


def show_user_deposits(all_user_data):
    list_of_deposits = []
    for key in all_user_data:
        for val_key in all_user_data[key]:
                for tuple_from_val in all_user_data[key][val_key]:
                    if tuple_from_val[1] == 'Deposit':
                        list_of_deposits.append(tuple_from_val)
    return list_of_deposits


def show_user_expenses(all_user_data):
    list_of_expenses = []
    for key in all_user_data:
        if 'expense' in all_user_data[key]:
            for tuple_from_val in all_user_data[key]['expense']:
                list_of_expenses.append(tuple_from_val)
        else:
            pass
    return list_of_expenses


def list_user_expenses_ordered_by_categories(all_user_data):
    list_of_expenses = show_user_expenses(all_user_data)
    list_of_expenses.sort(key=lambda elem: elem[1])
    return list_of_expenses


def show_user_data_per_date(date, all_user_data):
    list_of_user_data_per_date = []
    key = '===' + ' ' + date + ' ' + '==='
    if key in all_user_data:
        for val_key in all_user_data[key]:
            for tuple_from_val in all_user_data[key][val_key]:
                list_of_user_data_per_date.append(tuple_from_val)
    else:
        pass
    return list_of_user_data_per_date


def list_income_categories(all_user_data):
    list_of_income_categories = []
    for key in all_user_data:
        if 'income' in all_user_data[key]:
            for tuple_from_val in all_user_data[key]['income']:
                list_of_income_categories.append(tuple_from_val[1])
        else:
            pass
    return list_of_income_categories


def list_expense_categories(all_user_data):
    list_of_expense_categories = []
    for key in all_user_data:
        if 'expense' in all_user_data[key]:
            for tuple_from_val in all_user_data[key]['expense']:
                list_of_expense_categories.append(tuple_from_val[1])
        else:
            pass
    return list_of_expense_categories


def add_income(income_category, money, date, all_user_data):
    key = '===' + ' ' + date + ' ' + '==='
    if key in all_user_data:
        if 'income' in all_user_data[key]:
            all_user_data[key]['income'].append((money, income_category))
        else:
            all_user_data[key].update({'income':[(money, income_category)]})
    else:
        all_user_data.update({key:{'income':[(money, income_category)]}})
    return all_user_data[key]['income']


def add_expense(expense_category, money, date, all_user_data):
    key = '===' + ' ' + date + ' ' + '==='
    if key in all_user_data:
        if 'expense' in all_user_data[key]:
            all_user_data[key]['expense'].append((money, expense_category))
        else:
            all_user_data[key].update({'expense':[(money, expense_category)]})
    else:
        all_user_data.update({key:{'expense':[(money, expense_category)]}})
    return  all_user_data[key]['expense']

def main():
  
    file = open('money_tracker.txt')
    tuple_of_lines = tuple(file)
    print(tuple_of_lines)
    key = tuple_of_lines[0]
    key = key[:len(key) - 1]
    val = {}
    all_user_data = {}
    for line in tuple_of_lines[1:]:
        current_line = line.split(', ')
        if line == '\n':
            continue
        if line[0] == '=' :
            all_user_data.update({key: val})
            key = line[:len(line) - 1]
            val = {}
        else:
            first, second = current_line[2].split(' ')
            if line == tuple_of_lines[-1]:
                val_key = str(second.lower())
            else:
                val_key = str(second[:len(second) - 1]).lower()

            list_of_tuple = [(float(current_line[0]), current_line[1])]
            if val_key in val:
                val[val_key].append((float(current_line[0]), current_line[1]))
            else:
                val.update({val_key: list_of_tuple})

    all_user_data.update({key: val})
    print(all_user_data)

    file.close()
    while True:

            print('Hello, Peter!',
                'Choose one of the following options to continue:',
                '1 - show all data',
                '2 - show data for specific date',
                '3 - show expenses, ordered by categories',
                '4 - add new income',
                '5 - add new expense',
                '6 - exit', sep='\n')

            number = input()
            if int(number) < 1 or int(number) > 6:
                raise ValueError("Oops!  That was not number from 1 to 6.  Try again...")
            if number == '1':
                for key in all_user_data:
                    print(key)
                    date = key[4:len(key)-4]
                    print(show_user_data_per_date(date, all_user_data))


            elif number == '2':
                print('Choose data:')
                date = input()
                print(show_user_data_per_date(date, all_user_data))
            elif number == '3':
                print(list_user_expenses_ordered_by_categories(all_user_data))
            elif number == '4':
                print('New income amount:')
                income = input()
                print('New income type:')
                income_type = input()
                print('New income date:')
                income_date = input()
                add_income(income_type, income, income_date, all_user_data)
            elif number == '5':
                print('New expense amount:')
                expense = input()
                print('New expense type:')
                expense_type = input()
                print('New expense date:')
                expense_date = input()
                add_expense(expense_type, expense, expense_date, all_user_data)
            else:
                open('money_tracker.txt', "w").close()
                f = open('money_tracker.txt', "a")
                for keys, values in all_user_data.items():
                    f.writelines(keys+'\n')
                    for keys1, values1 in all_user_data[keys].items():
                        for i in range(len(values1)):
                            f.writelines(str(values1[i][0])+', '+values1[i][1]+', '+'New'+' '+keys1+'\n')
                print(all_user_data)
                break

if __name__ =='__main__':
    main()