import unittest
import one


class OneTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(one.add(1, 2), 3)
        self.assertEqual(one.add(-2, 3), 1)

    def test_division(self):
        self.assertEqual(one.division(10, 2), 5)
        self.assertRaises(ZeroDivisionError, one.division, 5, 0)


if __name__ == '__main__':
    unittest.main()
