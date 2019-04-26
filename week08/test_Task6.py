import unittest
import copy
from Task6 import *



class TestSchemaValidator(unittest.TestCase):
    schema = [
    'key1',
    'key2',
    [
        'key3',
        ['inner_key1', 'inner_key2']
    ]
]

    def test_schema_validator_when_is_passed_dictionary_that_do_not_contains_all_of_the_keys_from_schema_then_returns_false(self):
        data = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': {
        'inner_key1': 'val1'
    }
}
        self.assertFalse(schema_validator(self.schema, data))

    def test_schema_validator_when_is_passed_dictionary_that_contains_more_keys_then_keys_that_are_from_schema_then_returns_false(self):
        data = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': {
        'inner_key1': 'val1',
        'inner_key2': 'val2'
    },
    'key4': 'not expected'
}

        self.assertFalse(schema_validator(self.schema, data))

    def test_schema_validator_when_are_passed_schema_and_dictionary_that_have_missmatch_in_keys_then_returns_false(self):
        data = {
    'key1': 'val1',
    'key4': 'val2',
    'key3': {
        'inner_key1': 'val1',
        'inner_key2': 'val2'
    }
}
        self.assertFalse(schema_validator(self.schema, data))

    def test_scheme_validator_when_are_passed_is_passed_dictionary_that_contains_all_keys_from_passed_schema_then_returns_true(self):
        data = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': {
        'inner_key1': 'val1',
        'inner_key2': 'val2'
    }
}
        self.assertTrue(schema_validator(self.schema, data))




if __name__ == '__main__':
    unittest.main()