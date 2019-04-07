
def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 

def simplify_fraction(fraction):

    if not isinstance(fraction, tuple):
        raise Exception('not a tuple')

    if fraction[0] == fraction[1]:
        return (1, 1)
    elif fraction[0] == 1 or fraction[1] == 1:
        return fraction
    elif fraction[0] == 0:
        return (0, 0)
    else:
        Gcd = gcd(fraction[0], fraction[1])
        return ((int(fraction[0]/Gcd), int(fraction[1]/Gcd)))

def collect_fractions(fractions):
    tuple_fraction_1 = fractions[0]
    tuple_fraction_2 = fractions[1]

    lcd = (tuple_fraction_1[1] * tuple_fraction_2[1]) / gcd(tuple_fraction_1[1], tuple_fraction_2[1])

    first_number = tuple_fraction_1[0] * (lcd / tuple_fraction_1[1]) + tuple_fraction_2[0] * (lcd / tuple_fraction_2[1])
    second_number = lcd

    return simplify_fraction((first_number, second_number))


def sort_fractions(fractions):
    product = 1
    for tuples in fractions:
        product *= tuples[1]

    tuple_dictionary = {}

    for tuples in fractions:
        new_num1 = tuples[0] * (product / tuples[1])
        new_num2 = product
        tuple_dictionary.update({(tuples[0], tuples[1]): (new_num1, new_num2)})

    sorted_tuple_dictionary = sorted(tuple_dictionary.items(), key=lambda kv: kv[1])
    sorted_fractions = []

    for elements in sorted_tuple_dictionary:
        sorted_fractions.append(elements[0])

    return sorted_fractions

