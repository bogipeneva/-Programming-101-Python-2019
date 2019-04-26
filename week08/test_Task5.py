import unittest
import copy
import Task5
from Task5 import *

class TestDeepCompare(unittest.TestCase):

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
            }, {
        'inner_key5': 'val5',
    }),
    'key5':{
        'inner_key6': 'val6'
        },
    'inner_key1': 'bfs'
    }

    def test_deep_compare_when_are_passed_iterable_objects_that_are_from_different_types_then_returns_false(self):
        d1 = (1,2,3)
        d2 = [1,2,3]
        self.assertFalse(deep_compare(d1, d2))

    def test_deep_compare_when_are_passed_iterable_objects_from_one_type_that_are_not_dictionaries_or_sets_and_are_equal_then_returns_true(self):
        d1 = (1,2,3)
        d2 = (1,2,3)
        self.assertTrue(deep_compare(d1, d2))

    def test_deep_compare_when_are_passed_iterable_objects_from_one_type_that_are_not_dictionaries_or_sets_and_are__not_equal_then_returns_false(self):
        d1 = (1,2,3)
        d2 = (1,7,3)
        self.assertFalse(deep_compare(d1, d2))

    def test_deep_compare_when_are_passed_two_sets_and_they_are_not_equal_then_returns_false(self):
        d1 = {1,2,3,4}
        d2 = {1,7,3}
        self.assertFalse(deep_compare(d1, d2))

    def test_deep_compare_when_are_passed_two_sets_and_they_are_equal_then_returns_true(self):
        d1 = {1,3,4,7}
        d2 = {1,7,3,1,4}
        self.assertTrue(deep_compare(d1, d2))

    def test_deep_compare_when_are_passed_iterarable_objects_that_have_iterable_elements_and_they_are_different_but_from_one_type_then_returns_false(self):
        d1 = (1,2,3,[4,5,6])
        d2 = (1,2,3, [11,5,6])
        self.assertFalse(deep_compare(d1, d2))

    def test_deep_compare_when_are_passed_equal_iterarable_objects_that_are_not_dictionaries_and_have_iterable_elements_that_are_equal_then_returns_true(self):
        d1 = (1,2,3,[4,5,6])
        d2 = (1,2,3, [4,5,6])
        self.assertTrue(deep_compare(d1, d2))

    def test_deep_compare_when_are_passed_iterable_objects_that_are_not_equal_and_have_iterable_elements_that_have_dictionaries_in_them_then_returns_false(self):
        d1 = (1,2,3,[4,5,{'a':11, 'b':4}])
        d2 = (1,2,3, [4,5,{'a':12, 'b':4}])
        self.assertFalse(deep_compare(d1, d2))

    def test_deep_compare_when_are_passed_iterable_objects_that_are_equal_and_have_iterable_elements_that_have_dictionaries_in_them_then_returns_true(self):
        d1 = (1,2,3,[4,5,{'a':12, 'b':4}])
        d2 = (1,2,3, [4,5,{'a':12, 'b':4}])
        self.assertTrue(deep_compare(d1, d2))

    def test_deep_compare_when_are_passed_equal_dictionaries_then_returns_true(self):
        data2 = copy.deepcopy(self.data)
        self.assertTrue(deep_compare(self.data, data2))

    def test_deep_compare_when_are_passed_equal_dictionaries_then_returns_true(self):
        data2 = {
            'key1': 'val1',
            'key2': 'val2',
            'key3': [{
                'inner_key1': 'val1',
                'inner_key2': 'val2'
            }, { 'inner_key3': 'val3',
                'inner_key4': 'val4'}],
            'key4':({
                'inner_key5': 'val5',
            }, {
                'inner_key66': 'val5',
            }),
            'key5':{
                'inner_key6': 'val6'
                },
            'inner_key1': 'bfs'
            }
        self.assertFalse(deep_compare(self.data, data2))


if __name__ == '__main__':
    unittest.main()