
import os, sys


def chain(iterable_one, iterable_two):
    for element in iterable_one:
        yield element
    for element in iterable_two:
        yield element

def compress(iterable, mask):
    for index in range(len(iterable)):
        if mask[index] == True:
            yield iterable[index]

def cycle(iterable):
    start = 1
    index = 0
    while start < 30:
        if iterable[index] == iterable[-1]:
            yield iterable[index]
            index = 0
            start += 1
        yield iterable[index]
        index += 1
        start += 1

def book_reader(list_of_files):
    list_of_files.reverse()
    for file in list_of_files:
        with open(file) as myFile:
            text = myFile.read()
        result = text.split('#')
        for chapter in result:
            yield chapter

def main():
    path = "/home/helious/bogiPython/week06/Book/book"
    dirs = os.listdir(path)
    gen_object = book_reader(dirs)

    index = 0
    for el in gen_object:
        key = input()
        if key == ' ':
            print(el)
        else:
            break





if __name__ == '__main__':
    main()
