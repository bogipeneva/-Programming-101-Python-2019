from money_tracker import MoneyTracker
from category import *
from parse_money_tracker_data import *
from aggregated_money_tracker import *


class MoneyTrackerMenu:
    def __init__(self,AggregatedObject):
        self.AggregatedObject=AggregatedObject
        self.MoneyTrackerObject = MoneyTracker(self.AggregatedObject)
    def option(self):
        flag=True
        while flag:
            print("Choose one of the following options to continue:")
            print("1 - show all data")
            print("2 - show data for specific date")
            print("3 - show expenses, ordered by categories")
            print("4 - add new income")
            print("5 - add new expense")
            print("6 - exit")

            choice=input()
            if choice =='1':
                 print(self.MoneyTrackerObject.get_all_data())

            if choice =='2':
                date=input()
                print(self.MoneyTrackerObject.get_data_per_date(date))

            if choice =='3':
                print(self.MoneyTrackerObject.get_expenses_ordered_by_categories())

            if choice =='4':
                  print("New income amount:")
                  money=input()
                  if int(money) < 0:
                    raise CustomError('enter a valid amount')
                  print("New income type:")
                  income_category=input()
                  print("New income date:")
                  date = input()
                  income = Income(int(money),income_category,date)
                  self.MoneyTrackerObject.add_new_income(income)

            if choice =='5':
                  print("New expense amount:")
                  money=input()
                  if int(money) < 0:
                    raise CustomError('enter a valid amount')
                  print("New expense type:")
                  expense_category=input()
                  print("New expense date:")
                  date=input()
                  expense = Expense(int(money),expense_category,date)
                  self.MoneyTrackerObject.add_new_expense(expense)

            if choice=='6':#TODO да направя записването във файл
                 
                  flag=False
            if choice not in ('1','2','3','4','5','6'):
                raise Exception('Invalid input')
        

def main():
    parsed_data = ParseData('money_tracker.txt')
    obj = AggregatedObject(parsed_data.list_of_rows())
    menu = MoneyTrackerMenu(obj)
    menu.option()
if __name__=='__main__':
    main()

