import csv
import sys

def filter(file_name, **kwargs):
    list_of_dictionaries = []
    result=[]
    list_with_results = []
    f = open(file_name, 'rt')
    try:
        reader = csv.DictReader(f)
        for row in reader:
            list_of_dictionaries.append(row)
        add = True
        for element in list_of_dictionaries:
            for key, value in kwargs.items():
                if key in element:
                    if element[key] == value:
                        continue
                    else:
                        add = False
                elif key == 'full_name_startswith':
                    
                    if element['full_name'].split(' ')[0] == value:
                        continue
                    else:
                        add = False
                elif key == 'email__contains':
                    first, second = element['email'].split('@')
                    value = value[1:]
                    second = second[:len(second) - 4]
                    if second == value:
                        continue
                    else:
                        add = False
                elif key == 'salary_gt':
                    if int(element['salary']) > value:
                        continue
                    else:
                        add = False
                elif key == 'salary_lt':
                    if int(element['salary']) < value:
                        continue
                    else:
                        add = False
                else:
                    pass
            if add:
                result.append(element)
            else:
                add = True
        if 'order_by' in kwargs.keys():
            result = sorted(result, key=lambda k: k[kwargs['order_by']])

        for element in result:
            elements = [val for val in element.values()]
            list_with_results.append(elements)

        return list_with_results
    finally:
        f.close()
        
def count(file_name, **kwargs):
    count_of_result_elements = len(filter(file_name, **kwargs))
    return count_of_result_elements

def first(file_name, **kwargs):
    all_elements = filter(file_name, **kwargs)
    return all_elements[0]

def last(file_name, **kwargs):
    all_elements = filter(file_name, **kwargs)
    return all_elements[-1]

def main():

    print(filter('example_data.csv', company_name ="Scott, Young and King"))
    
if __name__ == '__main__':
    main()