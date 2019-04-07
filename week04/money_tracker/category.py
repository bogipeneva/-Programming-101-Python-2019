from datetime import datetime
class Category:

    def __init__(self, amount, category_type, date):
        self.verification(amount, category_type, date)
        self.amount = amount
        self.type = category_type
        self.date = date

    def verification(self, amount, category_type, date):
        if amount < 0:
            raise ValueError('You are trying to add negative amount, try agaiT')
        if not isinstance(category_type, str):
            raise TypeError('Wrong type, category should be string')
        if date != datetime.strptime(date, "%d-%m-%Y").strftime('%d-%m-%Y'):
            raise ValueError()

class Expense(Category):
    
    def __init__(self, expense_amount, expense_type, date):
        super().__init__(expense_amount, expense_type, date)

class Income(Category):
    def __init__(self, income_amount, income_type, date):
        super().__init__(income_amount, income_type, date)

def main():
    obj = Income(300, 'Deposit', '22-02-2039')
    print(obj.date)

if __name__ == '__main__':
    main()
