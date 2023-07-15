import unittest
import pytest
import one

"""
L 2
"""
# class OneTest(unittest.TestCase):
#     # func name must starts with 'test_'
#     def test_add(self):
#         self.assertEqual(one.add(1, 2), 3)
#         self.assertEqual(one.add(-2, 3), 1)
#
#     def test_division(self):
#         self.assertEqual(one.division(10, 2), 5)
#         self.assertRaises(ZeroDivisionError, one.division, 5, 0)


# ----------------------------------------------------
"""
L 3
"""


# class PersonTest(unittest.TestCase):
#     # before start testing
#     def setUp(self):
#         self.p1 = one.Person('erfan', 'safarzad')
#
#     # after testing done
#     def tearDown(self):
#         print('Done..')
#
#     def test_fullname(self):
#         self.assertEqual(self.p1.fullname(), 'erfan safarzad')

# ----------------------------------------------------
"""
L 4
"""


# def test_add():
#     assert one.add(1, 2) == 3
#     assert one.add(-1, 2) == 1
#
#
# def test_division():
#     assert one.division(10, 2) == 5

# ----------------------------------------------------
"""
L 5
"""
# it can be method or class


# def test_add():
#     assert one.add(1, 2) == 3
#     assert one.add(-1, 2) == 1
#
#
# class TestOne:
#     def test_add(self):
#         assert one.add(1, 2) == 3
#         assert one.add(-1, 2) == 1
#
#     def test_division(self):
#         assert one.division(10, 2) == 5

# ----------------------------------------------------
"""
L 6
"""
# import time


# # class name most start with 'Test'
# class TestPerson:
#     # before start testing
#     @pytest.fixture
#     def setup(self):
#         self.p1 = one.Person('erfan', 'safarzad')
#         yield 'setup'
#         # after yield teardown running
#         # print was not working
#         time.sleep(2)
#
#     def test_fullname(self, setup):
#         assert self.p1.fullname() == 'erfan safarzad'

# ----------------------------------------------------
"""
L 7
"""


# class TestOne:
#     def test_add(self):
#         assert one.add(1, 2) == 3
#         assert one.add(-1, 2) == 1
#
#     def test_division(self):
#         assert one.division(10, 2) == 5
#         with pytest.raises(ZeroDivisionError):
#             one.division(2, 0)

# ----------------------------------------------------
"""
L 8
"""


# class TakeTests(unittest.TestCase):
#     def test_simple_take(self):
#         t = one.take(range(10), 5)
#         self.assertEqual(t, [0, 1, 2, 3, 4])
#
#     def test_null_take(self):
#         t = one.take(range(10), 0)
#         self.assertEqual(t, [])
#
#     def test_take_too_much(self):
#         t = one.take(range(5), 10)
#         self.assertEqual(t, [0, 1, 2, 3, 4])
#
#     def test_negative_take(self):
#         self.assertRaises(ValueError, lambda: one.take(range(10), -3))
#
#
# class ChunkedTests(unittest.TestCase):
#     def test_even(self):
#         self.assertEqual(
#             list(one.chunked('abcdef', 3)),
#             [['a', 'b', 'c'], ['d', 'e', 'f']]
#         )
#
#     def test_odd(self):
#         self.assertEqual(
#             list(one.chunked('abcde', 3)),
#             [['a', 'b', 'c'], ['d', 'e']]
#         )
#
#     def test_none(self):
#         self.assertEqual(
#             list(one.chunked('abcdef', None)),
#             [['a', 'b', 'c', 'd', 'e', 'f']]
#         )
#
#     def test_strict_false(self):
#         self.assertEqual(
#             list(one.chunked('abcde', 3, strict=False)),
#             [['a', 'b', 'c'], ['d', 'e']]
#         )
#
#     def test_strict_true(self):
#
#         def f():
#             return list(one.chunked('abcde', 3, strict=True))
#
#         self.assertRaisesRegex(ValueError, 'iterator is not divisible by n', f)
#
#         self.assertEqual(
#             list(one.chunked('abcdef', 3, strict=True)),
#             [['a', 'b', 'c'], ['d', 'e', 'f']]
#         )
#
#     def test_strict_true_size_none(self):
#
#         def f():
#             return list(one.chunked('abcde', None, strict=True))
#
#         self.assertRaisesRegex(ValueError, 'n cant be None when strict is True', f)

# ----------------------------------------------------
"""
L 9
"""
# import traceback


# class FirstTest(unittest.TestCase):
#     def test_many(self):
#         self.assertEqual(one.first(x for x in range(4)), 0)
#
#     def test_one(self):
#         self.assertEqual(one.first([3]), 3)
#
#     def test_default(self):
#         self.assertEqual(one.first([], 'abc'), 'abc')
#
#     def test_empty_stop_iteration(self):
#         try:
#             one.first([])
#         except ValueError:
#             formatted_exec = traceback.format_exc()
#             self.assertIn('StopIteration', formatted_exec)
#             self.assertIn('The above exception was the direct cause', formatted_exec)
#         else:
#             self.fail()

# ----------------------------------------------------
"""
L 10
"""


class LastTest(unittest.TestCase):
    def test_basic(self):
        cases = [
            (range(4), 3),
            (iter(range(4)), 3),
            (range(1), 0),
            (iter(range(1)), 0),
            ({n: str(n) for n in range(5)}, 4)
        ]

        for iterable, expected in cases:
            with self.subTest(iterable=iterable):
                self.assertEqual(one.last(iterable), expected)

    def test_default(self):
        for iterable, default, expected in [
            (range(1), None, 0),
            ([], None, None),
            ({}, None, None),
            (iter([]), None, None)
        ]:
            with self.subTest(args=(iterable, default)):
                self.assertEqual(one.last(iterable, default=default), expected)

    def test_empty(self):
        for iterable in ([], iter(range(0))):
            with self.subTest(iterable=iterable):
                with self.assertRaises(ValueError):
                    one.last(iterable)

# ----------------------------------------------------


# ----------------------------------------------------

if __name__ == '__main__':
    unittest.main()

# ----------------------------------------------------
