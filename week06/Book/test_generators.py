import unittest
import generators

class TestGenerators(unittest.TestCase):
    def test_chain_when_two_ranges_are_passed_then_returns_another_one_that_concatenate_the_two_iterables(self):
        expr1 = range(0,4)
        expr2 = range(4, 8)
        expected_result = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(list(generators.chain(expr1, expr2)), expected_result)

    def test_chain_when_one_range_and_one_list_are_passed_then_returns_another_one_that_concatenate_the_two_iterables(self):
        expr1 = range(0,4)
        expr2 = [4,5,6,7]
        expected_result = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(list(generators.chain(expr1, expr2)), expected_result)

    def test_chain_when_two_sets_are_passed_then_returns_another_one_that_concatenate_the_two_iterables(self):
        expr1 = {1,2,3,4}
        expr2 = {1,7,8}
        expected_result = [1, 2, 3, 4, 1, 7, 8]
        self.assertEqual(list(generators.chain(expr1, expr2)).sort(), expected_result.sort())


    def test_compress_that_takes_one_iterables_and_one_iterable_mask_and_returns_only_this_objects_from_first_collection_that_have_true_on_their_position_in_the_mask(self):
        expr = ["Ivo", "Rado", "Panda"]
        mask = [False, False, True]
        expected_result = ["Panda"]
        self.assertEqual(list(generators.compress(expr, mask)), expected_result)


if __name__ == '__main__':
    unittest.main()
