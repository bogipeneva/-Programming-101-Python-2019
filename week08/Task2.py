import collections
from collections.abc import Iterable


def dfs_deep_find_all(data, key):
    key_values = []

    for keys, child in data.items():
        if keys == key:
            key_values.append(child)

        elif isinstance(child, dict):
            key_values += dfs_deep_find_all(child, key)

        elif isinstance(child, Iterable):
            for element in child:
                if isinstance(element, dict):
                    key_values += dfs_deep_find_all(element, key)

    return key_values

def bfs_deep_find_all(data, key):
    visited  = []
    key_values = []

    for keys, child in data.items():
        if keys == key:
            key_values.append(child)
        elif isinstance(child, Iterable):
            visited.append(child)

    for element in visited:
        if isinstance(element, dict):
            for keys, child in element.items():
                if keys == key:
                    key_values.append(child)
                elif isinstance(child, dict):
                    visited.append(child)

                elif isinstance(child, Iterable):
                    for el in child:
                        if isinstance(el,dict):
                            visited.append(el)

        elif isinstance(element, Iterable):
            for el in element:
                if isinstance(el, dict):
                    visited.append(el)
                elif isinstance(el, Iterable):
                    for element in el:
                        if isinstance(element,dict):
                            visited.append(element)

    return key_values




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
    
    print(dfs_deep_find_all(data , 'type'))

if __name__ == '__main__':
    main()


