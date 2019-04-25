import unittest
import Task2
from Task2 import *

class TestDeepFindAll(unittest.TestCase):

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

    def test_dfs_deep_find_all_when_is_passed_key_that_is_not_in_passed_data_then_returns_empty_list(self):
        self.assertEqual(dfs_deep_find_all(self.data, 'kon'), [])

    def test_dfs_deep_find_all_when_is_passed_key_that_has_one_value_then_returns_list_of_that_value(self):
        self.assertEqual(dfs_deep_find_all(self.data, 'key1'), ['val1'])

    def test_dfs_deep_find_all_when_is_passed_key_that_has_more_then_one_value_then_returns_list_of_them(self):
#TODO да оправя разместването при рекурсията
        self.assertEqual(dfs_deep_find_all(self.data, 'inner_key1'), ['val1', 'bfs'])

    def test_bfs_deep_find_all_when_is_passed_key_that_is_not_in_passed_data_then_returns_empty_list(self):
        self.assertEqual(bfs_deep_find_all(self.data, 'kon'), [])

    def test_bfs_deep_find_all_when_is_passed_key_that_has_one_value_then_returns_list_of_that_value(self):
        self.assertEqual(bfs_deep_find_all(self.data, 'key1'), ['val1'])

    def test_bfs_deep_find_all_when_is_passed_key_that_has_more_then_one_value_then_returns_list_of_them(self):
        self.assertEqual(bfs_deep_find_all(self.data, 'inner_key1'), ['bfs', 'val1'])




if __name__ == '__main__':
    unittest.main()