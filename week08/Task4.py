import copy
from collections.abc import Iterable

def deep_apply(func, data):
    copy_to_data = {}
    visited  = []
    list_of_elements = []

    for keys, child in data.copy.items():
            if not isinstance(child, Iterable):
                new_key = func(keys)
                data[new_key] 
                print('here')

            if isinstance(child, Iterable) and not isinstance(child, str):
                new_key = func(keys)
                copy_to_data[new_key] = 
                visited.append(child)



    for element in visited:
        if isinstance(element, dict):
            for keys, child in element.items():
                    if not isinstance(child, Iterable):
                        new_key = func(keys)
                        print(new_key)
                        copy_to_data[new_key] = child
                        print(copy_to_data[new_key])
                        print('all')
                    if isinstance(child, dict):

                         print('dict child')
                         visited.append(child)

                    elif isinstance(child, Iterable) and not isinstance(child, str):
                        print('iterable child')
                        for el in child:
                            if isinstance(el,dict):
                                visited.append(el)
                            elif isinstance(el, Iterable):
                                for element in el:
                                    if isinstance(element,dict):
                                        visited.append(element)


        elif isinstance(element, Iterable) and not isinstance(child, str):
            print('Iterable')
            for el in element:
                if isinstance(el, dict):
                    visited.append(el)
                elif isinstance(el, Iterable):
                    for element in el:
                        if isinstance(element,dict):
                            visited.append(element)





    return copy_to_data


def creat_new_key(key):
    key = key +'new'
    return key






def main():

    data = {
    "type": "Human",
    "dict": {
        "name": "Marto",
        "age": 20,
        
        "skills": [
            {
                "type": "Skill",
                "dict": {
                    "name": "X",
                    "level": 100
                }
            },
            {
                "type": "Skill",
                "dict": {
                    "name": "Y",
                    "level": 10
                }
            }
        ]
    }
}

    print(deep_apply(creat_new_key, data))



if __name__ == '__main__':
    main()