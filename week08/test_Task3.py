import unittest
import copy
import Task3
from Task3 import *

class TestDeepUpdate(unittest.TestCase):

    data = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': [{
        'inner_key1': 'val1',
        'inner_key2': 'val2'
    }, { 'inner_key3': 'val3',
        'inner_key4': 'val4'}],
    'key4':({
        'inner_key5': 'val5',
    }),
    'key5':{
        'inner_key6': 'val6'
        },
    'inner_key1': 'bfs'
    }

    def test_deep_update_when_is_passed_key_that_is_not_in_dictionary_then_does_nothing(self):
        data = copy.deepcopy(self.data)
        print(data)
        deep_update(self.data, 'bfs', 'haha')
        print(data)
        self.assertEqual(self.data, data)


    def test_deep_update_when_is_passed_key_that_isin_dictionary_then_for_all_occurance_of_that_key_update_all_values_with_given_one(self):
        data =     data = {
            'key1': 'val1',
            'key2': 'val2',
            'key3': [{
                'inner_key1': 'new',
                'inner_key2': 'val2'
            }, { 'inner_key3': 'val3',
                'inner_key4': 'val4'}],
            'key4':({
                'inner_key5': 'val5',
            }),
            'key5':{
                'inner_key6': 'val6'
                },
            'inner_key1': 'new'
            }

        deep_update(self.data, 'inner_key1', 'new')

        self.assertEqual(sorted(self.data.items()), sorted(data.items()))





if __name__ == '__main__':
    unittest.main()