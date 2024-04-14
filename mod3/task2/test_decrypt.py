import unittest
from mod2.task3 import decrypt

class TestDecrypt(unittest.TestCase):
    def test_no_dots(self):
        self.assertEqual(decrypt("абра-кадабра."), "абра-кадабра")

    def test_one_dot(self):
        self.assertEqual(decrypt("абраа..-кадабра"), "абра-кадабра")

    def test_two_dots(self):
        self.assertEqual(decrypt("абраа..-.кадабра"), "абра-кадабра")

    def test_three_dots(self):
        self.assertEqual(decrypt("абра--..кадабра"), "абра-кадабра")

    def test_more_dots(self):
        self.assertEqual(decrypt("абрау...-кадабра"), "абра-кадабра")

    def test_all_dots(self):
        self.assertEqual(decrypt("абра........"), "")

    def test_last_dot(self):
        self.assertEqual(decrypt("абр......a."), "a")

    def test_digits_dots(self):
        self.assertEqual(decrypt("1..2.3"), "23")

    def test_only_dot(self):
        self.assertEqual(decrypt("."), "")

    def test_only_digits_dots(self):
        self.assertEqual(decrypt("1......................."), "")


