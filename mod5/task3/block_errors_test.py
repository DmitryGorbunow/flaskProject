import unittest
from mod5.task3.block_errors import BlockErrors


class TestBlockErrors(unittest.TestCase):
    def test_no_error(self):
        err_types = {ZeroDivisionError, TypeError}
        with BlockErrors(err_types):
            result = 1 / 2
        self.assertEqual(result, 0.5, "Expected division result")

    def test_ignored_error(self):
        err_types = {ZeroDivisionError, TypeError}
        with BlockErrors(err_types):
            result = 1 / 0
        self.assertTrue(result is None, "Expected None due to error being ignored")

    def test_unhandled_error(self):
        err_types = {TypeError}
        with self.assertRaises(ZeroDivisionError):
            with BlockErrors(err_types):
                result = 1 / 0


if __name__ == '__main__':
    unittest.main()
