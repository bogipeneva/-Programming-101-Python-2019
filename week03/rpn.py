import math
import operator


  
def rpn_calculate(expression):

    stack = []

 
    for value in expression.split(' '):
        result = value
        if value in ['-', '+', '*', '/']:
            op1 = stack.pop()
            op2 = stack.pop()
            if value == '-': result = op2 - op1
            if value == '+': result = op2 + op1
            if value == '*': result = op2 * op1
            if value == '/': result = op2 / op1
            stack.append(result)
        elif value in ['SQRT','TAN', 'COS', 'SIN']:
            op = stack.pop()
            if value == 'SQRT': result = math.sqrt(op)
            if value == 'TAN': result = math.tan(op*(math.pi/180))
            if value == 'COS': result = math.cos(op*(math.pi/180))
            if value == 'SIN': result = math.sin(op*(math.pi/180))
            stack.append(result)
        else:
            stack.append(float(value))
 
    return stack.pop()

def main():
    pass

if __name__ == '__main__':
  main()