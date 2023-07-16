
# Doc Test
# python -m doctype one.py
# python -m doctype -v one.py

# """
# >>> add(2, 3)
# 5
# """


# def add(x, y):
#     """
#     >>> add(1, 2)
#     3
#     """
#     return x + y

# ----------------------------------------------------

"""
L 2
"""

# Unit Test
# python -m unittest test_one.py
# python -m unittest discover ( run all test_ in directory )

# def add(x, y):
#     return x + y
#
#
# def division(x, y):
#     if y == 0:
#         raise ZeroDivisionError('cant divide by zero !')
#     return x // y

# ----------------------------------------------------
"""
L 3
"""

# python -m unittest test_one.py


# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#
#     def fullname(self):
#         return f"{self.fname} {self.lname}"

# ----------------------------------------------------
"""
L 4
"""

# pip install nose
# nosetests (runs all test_.py files and test_ methods)
# nosetests test_one.py
# nosetests -v test_one.py


# def add(x, y):
#     return x + y
#
#
# def division(x, y):
#     if y == 0:
#         raise ZeroDivisionError('cant divide by zero !')
#     return x // y

# ----------------------------------------------------
"""
L 5
"""

# pip install pytest
# pytest (runs all test_.py files and test_ methods)
# pytest test_one.py
# pytest -v test_one.py
# it's ok with unittest codes


# def add(x, y):
#     return x + y
#
#
# def division(x, y):
#     if y == 0:
#         raise ZeroDivisionError('cant divide by zero !')
#     return x // y

# ----------------------------------------------------
"""
L 6
"""

# pytest test_one.py


# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#
#     def fullname(self):
#         return f"{self.fname} {self.lname}"

# ----------------------------------------------------
"""
L 7
"""

# pytest test_one.py
# pytest test_one.py --resultlog=result.log (creates a log of test)


# def add(x, y):
#     return x + y
#
#
# def division(x, y):
#     if y == 0:
#         raise ZeroDivisionError('cant divide by zero !')
#     return x // y

# ----------------------------------------------------
"""
L 8
"""
# from itertools import islice
# from functools import partial


# l = [1, 2, 3, 4, 5, 6, 7]


# def take(iterable, n):
#     return list(islice(iterable, n))


# def chunked(iterable, n, strict=False):
#     iterator = iter(partial(take, iter(iterable), n), [])
#     if strict:
#         if n is None:
#             raise ValueError('n cant be None when strict is True')
#
#         def ret():
#             for chunk in iterator:
#                 if len(chunk) != n:
#                     raise ValueError('iterator is not divisible by n')
#                 yield chunk
#         return iter(ret())
#     else:
#         return iterator

# ----------------------------------------------------
"""
L 9
"""
# _marker = object()


# def first(iterable, default=_marker):
#     try:
#         return next(iter(iterable))
#     except StopIteration as e:
#         if default is _marker:
#             raise ValueError('first() was called on an iterable,'
#                              ' and no default value was provided.') from e
#         return default

# ----------------------------------------------------
"""
L 10 & 11
"""
# from collections import deque
# from collections.abc import Sequence
# from itertools import islice
#
#
# _marker = object()
#
#
# def last(iterable, default=_marker):
#     try:
#         if isinstance(iterable, Sequence):
#             return iterable[-1]
#         elif hasattr(iterable, '__reversed__'):
#             return next(reversed(iterable))
#         else:
#             return deque(iterable, maxlen=1)[-1]
#     except (IndexError, TypeError, StopIteration):
#         if default is _marker:
#             raise ValueError(
#                 'last() was called on an empty iterable. and no default was provided.'
#             )
#         return default
#
#
# def nth_or_last(iterable, n, default=_marker):
#     return last(islice(iterable, n+1), default=default)

# ----------------------------------------------------
"""
l 12
"""


# def one(iterable, too_short=None, too_long=None):
#     it = iter(iterable)
#     try:
#         first_value = next(it)
#     except StopIteration as e:
#         raise (
#             too_short or ValueError('too few items in iterable (expected 1)')
#         ) from e
#
#     try:
#         second_value = next(it)
#     except StopIteration:
#         pass
#     else:
#         msg = (
#             'Expected exactly one item : but got {!r}, {!r}, '
#             'and perhaps more.'.format(first_value, second_value)
#         )
#         raise too_long or ValueError(msg)
#
#     return first_value

# ----------------------------------------------------
"""
l 13
"""

# from itertools import chain


# def interleave(*iterable):
#     return chain.from_iterable(zip(*iterable))

# ----------------------------------------------------
"""
l 14
"""

# from itertools import chain, repeat, islice


# def take(iterable, n):
#     return list(islice(iterable, n))


# def repeat_each(iterable, n=2):
#     return chain.from_iterable(map(repeat, iterable, repeat(n)))

# ----------------------------------------------------
"""
L 15
"""


# def raise_(exception, *args):
#     raise exception(*args)


# def strictly_n(iterable, n, too_short=None, too_long=None):
#     if too_short is None:
#         too_short = lambda item_count: raise_(
#             ValueError,
#             f'Too few items in iterable (got {item_count})'
#         )
#
#     if too_long is None:
#         too_long = lambda item_count: raise_(
#             ValueError,
#             f'Too many items in iterable (got at last {item_count})'
#         )
#
#     it = iter(iterable)
#     for i in range(n):
#         try:
#             item = next(it)
#         except StopIteration:
#             too_short(i)
#             return
#         else:
#             yield item
#
#     try:
#        next(it)
#     except StopIteration:
#         pass
#     else:
#         too_long(n+1)

# ----------------------------------------------------
"""
L 16
"""


# def only(iterable, default=None, too_long=None):
#     it = iter(iterable)
#     first_value = next(it, default)
#
#     try:
#         second_value = next(it)
#     except StopIteration:
#         pass
#     else:
#         msg = (
#             'Expected exacly one item in iterable, but got {}, {}, '
#             'and perhaps more.'.format(first_value, second_value)
#         )
#         raise too_long or ValueError(msg)
#     return first_value

# ----------------------------------------------------
"""
L 17
"""


# def always_reversible(iterable):
#     try:
#         return reversed(iterable)
#     except TypeError:
#         return reversed(list(iterable))

# ----------------------------------------------------
"""
L 18
"""


# def always_iterable(obj, base_type=(str, bytes)):
#     if obj is None:
#         return iter(())
#
#     if (base_type is not None) and isinstance(obj, base_type):
#         return iter((obj,))
#
#     try:
#         return iter(obj)
#     except TypeError:
#         return iter((obj,))

# ----------------------------------------------------
"""
L 19
"""


# def split_after(iterable, pred, max_split=-1):
#     if max_split == 0:
#         yield list(iterable)
#         return
#
#     buf = []
#     it = iter(iterable)
#     for item in it:
#         buf.append(item)
#         if pred(item) and buf:
#             yield buf
#             if max_split == 1:
#                 yield list(it)
#                 return
#             buf = []
#             max_split -= 1
#     if buf:
#         yield buf

# ----------------------------------------------------
"""
L 20
"""
# from itertools import islice


# def split_into(iterable, sizes):
#     it = iter(iterable)
#     for size in sizes:
#         if size is None:
#             yield list(it)
#             return
#         else:
#             yield list(islice(it, size))

# ----------------------------------------------------
"""
L 21
"""


# def map_if(iterable, pred, func, func_else=lambda x: x):
#     for item in iterable:
#         yield func(item) if pred(item) else func_else(item)

# ----------------------------------------------------
"""
L 22
"""
# from time import monotonic


# class time_limited:
#     def __init__(self, limit_seconds, iterable):
#         if limit_seconds < 0:
#             raise ValueError('limit_second must be positive')
#         self.limit_seconds = limit_seconds
#         self._iterable = iter(iterable)
#         self._start_time = monotonic()
#         self.timed_out = False
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         item = next(self._iterable)
#         if monotonic() - self._start_time > self.limit_seconds:
#             self.timed_out = True
#             raise StopIteration
#         return item

# ----------------------------------------------------
"""
L 23
"""
# from operator import sub
# from itertools import tee, chain, starmap


# def difference(iterable, func=sub, *, initial=None):
#     a, b = tee(iterable)
#
#     try:
#         first = [next(b)]
#     except StopIteration:
#         return iter([])
#
#     if initial is not None:
#         first = []
#
#     # (zip b and a) then (sending to starmap fanc) and (chaining with first)
#     return chain(first, starmap(func, zip(b, a)))

# ----------------------------------------------------
"""
L 24
"""


# def value_chain(*args):
#     for value in args:
#         if isinstance(value, (str, bytes)):
#             yield value
#             continue
#         try:
#             yield from value
#         except TypeError:
#             yield value

# ----------------------------------------------------
"""
L 25
"""
# from collections.abc import Sequence


# class SequenceView(Sequence):
#     def __init__(self, target):
#         if not isinstance(target, Sequence):
#             raise TypeError
#         self._target = target
#
#     def __getitem__(self, index):
#         return self._target[index]
#
#     def __len__(self):
#         return len(self._target)
#
#     def __repr__(self):
#         return f'{self.__class__.__name__}({self._target})'

# ----------------------------------------------------
