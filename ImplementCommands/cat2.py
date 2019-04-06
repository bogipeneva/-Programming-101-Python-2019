import sys

from cat import cat


def cat2(arguments):
    number_of_elements = len(arguments)
    i = 1
    while i < number_of_elements - 1:
        cat(arguments[i])
        print('\n')
        i = i + 1
    cat(arguments[i])


def main():
    arguments = sys.argv
    cat2(arguments)

if __name__ == '__main__':
    main()