import unittest

from mod3.task4.person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('Dmitry', 1995, 'les')

    def test_get_name(self):
        result = self.person.get_name()
        self.assertEqual('Dmitry', result)

    def test_get_address(self):
        result = self.person.get_address()
        self.assertEqual('les', result)

    def test_set_name(self):
        self.person.set_name("Dima")
        self.assertEqual("Dima", self.person.get_name())

    def test_set_address(self):
        self.person.set_address("new address")
        self.assertEqual("new_address", self.person.get_address())

    def test_is_homeless(self):
        result = self.person.is_homeless()
        self.assertEqual(False, result)

    def test_get_age(self):
        result = self.person.get_age()
        self.assertEqual(29, result)