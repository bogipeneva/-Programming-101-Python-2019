import json 
import sys


def read_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

def best_person_in_every_language(json_file):

    data = read_json(json_file)

    best_person_in_every_language_dict = {}

    for person in data['people']:
        for objects in person['skills']:
            if objects['name'] in best_person_in_every_language_dict:
                if objects['level'] > best_person_in_every_language_dict[objects['name']][0]:
                    best_person_in_every_language_dict.update({objects['name']:(objects['level'], person['first_name'] + ' ' + person['last_name'])})
            else:
                best_person_in_every_language_dict.update({objects['name']:(objects['level'], person['first_name'] + ' ' + person['last_name'])})

    return best_person_in_every_language_dict


def main():
    dictionary = best_person_in_every_language(sys.argv[1])

    for key in dictionary:
        print(key + ' ' + '-' + ' ' + dictionary[key][1])


if __name__ == '__main__':
    main()