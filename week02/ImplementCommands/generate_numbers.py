import sys
from random import randint


def generate_numbers(filename, numbers):
    file = open(filename, "w") 
    n = int(numbers) 
    while n > 0 :
        file.write(str(randint(1, 1000)))
        file.write(' ')
        n = n - 1
    
    file.close()


def main():
    filename = sys.argv[1]
    numbers = sys.argv[2]

    generate_numbers(filename, numbers)

if __name__ == '__main__':
    main()