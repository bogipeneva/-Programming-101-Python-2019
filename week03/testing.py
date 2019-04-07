
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
    sort_fractions = sorted(fractions)
    return sort_fractions

print(sort_fractions([(2, 3), (1, 2)]))