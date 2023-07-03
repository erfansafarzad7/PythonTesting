import unittest
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


class PersonTest(unittest.TestCase):
    # before start testing
    def setUp(self):
        self.p1 = one.Person('erfan', 'safarzad')

    # after testing done
    def tearDown(self):
        print('Done..')

    def test_fullname(self):
        self.assertEqual(self.p1.fullname(), 'erfan safarzad')

# ----------------------------------------------------


# ----------------------------------------------------

if __name__ == '__main__':
    unittest.main()

# ----------------------------------------------------
