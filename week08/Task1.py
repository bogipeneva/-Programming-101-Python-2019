from collections.abc import Iterable


def dfs_deep_find(data, key):
    for keys, child in data.items():
        if keys == key:
            return child

        elif isinstance(child, dict):
            result = dfs_deep_find(child, key)
            if result is not None:
                return result

        elif isinstance(child, Iterable):
            for element in child:
                if isinstance(element, dict):
                    if dfs_deep_find(element, key) != None:
                        return dfs_deep_find(element, key)
        #return None

def bfs_deep_find(data, key):
    visited  = []

    for keys, child in data.items():
        if keys == key:
            return child
        elif isinstance(child, Iterable):
            visited.append(child)

    for element in visited:
        if isinstance(element, dict):
            for keys, child in element.items():
                if keys == key:
                    return child
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




def main():
    data={'A':[1,{'X':[[1,2,3],{'C1':100}]}],
          'B':[2,3],
          'C':{'C1':4, 'C2':5},
          }
    print(bfs_deep_find(data, 'C1'))

if __name__ == '__main__':
    main()


