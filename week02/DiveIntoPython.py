import sys
sys.path.insert(0, '/home/helious/bogiPython/week01')

def gas_stations(distance, tank_size, stations):
    get_stations_in_route = []
    distance_traveled = 0
    gas_stations = []

    while True:
        if distance_traveled + tank_size >= distance:
            break
        gas_stations = max([station for station in stations if station <= distance_traveled + tank_size])
        get_stations_in_route.append(gas_stations)
        distance_traveled = gas_stations

    return get_stations_in_route

'''
def gas_stations(distance, tank_size, stations): #  не работи за втория пример
    stations.append(distance)
    stations[:0-1]
    path = []
    current_tank_size = tank_size
    last_visited_station = stations[0]
    station_index = 0

    while station_index < len(stations):

        dist_between_stations = stations[station_index] - last_visited_station

        if current_tank_size <= dist_between_stations:
            path.append(last_visited_station)
            last_visited_station = stations[station_index]
        else:
            last_visited_station = stations[station_index]
            current_tank_size = dist_between_stations

        current_tank_size = tank_size - dist_between_stations

        station_index = station_index + 1

    return path
'''


from week01 import to_digits

def is_number_balanced(number):
    number_to_string = to_digits(number)
    number_of_digits = len(number_to_string)

    if number_of_digits == 1:
        return True

    middle_number = 1 if number_of_digits % 2 == 1 else 0

    left_part = number_to_string[:number_of_digits // 2]
    right_part = number_to_string[number_of_digits // 2 + middle_number:]

    if sum(left_part) == sum(right_part):
        return True
    else:
        return False

'''
print(is_number_balanced(9))
print(is_number_balanced(4518))

print(is_number_balanced(28471))
print(is_number_balanced(1238033))
'''

def increasing_or_decreasing(seq):
    
    if all(x<y for x, y in zip(seq, seq[1:])):
        return 'Up!'
    if all(x>y for x, y in zip(seq, seq[1:])):
        return 'Down!'
    return False
'''
print(increasing_or_decreasing([1,2,3,4,5]))
print(increasing_or_decreasing([5,6,-10]))
print(increasing_or_decreasing([1,1,1,1]))
print(increasing_or_decreasing([9,8,7,6]))
'''

from week01 import palindrome

def get_largest_palindrome(n):

    largest_palindrome = n - 1
    is_palindrome = False

    while True:
        is_palindrome = palindrome(largest_palindrome)

        if is_palindrome:
            break

        largest_palindrome = largest_palindrome - 1

    return largest_palindrome
'''
print(get_largest_palindrome(99))
print(get_largest_palindrome(252))
print(get_largest_palindrome(994687))
print(get_largest_palindrome(754649))
'''

import re

def sum_of_numbers(input_string):
    list_of_str = re.findall(r'\d+', input_string)
    list_of_numbers = [int(x) for x in list_of_str]

    return sum(list_of_numbers)
'''
print(sum_of_numbers("ab125cd3"))
print(sum_of_numbers("ab12"))
print(sum_of_numbers("ab"))
print(sum_of_numbers("1101"))
print(sum_of_numbers("1111O"))
print(sum_of_numbers("1abc33xyz22"))
print(sum_of_numbers("0hfabnek"))
'''
def birthday_ranges(birthdays, ranges):
    number_of_people_for_each_tuple = []
    count_of_people_in_one_tuple = 0

    for tuples in ranges:
        for element_index in range(len(birthdays)):
            if birthdays[element_index] >= tuples[0] and birthdays[element_index] <= tuples[1]:
                count_of_people_in_one_tuple = count_of_people_in_one_tuple + 1

        number_of_people_for_each_tuple.append(count_of_people_in_one_tuple)
        count_of_people_in_one_tuple = 0

    return number_of_people_for_each_tuple
'''
print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]))
'''
nokia = {
        0: ' ',
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }

def numbers_to_message(pressed_sequence):
  

    message = ""
    number_of_equal_digits = 0
    capitalized = False

    for digit_index in range(1, len(pressed_sequence)):

        if pressed_sequence[digit_index - 1] == 1:
            capitalized = True

        elif pressed_sequence[digit_index - 1] == -1:
            number_of_equal_digits = 0

        elif pressed_sequence[digit_index - 1] != pressed_sequence[digit_index]:
            if number_of_equal_digits > len(nokia[pressed_sequence[digit_index - 1]]) - 1:
                number_of_equal_digits = 0
           
            if not capitalized:
                message += nokia[pressed_sequence[digit_index - 1]][number_of_equal_digits]
            if capitalized:
                message += nokia[pressed_sequence[digit_index - 1]][number_of_equal_digits].upper()
                capitalized = False

            if digit_index == len(pressed_sequence) - 1:
                message += nokia[pressed_sequence[digit_index]][number_of_equal_digits] 

            number_of_equal_digits = 0
        else:
            number_of_equal_digits += 1
            if digit_index == len(pressed_sequence) - 1:
                if number_of_equal_digits > len(nokia[pressed_sequence[digit_index - 1]]) - 1:
                    number_of_equal_digits = 0
                if not capitalized:
                    message += nokia[pressed_sequence[digit_index - 1]][number_of_equal_digits]
                if capitalized:
                    message += nokia[pressed_sequence[digit_index - 1]][number_of_equal_digits].upper()
                    #number_of_equal_digits = 0
                    capitalized = False
    return message

#print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))
def append_numbers(list_of_chars, list_with_numbers):
    for el in list_of_chars:
        list_with_numbers.append(int(el))

def message_to_numbers(message):
    reversed_nokia = {}
    for key, val in nokia.items():
        string_key = str(key)
        for index in range(1, len(val) + 1):
            new_key = string_key*index
            reversed_nokia.update({val[index - 1]:new_key})

    sequence_of_numbers = []
    if message[0].isupper():
        sequence_of_numbers.append(1)
    append_numbers(reversed_nokia[message[0].lower()], sequence_of_numbers)

    for character in message[1:]:
        if character.isupper():
            sequence_of_numbers.append(1)
        if int(reversed_nokia[character.lower()][0]) == sequence_of_numbers[-1]:
            sequence_of_numbers.append(-1)
        append_numbers(reversed_nokia[character.lower()], sequence_of_numbers)

    return sequence_of_numbers





def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):
    if people_weight==[] or people_floors==[]:
        return 0
    trips=0
    current_weight=0
    start=0
    for index,person_weight in enumerate(people_weight):
        current_weight+=person_weight
        if current_weight>max_weight or len(people_weight[start:index])>=max_people :
            trips+=len(set(people_floors[start:index]))+1
            current_weight=person_weight
            start=index
    trips+=len(set(people_floors[start:]))+1
    return trips

