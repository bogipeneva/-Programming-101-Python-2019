from collections.abc import Iterable

def flatten(items):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, str):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x

def list_of_dictionary_keys(data):
    visited  = []
    keys = []

    for key, child in data.items():
            keys.append(key)
            if isinstance(child, Iterable):
                visited.append(child)

    for element in visited:
        if isinstance(element, dict):
            for key, child in element.items():
                keys.append(key)
                if isinstance(child, dict):
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
    return keys

def schema_validator(schema: list, data: dict):
    schema_keys = list(flatten(schema))
    dictionary_keys = list_of_dictionary_keys(data)

    if len(schema_keys) == len(dictionary_keys):
        return set(list(flatten(schema))) == set(dictionary_keys)
    return False


def main():
    schema = [
    'key1',
    'key2',
    [
        'key3',
        ['inner_key1', 'inner_key2', 'inner_key3']
    ]
]

    data = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': {
        'inner_key1': 'val1',
        'inner_key2': 'val2'
    },
    'inner_key3':'vs'
}

    print(list(flatten(schema)))
    print(list_of_dictionary_keys(data))
    print(schema_validator(schema, data))


if __name__ == '__main__':
    main()