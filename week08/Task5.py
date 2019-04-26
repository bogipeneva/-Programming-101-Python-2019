import collections
from collections.abc import Iterable

def deep_compare(d1, d2):
    visited  = []
    key_values = []
    equal = True

    if type(d1) == type(d2):
        if isinstance(d1, dict):

            if d1.keys() != d2.keys():
                equal = False
            else:
                common_keys = set(d1.keys())
                for key in common_keys:
                    if d1[key] != d2[key]:
                        equal = False
                    elif isinstance(d1[key], Iterable):
                        visited.append(d1[key])

            for element in visited:
                if isinstance(element, dict):
                    for keys, child in element.items():
                        if d1.keys() != d2.keys():
                            equal = False
                        else:
                            common_keys = set(d1.keys())
                            for key in common_keys:
                                if d1[key] != d2[key]:
                                    equal = False
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

        elif isinstance(d1, Iterable) and not isinstance(d1, (set, tuple,list)):
            if len(d1) != len(d2):
                equal = False

            for i in range(len(d1)):
                equal = deep_compare(d1[i], d2[i])

        else:
            if d1 != d2:
                equal = False
    else:
        equal = False

    return equal


if __name__ == '__main__':
    pass