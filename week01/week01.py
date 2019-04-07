def sum_of_digits(n):
    sum = 0;
    if n < 0:
        n*= (-1)

    while n>0:
        temp = n%10
        sum+=temp
        n//=10
    return sum


def to_digits(n):
    list = []
    while n > 0:
        temp = n % 10
        list.append(temp)
        n//=10
    list.reverse()
    return list



def to_number(digits):
    number = 0
    k = len(digits)
    index = range(k)
    for ind in index:
        item = digits[ind]

        temp = 10 ** k
        item *= temp
        number += item
        k -= 1
    number /= 10
    return number



def fact_number(n):
    sum = 1
    index = 1
    while index <= n:
        sum *= index
        index += 1
    return sum


def fact_digits(n):
    sum = 0
    
    while n > 0:
        item = n % 10
        item = fact_number(item)
        sum += item
        n //= 10
    return sum


def reverse_string(string):
    result = ''
    n = len(string)

    for i in range(n):
        result += string[n - i - 1]

    return result

def palindrome(obj):
    string_repr_of_obj = str(obj)
    return string_repr_of_obj == reverse_string(string_repr_of_obj)




def count_vowels(string):
    num_vowels=0
    for char in string:
        if char in "aeiouyAEIOUY":
           num_vowels = num_vowels+1
    return num_vowels


def count_consonants(string):
    num_vowels=0
    for char in string.lower():
        if char in "bcdfghjklmnpqrstvwxz":
           num_vowels = num_vowels+1
    return num_vowels



def count_times(str, elem):
    count = 0
    chars = [str(digit) for digit in str]

    for char in chars:
        if char == elem:
            count += 1
    return count



def char_histogram(string):
    out = {}
    for c in string:
        out[c] = out.get(c, 0) + 1
    return out



def g(arg):
    return arg


def p(arg):
    return True


def f(args):
    result = []

    for arg in args:
        if p(arg):
            result.append(g(arg))

    return result

def ff(args):
    return [g(arg) for arg in args]
    # List comprehension



def sum_of_digits(n):
    return sum(to_digits(n))


def to_digits(n):
    n = abs(n)

    return [int(ch) for ch in str(n)]


def join(items, delimiter):
    result = ''
    n = len(items)

    for index in range(n):
        item = items[index]

        result = result + item

        if index != n - 1:
            result += delimiter

    return result


def to_number(digits):
    chars = [str(digit) for digit in digits]

    return int(join(chars, ''))

def fact(n):
    if n in [0, 1]:
        return 1

    result = 1

    for x in range(n):
        result *= x + 1

    return result


def fact_digits(n):
    return sum([fact(digit) for digit in to_digits(n)])




def sum_matrix(matrix):
    return sum([sum(x) for x in matrix])



def nan_expand(n):
    string = ""
    if n == 0:
        return string
    i = 0
    list = []
    while i < n:
        list.append("Not a")
        i = i+1
    list.append("Nan")
    string = join(list, ' ')
    return string


def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True




def  prime_factorization(n):

    dict = {}

    if isPrime(n):
        return [(n, 1)]

    i = 2
    while n > 0 and i <= n:
        while n % i == 0 and isPrime(i):
            dict[i] = dict.get(i, 0) + 1
            n = n / i
        i = i +1

    result = [(k, dict[k]) for k in dict]
    return result

    

def group(llist): 
    final_group = []
    current_group = [llist[0]]
    for i in range(1,len(items)):
        if current_group[-1] == llist[i]:
            current_group.append(llist[i])
        else:
            final_group.append(current_group)
            current_group = [llist[i]]
    final_group.append(current_group)
    return final_group


def max_consecutive(items):
    result=1
    max_result=0
    last_seen=items[0]

    for v in items[1:]:
        if v==last_seen:
            result += 1
        else:
            if result > max_result:
                max_result = result
            last_seen = v
            result = 1
            
    if result > max_result:
        max_result = result

    return max_result


def number_of_words(string, word):
    normal = string
    reverse = reverse_string(string)

    n = len(word); count = 0;

    idx = 0; start = 0;
    while idx >= 0:
        idx = normal.find(word, start)
        if idx >= 0:
            count+=1
        start=idx+1
    idx = 0; start = 0;
    while idx >= 0:
        idx = reverse.find(word, start)
        if idx >= 0:
            count+=1
        start=idx+1

    return count

def find_diagonals(grid):
    pass
#TODO да допиша търсенето в диагонал
def search_word(grid, word):

    n = len(grid[0])
    m = len(grid)
    if n == 1:
        from_cols = sum([number_of_words(''.join(i), word) for i in zip(*grid)])
        return from_cols
    if m == 1:
        from_rows = sum([number_of_words(''.join(i), word) for i in grid])
        return from_rows

    from_cols = sum([number_of_words(''.join(i), word) for i in zip(*grid)])
    from_rows = sum([number_of_words(''.join(i), word) for i in grid])
    return from_cols+from_rows 

def main():
    pass
if __name__ == '__main__':
    main()
