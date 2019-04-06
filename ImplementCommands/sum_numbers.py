import sys


def sum_numbers(filename):
    f = open(filename)

    string = f.readlines()[0]
    number_of_numbers = len(string)
    
    i = 0
    sum = 0
    temp =  " "
    temp_int = 0

    while i < number_of_numbers:
        if string[i] != " ":
            temp += string[i]
        else:
            temp_int = int(temp)
            sum = sum + temp_int
            temp = ' '
        i = i + 1

    temp_int = int(temp)

    return sum + temp_int

    f.close()



def main():
    file_name = sys.argv[1]
    print(sum_numbers(file_name))

if __name__ == '__main__':
    main()