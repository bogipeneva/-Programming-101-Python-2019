
class ParseData():

    def __init__(self, file_name):
        self.file_name = file_name

    def list_of_rows(self):
        with open(self.file_name, "r") as file:
            array = []
            for rows in file:
                array.append(rows)
        return array

def main():
    parsed_data = ParseData('money_tracker.txt')
    print(parsed_data.list_of_rows())

if __name__ == '__main__':
    main()
