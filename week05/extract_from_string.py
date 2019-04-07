
def extract_variable_and_power_from_string(s):
    splited_string = s.split('^')

    if len(splited_string) == 1:
        return splited_string[0], 1

    if len(splited_string) == 2:
        return splited_string[0], int(splited_string[1][0])


def extract_term_from_string(s):
    splited_string = s.split('*')

    if len(splited_string) == 1:
        try:
            int(splited_string[0])
            return int(splited_string[0]), None, 0
        except:
            return (1, *extract_variable_and_power_from_string(splited_string[0]))

    if len(splited_string) == 2:
        return (int(splited_string[0]), *extract_variable_and_power_from_string(splited_string[1]))

def main():
    s = 'x^2'
    print(extract_variable_and_power_from_string(s))

if __name__ == '__main__':
    main()



