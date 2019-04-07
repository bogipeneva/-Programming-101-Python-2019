
import json
import collections
from collections import namedtuple
import xml.etree.ElementTree as ET



class Jsonable:
    def to_json(self, indent = 4):
        dictionary = {}
        dictionary.update({'type': self.__class__.__name__})
        dictionary.update({'dict': self.__dict__})
        list_of_tuples_sorted_by_first_attr = sorted(dictionary.items(), key=lambda x: x[0])
        sorted_dictionary = collections.OrderedDict()
        for tuples in list_of_tuples_sorted_by_first_attr:
            if isinstance(tuples[1], dict):
                value = collections.OrderedDict(sorted(tuples[1].items(), key=lambda x: x[0]))
                sorted_dictionary.update({tuples[0]:value})
            else:
                sorted_dictionary.update({tuples[0]:tuples[1]})
        json_dictionary = json.dumps(sorted_dictionary, indent = indent)
        return json_dictionary


    @classmethod
    def from_json(cls, json_string):
        dictionary = json.loads(json_string)
        element = namedtuple(dictionary["type"], dictionary['dict'].keys())(*dictionary['dict'].values())
        return element

class Xmlable:
    def to_xml(self):
        result = ""
        result += "<"+self.__class__.__name__+">"
        for key in self.__dict__:
            result +=  "<"+key+">" + str(self.__dict__[key]) + "</"+key+">" 
        result += "</"+self.__class__.__name__+">"

        return result

    @classmethod
    def from_xml(cls, xml_string):
        root = ET.fromstring(xml_string)
        dictionary = collections.OrderedDict()
        for child in root:
            if child.text.isdigit():
                dictionary[child.tag]=int(child.text)
                continue
            if child.text=='True' or child.text=='False':
                dictionary[child.tag]=bool(child.text)
                continue
            dictionary[child.tag]=child.text

        new_object = namedtuple(root.tag, dictionary.keys())(*dictionary.values())

        return new_object
        

class Panda(Jsonable, Xmlable):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

def main():
    p = Panda(name='Ivo', age = 20)
    json_string = p.to_json()
    xml_string = p.to_xml()
    print(xml_string)
    p2 = Panda.from_xml(xml_string)
    print(p2)
    print(p==p2)


if __name__ == '__main__':
    main()
