
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


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def fullname(self):
        return f"{self.fname} {self.lname}"


# ----------------------------------------------------
