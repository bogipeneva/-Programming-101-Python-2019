import os
import sys

def wc(command, filename):
    file = open(filename)

    number_of_characters = 0
    number_of_lines = 0
    number_of_words = 0

    for line in file:
        wordslist=line.split()
        number_of_lines = number_of_lines + 1
        number_of_words = number_of_words+len(wordslist)
        number_of_characters = number_of_characters + len(line)

    if command == 'chars':
        return number_of_characters
    elif command == 'words':
        return number_of_words
    else:
        return number_of_lines

    file.close()


def main():

    command = sys.argv[1]
    filename = sys.argv[2]

    print(wc(command, filename))

if __name__ == '__main__':
    main()

