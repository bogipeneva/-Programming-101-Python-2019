import datetime
import time
from time import sleep
from contextlib import contextmanager


@contextmanager
def performance(file_name):
        start_time = time.time()

        yield 

        file = open(file_name, 'a')
        current_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        file.write("Date ")
        file.write(current_time)
        file.write(' Execution time: ')
        end_time = time.time()
        file.write(str(round((end_time - start_time), 16)))
        file.write('\n')
        file.close()


def main():
    pass

if __name__ == '__main__':
    main()