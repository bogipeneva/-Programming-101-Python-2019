import sys
from extract_from_string import extract_term_from_string


class Term:

    def __init__(self, coefficient, variable, power):

        self.coefficient = coefficient
        self.variable = variable
        self.power = power

    def __str__(self):
        if self.variable is None or self.power == 0 :
            return str(self.coefficient)

        return (str(self.coefficient) + '*' + str(self.variable) +'^'+str(self.power))

    def __eq__(self, other):
        return self.coefficient == other.coefficient and self.variable == other.variable and self.power == other.power

    def __add__(self, other):
        if other.variable != self.variable or other.power != self.power:
            raise Exception("wrong operation")

        return Term(
            self.coefficient + other.coefficient,
            self.variable,
            self.power
        )

    def derivative(self):
        if self.variable is None and self.power == 0:
            return Term(0, None, 0)

        return Term(
            self.coefficient * self.power,
            self.variable,
            max(0, self.power - 1)
        )

    @classmethod
    def extract_from_string(cls, s, sign):
        coefficient, variable, power = extract_term_from_string(s)
        if sign == -1:
            coefficient *= -1
        return cls(coefficient, variable, power)

class Polynom:
    def __init__(self, terms):
        self.terms = {}

        for term in terms:
            if term.power in self.terms:
                self.terms[term.power] += term
            else:
                self.terms[term.power] = term

    def __str__(self):
        list_of_sorted_terms = []
        result = ''

        for power in sorted(self.terms.keys(), reverse=True):
            list_of_sorted_terms.append(str(self.terms[power]))

        result+=list_of_sorted_terms[0]

        for term in list_of_sorted_terms[1:]:
            if term[0] == '-':
                result+=term
            else:
                result=result+'+'+term

        return result
    def __eq__(self, other):
        for key, val in self.terms.items():
            if key in other.terms and val == other.terms[key]:
                pass
            else:
                return False
        return True


    def derivative(self):

        terms_derivatives =[]
        for key in self.terms:
            terms_derivatives.append(self.terms[key].derivative())

        return Polynom(terms_derivatives)

    @classmethod
    def extract_from_string(cls, string):
        sign = 1
        term = ''
        terms = []
        for digit in string:
            if digit == '-':
                terms.append(Term.extract_from_string(term, sign))
                sign = -1
                term = ''
            elif digit == '+':
                terms.append(Term.extract_from_string(term, sign))
                sign = 1
                term = ''
            else:
                term+=digit
        terms.append(Term.extract_from_string(term, sign))


        return cls(terms)

def main():
    poly = Polynom.extract_from_string(sys.argv[1])


    print('Derivative of f(x) = ' + str(poly)+' is:')
    print('f`(x) = ' + str(poly.derivative()))



    '''
    t1 =  Term(2, 'x', 4)
    t2 = Term.extract_from_string('2')
    print(str(t1))
    print(str(t2))
    print(t1 == t2)
    print(str(t1.derivative()))
    t3 = Term(3, 'x', 4)

    t4 = t1+t3
    print(t4)

    poly = Polynom([t1, t3, t4])
    print(str(poly))
    poly2 = Polynom.extract_from_string('2*x^3+11*x^2')
    print(poly2)
    print(poly2.derivative())
    '''



if __name__ == '__main__':
    main()
