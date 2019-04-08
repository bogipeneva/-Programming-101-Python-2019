
import random
from random import choice
import string
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

def word_generator(length=8, chars=string.ascii_letters + string.digits):
    return ''.join([choice(chars) for i in range(length)])

def words_generator(word_range):
    return ' '.join([word_generator(random.randint(1,20)) for i in word_range])

def book_generator(chapters_count, chapter_length):
    #TODO да го направя да генерира различни файлове + номерацията на текста 
    path = '/home/helious/python101/week06/Book/book'

    if not os.path.exists(path):
        os.makedirs(path)

    buff = ''

    with open(os.path.join(path, '003.txt'), 'a') as temp_file:
        for chapter in range(1, chapters_count+1):
            chapter_to_include = 'Chapter '+ str(chapter)+'\n'
            buff += chapter_to_include
            buff += words_generator(chapter_length)
            buff += '\n'
            temp_file.write(buff)


def main():
    
    path = "/home/helious/python101/week06/Book/book"
    dirs = os.listdir(path)
    gen_object = book_reader(dirs)
    for el in gen_object:
        key = input()
        if key == ' ':
            print(el)
        else:
            break
            
    book = book_generator(5, range(5, 10))






if __name__ == '__main__':
    main()
