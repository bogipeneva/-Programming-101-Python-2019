from contextlib import contextmanager

@contextmanager
def assertRaises(exception_expected, msg=None):
     try:
        yield
        raise Exception('exception not found')
     except Exception as exc:
        if type(exc) == exception_expected:
            if msg is not None and msg == str(exc):
                return True
            else:
                raise Exception('message is wrong')
        raise Exception('Exception found, but it\'s not ower')


def some_function(num1, num2):
    if num1 < 0 or num2 < 0:
        raise Exception('Only positive integers')

    return num1 + num2

def main():
    with assertRaises(Exception, 'Only positive integers'):
        some_function(-1,2)

if __name__ == '__main__':
    main()