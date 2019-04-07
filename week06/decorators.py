import datetime
import time
from time import sleep
import random
from functools import wraps


def accepts(*args):
    def accepter(func):
        @wraps(func)
        def decorated(*args_func):
            for index in range(len(args_func)):
                if not isinstance(args_func[index], args[index]):
                    raise TypeError('Argument ' + str(index+1) + ' of ' + str(func.__name__) + ' is not ' + str(args[index].__name__)+ '!')
            return func(*args_func)
        return decorated
    return accepter

def encrypt(key):
    def accepter(func):
        @wraps(func)
        def decorated_func():
            message = func()
            translated = ''
            for character in message:
                if character.isalpha():
                    number = ord(character)
                    number += key
                    if character.isupper():
                        if number > ord('Z'):
                            number -= 26
                        elif number < ord('A'):
                            number += 26
                    elif character.islower():
                        if number > ord('z'):
                            numberber -= 26
                        elif number < ord('a'):
                            number += 26
                    translated += chr(number)
                else:
                    translated += character
            return translated
        return decorated_func
    return accepter

def log(file_name):
    def accepter(func):
        @wraps(func)
        def wrapper(*args):
            func_name = func.__name__
            time_in_seconds = time.time()
            current_time = datetime.datetime.fromtimestamp(time_in_seconds).strftime('%Y-%m-%d %H:%M:%S')
            with open(file_name, 'a') as file:
                file.write(func_name)
                file.write(" was called at ")
                file.write(current_time)
                file.write('\n')
            return func(*args)
        return wrapper
    return accepter

def performance(file_name):
    def accepter(func):
        @wraps(func)
        def wrapper(*args):
            func_name = func.__name__
            start_time = time.time()
            function = func(*args)
            end_time = time.time()
            with open(file_name, 'a') as file:
                file.write(func_name)
                file.write(" was called and took ")
                file.write(str(round((end_time - start_time), 2)))
                file.write(" seconds to complete ")
                file.write('\n')
            return function
        return wrapper
    return accepter

@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True
    
@log('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"


@performance('log.txt')
def something_heavy():
    sleep(2)
    return "I am done!"


def main():
    print(get_low())



if __name__ == '__main__':
    main()


