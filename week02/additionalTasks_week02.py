
import sys
sys.path.insert(0, '/home/helious/bogiPython/week01')

def anagrams():
    
    print('Input:')
    Input = input()
    first_word, second_word = Input.split(' ')

    first_word_sorted = sorted(first_word.upper())
    second_word_sorted = sorted(second_word.upper())

    if first_word_sorted == second_word_sorted:
        return "ANAGRAMS"
    else:
        return "NOT ANAGRAMS"

from week01 import to_digits
from week01 import sum_of_digits



def is_credit_card_valid(number):

    number_of_digits = len(str(number))


    if number_of_digits % 2 == 0:
        return False

    numbers = [int(digits) for digits in str(number)]
    changed_numbers = []

    for index in range(len(numbers)):
        if index % 2 != 0:
            changed_numbers.append(numbers[index] * 2)
        else:
            changed_numbers.append(numbers[index])

    if sum([sum_of_digits(element) for element in changed_numbers]) % 10 == 0:
        return True
    else:
        return False

from week01 import isPrime

def goldbach(n):
    list_of_tuples = []
    number = int(n/2)
    
    for number in range(2, number +1):
        if isPrime(number) and isPrime(n - number):
            list_of_tuples.append((number, n-number))

    return list_of_tuples


def main():
    pass


if __name__ == '__main__':
    main()