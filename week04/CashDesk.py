class CustomError(Exception):
    pass

class Bill:

    def __init__(self, amount):
        self.validate_amount(amount)
        self.amount = amount

    def validate_amount(self, amount):
        if amount < 0:
            raise ValueError('negative amount, try again')
        if not isinstance(amount, int):
            raise TypeError('amount')

    def __str__(self):
        result = 'A' + ' ' + str(self.amount) + '$' + ' ' + 'bill'
        return result

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return int(self.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)

class BatchBill:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)

    def total(self):
        count = 0
        index = 0
        while index < len(self):
            count += self.lst[index].amount
            index += 1
        return count
    

    def __getitem__(self, index):
        return self.lst[index]



class CashDesk:
     total_money_amount=0
     bills=[]

     def __init__(self):
        pass

     def take_money(self, money):
            if isinstance(money, Bill):
                self.total_money_amount += money.amount
                self.bills.append(money)
            if isinstance(money, BatchBill):
                self.total_money_amount += money.total()
                for bill in money:
                    self.bills.append(bill)
            
     def total(self):
        return self.total_money_amount

     def inspect(self):
        print("We have the following count of bills, sorted in ascending order:")
        unique_bills=[]
        for bill in self.bills:
            if bill not in unique_bills:
                unique_bills.append(bill)
        for bill in unique_bills:
            s=str(int(bill))+'$ bills '+str(self.bills.count(bill))
            print(s)




def main():
    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]

    batch = BatchBill(bills)

    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))

    print(desk.total()) # 390
    desk.inspect()

if __name__ == '__main__':
    main()