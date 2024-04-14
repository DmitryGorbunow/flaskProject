import unittest
from mod2.task4 import app, get_weekday_name
from freezegun import freeze_time
from datetime import datetime

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        app.config[' TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello_world/'

    def test_can_get_correct_max_number_in_series_of_two(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    @freeze_time("2024-04-09")
    def test_correct_weekday_returned(self):
        username = 'Хорошей среды'
        expected_weekday_name = "Привет, Хорошей среды, хорошего вторника!"
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(expected_weekday_name in response_text)