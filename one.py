
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
from itertools import islice
from functools import partial


l = [1, 2, 3, 4, 5, 6, 7]


def take(iterable, n):
    return list(islice(iterable, n))


def chunked(iterable, n, strict=False):
    iterator = iter(partial(take, iter(iterable), n), [])
    if strict:
        if n is None:
            raise ValueError('n cant be None when strict is True')

        def ret():
            for chunk in iterator:
                if len(chunk) != n:
                    raise ValueError('iterator is not divisible by n')
                yield chunk
        return iter(ret())
    else:
        return iterator

# ----------------------------------------------------
