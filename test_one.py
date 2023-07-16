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


# class FirstTests(unittest.TestCase):
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
L 10 & 11
"""


# class LastTests(unittest.TestCase):
#     def test_basic(self):
#         cases = [
#             (range(4), 3),
#             (iter(range(4)), 3),
#             (range(1), 0),
#             (iter(range(1)), 0),
#             ({n: str(n) for n in range(5)}, 4)
#         ]
#
#         for iterable, expected in cases:
#             with self.subTest(iterable=iterable):
#                 self.assertEqual(one.last(iterable), expected)
#
#     def test_default(self):
#         for iterable, default, expected in [
#             (range(1), None, 0),
#             ([], None, None),
#             ({}, None, None),
#             (iter([]), None, None)
#         ]:
#             with self.subTest(args=(iterable, default)):
#                 self.assertEqual(one.last(iterable, default=default), expected)
#
#     def test_empty(self):
#         for iterable in ([], iter(range(0))):
#             with self.subTest(iterable=iterable):
#                 with self.assertRaises(ValueError):
#                     one.last(iterable)
#
#
# class NthOrLastTest(unittest.TestCase):
#     def test_basic(self):
#         self.assertEqual(one.nth_or_last(range(3), 1), 1)
#         self.assertEqual(one.nth_or_last(range(3), 3), 2)
#
#     def test_default_value(self):
#         default = 43
#         self.assertEqual(one.nth_or_last(range(0), 3, default), default)
#
#     def test_empty_iterable_no_default(self):
#         self.assertRaises(ValueError, lambda: one.nth_or_last(range(0), 0))


# ----------------------------------------------------
"""
l 12
"""
# import traceback
# from itertools import count


# class OneTests(unittest.TestCase):
#     def test_basic(self):
#         it = ['item']
#         self.assertEqual(one.one(it), 'item')
#
#     def test_too_short(self):
#         it = []
#         for too_short, exc_type in [
#             (None, ValueError),
#             (IndexError, IndexError)
#         ]:
#             with self.subTest(too_short=too_short):
#                 try:
#                     one.one(it, too_short=too_short)
#                 except exc_type:
#                     formatted_exc = traceback.format_exc()
#                     self.assertIn('StopIteration', formatted_exc)
#                     self.assertIn('The above exception was the direct cause', formatted_exc)
#                 else:
#                     self.fail()
#
#     def test_too_long(self):
#         it = count()
#         self.assertRaises(ValueError, lambda: one.one(it))
#         self.assertEqual(next(it), 2)
#         self.assertRaises(
#             OverflowError, lambda: one.one(it, too_long=OverflowError)
#         )
#
#     def test_too_long_default_message(self):
#         it = count()
#         self.assertRaisesRegex(
#             ValueError,
#             'Expected exactly one item : but got 0, 1, and perhaps more.',
#             lambda: one.one(it)
#         )

# ----------------------------------------------------
"""
l 13
"""
# from itertools import count


# class InterleaveTests(unittest.TestCase):
#     def test_even(self):
#         actual = list(one.interleave([1, 4, 7], [2, 5, 8], [3, 6, 9]))
#         expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         self.assertEqual(actual, expected)
#
#     def test_short(self):
#         actual = list(one.interleave([1, 4], [2, 5, 8], [3, 6, 9]))
#         expected = [1, 2, 3, 4, 5, 6]
#         self.assertEqual(actual, expected)
#
#     def test_mixed_types(self):
#         it_list = ['a', 'b', 'c', 'd']
#         it_str = '123456'
#         it_int = count()
#         actual = list(one.interleave(it_list, it_str, it_int))
#         expected = ['a', '1', 0, 'b', '2', 1, 'c', '3', 2, 'd', '4', 3]
#         self.assertEqual(actual, expected)

# ----------------------------------------------------
"""
l 14
"""
# from itertools import cycle


# class RepeatEachTests(unittest.TestCase):
#     def test_default(self):
#         actual = list(one.repeat_each('abc'))
#         expected = ['a', 'a', 'b', 'b', 'c', 'c']
#         self.assertEqual(actual, expected)
#
#     def test_basic(self):
#         actual = list(one.repeat_each('abc', 3))
#         expected = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']
#         self.assertEqual(actual, expected)
#
#     def test_empty(self):
#         actual = list(one.repeat_each(''))
#         expected = []
#         self.assertEqual(actual, expected)
#
#     def test_no_repeat(self):
#         actual = list(one.repeat_each('abc', 0))
#         expected = []
#         self.assertEqual(actual, expected)
#
#     def test_negative_repeat(self):
#         actual = list(one.repeat_each('abc', -1))
#         expected = []
#         self.assertEqual(actual, expected)
#
#     def test_infinite_input(self):
#         repeater = one.repeat_each(cycle('ab'))
#         actual = one.take(repeater, 6)
#         expected = ['a', 'a', 'b', 'b', 'a', 'a']
#         self.assertEqual(actual, expected)

# ----------------------------------------------------
"""
L 15
"""


# class StrictlyNTests(unittest.TestCase):
#     def test_basic(self):
#         iterable = ['a', 'b', 'c', 'd']
#         n = 4
#         actual = list(one.strictly_n(iterable, n))
#         expected = iterable
#         self.assertEqual(actual, expected)
#
#     def test_too_short_default(self):
#         iterable = ['a', 'b', 'c', 'd']
#         n = 5
#
#         with self.assertRaises(ValueError) as exc:
#             list(one.strictly_n(iterable, n))
#
#         self.assertEqual(
#             'Too few items in iterable (got 4)', exc.exception.args[0]
#         )
#
#     def test_too_long_default(self):
#         iterable = ['a', 'b', 'c', 'd']
#         n = 3
#
#         with self.assertRaises(ValueError) as exc:
#             list(one.strictly_n(iterable, n))
#
#         self.assertEqual(
#             'Too many items in iterable (got at last 4)', exc.exception.args[0]
#         )
#
#     def test_too_short_custom(self):
#         call_count = 0
#
#         def too_short(item_count):
#             nonlocal call_count
#             call_count += 1
#
#         iterable = ['a', 'b', 'c', 'd']
#         n = 6
#         actual = []
#
#         for item in one.strictly_n(iterable, n, too_short=too_short):
#             actual.append(item)
#
#         expected = ['a', 'b', 'c', 'd']
#         self.assertEqual(actual, expected)
#         self.assertEqual(call_count, 1)
#
#     def test_too_long_custom(self):
#         import logging
#
#         iterable = ['a', 'b', 'c', 'd']
#         n = 2
#         too_long = lambda item_count: logging.warning(
#             f'Picked the first {n} item'
#         )
#
#         with self.assertLogs(level='WARNING') as exc:
#             actual = list(one.strictly_n(iterable, n, too_long=too_long))
#
#         self.assertEqual(actual, ['a', 'b'])
#         self.assertIn('Picked the first 2 item', exc.output[0])

# ----------------------------------------------------
"""
L 16
"""


# class OnlyTests(unittest.TestCase):
#     def test_default(self):
#         self.assertEqual(one.only([]), None)
#         self.assertEqual(one.only([1]), 1)
#         self.assertRaises(ValueError, lambda: one.only([1, 2]))
#
#     def test_custom_value(self):
#         self.assertEqual(one.only([], default='!'), '!')
#         self.assertEqual(one.only([1], default='!'), 1)
#         self.assertRaises(ValueError, lambda: one.only([1, 2], default='!'))
#
#     def test_custom_exception(self):
#         self.assertEqual(one.only([], too_long=RuntimeError), None)
#         self.assertEqual(one.only([1], too_long=RuntimeError), 1)
#         self.assertRaises(RuntimeError, lambda: one.only([1, 2], too_long=RuntimeError))
#
#     def test_default_exception_message(self):
#         self.assertRaisesRegex(
#             ValueError,
#             "Expected exacly one item in iterable, but got foo, bar, "
#             "and perhaps more.",
#             lambda: one.only(['foo', 'bar', 'baz'])
#         )


# ----------------------------------------------------
"""
L 17
"""


# class AlwaysReversibleTests(unittest.TestCase):
#     def test_regular_reversed(self):
#         self.assertEqual(
#             list(reversed(range(10))), list(one.always_reversible(range(10)))
#         )
#
#         self.assertEqual(
#             reversed([1, 2, 3]).__class__, one.always_reversible([1, 2, 3]).__class__
#         )
#
#     def test_nonseq_reversed(self):
#         self.assertEqual(
#             list(reversed(range(10))), list(one.always_reversible(x for x in range(10)))
#         )
#
#         self.assertNotEqual(
#             reversed((1, 2)).__class__, one.always_reversible(x for x in (1, 2)).__class__
#         )


# ----------------------------------------------------
"""
L 18
"""


# class AlwaysIterableTests(unittest.TestCase):
#     def test_single(self):
#         self.assertEqual(list(one.always_iterable(1)), [1])
#
#     def test_string(self):
#         for obj in ['foo', b'bar', 'baz']:
#             actual = list(one.always_iterable(obj))
#             expected = [obj]
#             self.assertEqual(actual, expected)
#
#     def test_base_type(self):
#         dict_obj = {'a': 1, 'b': 2}
#         str_obj = '123'
#
#         default_actual = list(one.always_iterable(dict_obj))
#         default_expected = list(dict_obj)
#         self.assertEqual(default_actual, default_expected)
#
#         custom_actual = list(one.always_iterable(dict_obj, base_type=dict))
#         custom_expected = [dict_obj]
#         self.assertEqual(custom_actual, custom_expected)
#
#         str_actual = list(one.always_iterable(str_obj, base_type=None))
#         str_expected = list(str_obj)
#         self.assertEqual(str_actual, str_expected)
#
#         base_type = ((dict,),)
#         custom_actual = list(one.always_iterable(dict_obj, base_type=base_type))
#         custom_expected = [dict_obj]
#         self.assertEqual(custom_actual, custom_expected)
#
#     def test_iterables(self):
#         self.assertEqual(list(one.always_iterable([0, 1])), [0, 1])
#         self.assertEqual(list(one.always_iterable([0, 1], base_type=list)), [[0, 1]])
#         self.assertEqual(list(one.always_iterable(iter('foo'))), ['f', 'o', 'o'])
#         self.assertEqual(list(one.always_iterable([])), [])
#
#     def test_none(self):
#         self.assertEqual(list(one.always_iterable(None)), [])
#
#     def test_generator(self):
#         def _gen():
#             yield 0
#             yield 1
#
#         self.assertEqual(list(one.always_iterable(_gen())), [0, 1])


# ----------------------------------------------------
"""
L 19
"""


# class SplitAfterTests(unittest.TestCase):
#
#     def test_start_with_sep(self):
#         actual = list(one.split_after('xooxoo', lambda c: c == 'x'))
#         expected = [['x'], ['o', 'o', 'x'], ['o', 'o']]
#         self.assertEqual(actual, expected)
#
#     def test_ends_with_sep(self):
#         actual = list(one.split_after('ooxoox', lambda c: c == 'x'))
#         expected = [['o', 'o', 'x'], ['o', 'o', 'x']]
#         self.assertEqual(actual, expected)
#
#     def test_no_sep(self):
#         actual = list(one.split_after('ooo', lambda c: c == 'x'))
#         expected = [['o', 'o', 'o']]
#         self.assertEqual(actual, expected)
#
#     def test_max_split(self):
#         for args, expected in [
#             (
#                     ('a,b,c,d', lambda c: c == ',', -1),
#                     [['a', ','], ['b', ','], ['c', ','], ['d']]
#             ),
#             (
#                     ('a,b,c,d', lambda c: c == ',', 0),
#                     [['a', ',', 'b', ',', 'c', ',', 'd']]
#             ),
#             (
#                     ('a,b,c,d', lambda c: c == ',', 1),
#                     [['a', ','], ['b', ',', 'c', ',', 'd']]
#             ),
#             (
#                     ('a,b,c,d', lambda c: c == ',', 2),
#                     [['a', ','], ['b', ','], ['c', ',', 'd']]
#             ),
#             (
#                     ('a,b,c,d', lambda c: c == ',', 10),
#                     [['a', ','], ['b', ','], ['c', ','], ['d']]
#             ),
#             (
#                     ('a,b,c,d', lambda c: c == '@', 2),
#                     [['a', ',', 'b', ',', 'c', ',', 'd']]
#             ),
#             (
#                     ('a,b,c,d', lambda c: c != ',', 2),
#                     [['a'], [',', 'b'], [',', 'c', ',', 'd']]
#             ),
#         ]:
#             actual = list(one.split_after(*args))
#             self.assertEqual(actual, expected)

# ----------------------------------------------------
"""
L 20
"""


# class SplitIntoTest(unittest.TestCase):
#     def test_iterable_just_right(self):
#         iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         sizes = [2, 3, 4]
#         expected = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
#         actual = list(one.split_into(iterable, sizes))
#         self.assertEqual(actual, expected)
#
#     def test_iterable_too_small(self):
#         iterable = [1, 2, 3, 4, 5, 6, 7]
#         sizes = [2, 3, 4]
#         expected = [[1, 2], [3, 4, 5], [6, 7]]
#         actual = list(one.split_into(iterable, sizes))
#         self.assertEqual(actual, expected)
#
#     def test_iterable_too_small_extra(self):
#         iterable = [1, 2, 3, 4, 5, 6, 7]
#         sizes = [2, 3, 4, 5]
#         expected = [[1, 2], [3, 4, 5], [6, 7], []]
#         actual = list(one.split_into(iterable, sizes))
#         self.assertEqual(actual, expected)
#
#     def test_iterable_too_large(self):
#         iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         sizes = [2, 3, 2]
#         expected = [[1, 2], [3, 4, 5], [6, 7]]
#         actual = list(one.split_into(iterable, sizes))
#         self.assertEqual(actual, expected)
#
#     def test_using_none_with_leftover(self):
#         iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         sizes = [2, 3, None]
#         expected = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
#         actual = list(one.split_into(iterable, sizes))
#         self.assertEqual(actual, expected)
#
#     def test_using_none_mid_sizes(self):
#         iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         sizes = [2, 3, None, 4]
#         expected = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
#         actual = list(one.split_into(iterable, sizes))
#         self.assertEqual(actual, expected)
#
#     def test_iterable_empty(self):
#         iterable = []
#         sizes = [2, 3, 4]
#         expected = [[], [], []]
#         actual = list(one.split_into(iterable, sizes))
#         self.assertEqual(actual, expected)
#
#     def test_iterable_empty_using_none(self):
#         iterable = []
#         sizes = [2, 3, None, 4]
#         expected = [[], [], []]
#         actual = list(one.split_into(iterable, sizes))
#         self.assertEqual(actual, expected)
#
#     def test_sizes_empty(self):
#         iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         sizes = []
#         expected = []
#         actual = list(one.split_into(iterable, sizes))
#         self.assertEqual(actual, expected)
#
#     def test_both_empty(self):
#         iterable = []
#         sizes = []
#         expected = []
#         actual = list(one.split_into(iterable, sizes))
#         self.assertEqual(actual, expected)
#
#     def test_bool_in_sizes(self):
#         iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         sizes = [3, True, 2, False]
#         expected = [[1, 2, 3], [4], [5, 6], []]
#         actual = list(one.split_into(iterable, sizes))
#         self.assertEqual(actual, expected)
#
#     def test_invalid_in_sizes(self):
#         iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         sizes = [1, [], 3]
#         expected = [[1, 2, 3], [4], [5, 6], []]
#         with self.assertRaises(ValueError):
#             list(one.split_into(iterable, sizes))
#
#     def test_invalid_in_sizes_after_none(self):
#         iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         sizes = [3, 4, None, []]
#         expected = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
#         actual = list(one.split_into(iterable, sizes))
#         self.assertEqual(actual, expected)
#
#     def test_generator_iterable_integrity(self):
#         iterable = (i for i in range(10))
#         sizes = [2, 3]
#         expected = [[0, 1], [2, 3, 4]]
#         actual = list(one.split_into(iterable, sizes))
#         self.assertEqual(actual, expected)
#
#         iterable_expected = [5, 6, 7, 8, 9]
#         iterable_actual = list(iterable)
#         self.assertEqual(iterable_actual, iterable_expected)
#
#     def test_generator_sizes_integrity(self):
#         iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         sizes = (i for i in [1, 2, None, 3, 4])
#         expected = [[1], [2, 3], [4, 5, 6, 7, 8, 9]]
#         actual = list(one.split_into(iterable, sizes))
#         self.assertEqual(actual, expected)
#
#         sizes_expected = [3, 4]
#         sizes_actual = list(sizes)
#         self.assertEqual(sizes_actual, sizes_expected)

# ----------------------------------------------------
"""
L 21
"""


# class MapIfTests(unittest.TestCase):
#     def test_without_func_else(self):
#         iterable = list(range(-5, 5))
#         actual = list(one.map_if(iterable, lambda x: x > 3, lambda x: 'toobig'))
#         expected = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 'toobig']
#         self.assertEqual(actual, expected)
#
#     def test_with_func_else(self):
#         iterable = list(range(-5, 5))
#         actual = list(one.map_if(iterable, lambda x: x >= 0, lambda x: 'notneg', lambda x: 'neg'))
#         expected = ['neg'] * 5 + ['notneg'] * 5
#         self.assertEqual(actual, expected)
#
#     def test_empty(self):
#         actual = list(one.map_if([], lambda x: len(x) > 5, lambda x: None))
#         expected = []
#         self.assertEqual(actual, expected)

# ----------------------------------------------------
"""
L 22
"""
# from time import sleep
# from itertools import count


# class TimeLimitedTest(unittest.TestCase):
#     def test_basic(self):
#         def generator():
#             yield 1
#             yield 2
#             sleep(0.2)
#             yield 3
#
#         iterable = one.time_limited(0.1, generator())
#         actual = list(iterable)
#         expected = [1, 2]
#         self.assertEqual(actual, expected)
#         self.assertTrue(iterable.timed_out)
#
#     def test_complete(self):
#         iterable = one.time_limited(2, iter(range(10)))
#         actual = list(iterable)
#         expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#         self.assertEqual(actual, expected)
#         self.assertFalse(iterable.timed_out)
#
#     def test_zero_limit(self):
#         iterable = one.time_limited(0, [1, 2, 3, 4])
#         actual = list(iterable)
#         expected = []
#         self.assertEqual(actual, expected)
#         self.assertTrue(iterable.timed_out)
#
#     def test_invalid_limit(self):
#         with self.assertRaises(ValueError):
#             list(one.time_limited(-0.1, count()))


# ----------------------------------------------------
"""
L 23
"""
# from unittest import skipIf
# from itertools import accumulate
# from operator import add
# from sys import version_info


# class DifferenceTests(unittest.TestCase):
#     def test_normal(self):
#         iterable = [10, 20, 30, 40, 50]
#         actual = list(one.difference(iterable))
#         expected = [10, 10, 10, 10, 10]
#         self.assertEqual(actual, expected)
#
#     def test_custom(self):
#         iterable = [10, 20, 30, 40, 50]
#         actual = list(one.difference(iterable, add))
#         expected = [10, 30, 50, 70, 90]
#         self.assertEqual(actual, expected)
#
#     def test_roundtrip(self):
#         original = list(range(100))
#         accumulated = accumulate(original)
#         actual = list(one.difference(accumulated))
#         self.assertEqual(actual, original)
#
#     def test_one(self):
#         self.assertEqual(list(one.difference([0])), [0])
#
#     def test_empty(self):
#         self.assertEqual(list(one.difference([])), [])
#
#     @skipIf(version_info[:2] < (3, 8), 'accumulate with initial needs +3.8')
#     def test_initial(self):
#         original = list(range(100))
#         accumulated = accumulate(original, initial=100)
#         actual = list(one.difference(accumulated, initial=100))
#         self.assertEqual(actual, original)

# ----------------------------------------------------
"""
L 24
"""


# class ValueChainTests(unittest.TestCase):
#     def test_empty(self):
#         actual = list(one.value_chain())
#         expected = []
#         self.assertEqual(actual, expected)
#
#     def test_simple(self):
#         actual = list(one.value_chain(1, 2.17, False, 'foo'))
#         expected = [1, 2.17, False, 'foo']
#         self.assertEqual(actual, expected)
#
#     def test_more(self):
#         actual = list(one.value_chain(b'bar', [1, 2, 3], 4, {'key': 1}))
#         expected = [b'bar', 1, 2, 3, 4, 'key']
#         self.assertEqual(actual, expected)
#
#     def test_empty_lists(self):
#         actual = list(one.value_chain(1, 2, [], [3, 4]))
#         expected = [1, 2, 3, 4]
#         self.assertEqual(actual, expected)
#
#     def test_complex(self):
#         obj = object()
#         actual = list(
#             one.value_chain(
#                 (1, (2, (3,))),
#                 ['foo', ['bar', ['baz']], 'tic'],
#                 {'key': {'foo': 1}},
#                 obj,
#             )
#         )
#
#         expected = [1, (2, (3, )), 'foo', ['bar', ['baz']], 'tic', 'key', obj]
#         self.assertEqual(actual, expected)
# ----------------------------------------------------
"""
L 25
"""


# class SequenceViewTests(unittest.TestCase):
#
#     def test_init(self):
#         view = one.SequenceView((1, 2, 3))
#         self.assertEqual(repr(view), 'SequenceView((1, 2, 3))')
#         self.assertRaises(TypeError, lambda: one.SequenceView({}))
#
#     def test_update(self):
#         seq = [1, 2, 3]
#         view = one.SequenceView(seq)
#         self.assertEqual(len(view), 3)
#         self.assertEqual(repr(view), 'SequenceView([1, 2, 3])')
#
#         seq.pop()
#         self.assertEqual(len(view), 2)
#         self.assertEqual(repr(view), 'SequenceView([1, 2])')
#
#     def test_indexing(self):
#         seq = ('a', 'b', 'c', 'd', 'e', 'f')
#         view = one.SequenceView(seq)
#         for i in range(-len(seq), len(seq)):
#             self.assertEqual(view[i], seq[i])
#
#     def test_abc_methods(self):
#         seq = ('a', 'b', 'c', 'd', 'e', 'f', 'f')
#         view = one.SequenceView(seq)
#
#         self.assertIn('b', view)
#         self.assertNotIn('g', view)
#         self.assertEqual(list(iter(view)), list(seq))
#         self.assertEqual(list(reversed(view)), list(reversed(seq)))
#         self.assertEqual(view.index('b'), 1)
#         self.assertEqual(view.count('f'), 2)

# ----------------------------------------------------

if __name__ == '__main__':
    unittest.main()

# ----------------------------------------------------
