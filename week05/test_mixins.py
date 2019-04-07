import unittest
import mixins
from mixins import Panda
from mixins import Jsonable

class TestSerializingAndDeserializingFromOrtoJSONandXML(unittest.TestCase):
    def test_to_json_when_is_passed_object_then_return_string_of_his_json_representation(self):
        expr = Panda(name='Ivo', age = 20)
        expected_result = """{
    "dict": {
        "age": 20,
        "name": "Ivo"
    },
    "type": "Panda"
}"""
        # expected_result = ''
        self.assertEqual(expr.to_json(), expected_result)

    def test_from_json_when_is_passed_json_string_then_return_class_object(self):
        expected_result = Panda(name='Ivo', age = 20)
        expr = """{
    "dict": {
        "age": 20,
        "name": "Ivo"
    },
    "type": "Panda"
}"""

        self.assertEqual(Panda.from_json(expr), expected_result)
'''
    def test_to_xml_when_is_passed_object_then_return_string_of_his_xml_representation(self):
        expr = Panda(name='Ivo', age = 20)
        expected_result = """<Panda><name>Ivo</name><age>20</age></Panda>"""
        # expected_result = ''
        self.assertEqual(expr.to_xml(), expected_result)
'''

if __name__ == '__main__':
    unittest.main()