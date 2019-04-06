import sys

def cut_last_char(ls):
    ls = ls[0:len(ls) - 1]
    return ls

def cat(arguments):
    f = open(arguments)
    i =0
    array = f.readlines()

    while i < len(array) - 1:
        print(cut_last_char(array[i]))
        i = i + 1
   # print(f.readlines())
    print(array[i])
    f.close()


def main():
    arguments = sys.argv[1]
    cat(arguments)
    


if __name__ == '__main__':
    main()