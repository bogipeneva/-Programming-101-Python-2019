

def deep_update(data, key, val):

    for keys, child in data.items():
        if keys == key:
            data.update({keys:val})

        elif isinstance(child, dict):
            deep_update(child, key, val)

        elif isinstance(child, Iterable):
            for element in child:
                if isinstance(element, dict):
                    deep_update(element, key, val)

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
    deep_update(data, 'type', 'beast')
    print(data)

if __name__ == '__main__':
    main()