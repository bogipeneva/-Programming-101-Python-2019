import unittest
import Task1
from Task1 import *

class TestDeepFind(unittest.TestCase):

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

    def test_dfs_deep_find_when_is_passed_key_that_is_not_in_dictionary_then_return_none(self):
        self.assertEqual(dfs_deep_find(self.data, 'key23'), None)

    def test_dfs_deep_find_when_is_passed_key_which_value_is_string_then_return_that_value(self):
        self.assertEqual(dfs_deep_find(self.data, 'key2'), 'val2')

    def test_dfs_deep_find_when_is_passed_key_which_value_is_dictionary_then_return_that_dictionary(self):
        self.assertEqual(dfs_deep_find(self.data, 'key5'), { 'inner_key6': 'val6'})

    def test_dfs_deep_find_when_is_passed_key_that_is_inner_key_from_dictionary(self):
        self.assertEqual(dfs_deep_find(self.data, 'inner_key6'), 'val6')

    def test_dfs_deep_find_when_is_passed_key_that_is_inner_key_from_dictionary_that_is_from_list(self):
        self.assertEqual(dfs_deep_find(self.data, 'inner_key3'), 'val3')

    def test_dfs_deep_find_when_is_passed_key_that_is_inner_key_from_dictionary_that_is_from_tuple(self):
        self.assertEqual(dfs_deep_find(self.data, 'inner_key5'), 'val5')


    def test_bfs_deep_find_when_is_passed_key_that_is_not_in_dictionary_then_return_none(self):
        self.assertEqual(bfs_deep_find(self.data, 'key23'), None)

    def test_bfs_deep_find_when_is_passed_key_which_value_is_string_then_return_that_value(self):
        self.assertEqual(bfs_deep_find(self.data, 'key2'), 'val2')

    def test_bfs_deep_find_when_is_passed_key_which_value_is_dictionary_then_return_that_dictionary(self):
        self.assertEqual(bfs_deep_find(self.data, 'key5'), { 'inner_key6': 'val6'})

    def test_bfs_deep_find_when_is_passed_key_that_is_inner_key_from_dictionary(self):
        self.assertEqual(bfs_deep_find(self.data, 'inner_key1'), 'bfs')

    def test_bfs_deep_find_when_is_passed_key_that_is_inner_key_from_dictionary_that_is_from_list(self):
        self.assertEqual(bfs_deep_find(self.data, 'inner_key3'), 'val3')

    def test_bfs_deep_find_when_is_passed_key_that_is_inner_key_from_dictionary_that_is_from_tuple(self):
        self.assertEqual(bfs_deep_find(self.data, 'inner_key5'), 'val5')


if __name__ == '__main__':
    unittest.main()