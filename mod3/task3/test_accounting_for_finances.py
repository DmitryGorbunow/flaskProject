import unittest
from mod2.task7 import app, expenses


class TestExpenseApp(unittest.TestCase):
    def setUp(self):
        app.config[' TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        expenses[2024] = {4: 500}

    def test_add_expense(self):
        expected = "Расход в размере 437 рублей на дату 20240404 добавлен успешно."
        response = self.app.get('/add/20240404/437')
        self.assertEqual(response.status_code, 200)
        response_text = response.data.decode()
        self.assertEqual(expected, response_text)

    def test_calculate_by_year(self):
        expected = 'Суммарные траты за 2024 год: 500 рублей.'
        response = self.app.get('/calculate/2024')
        self.assertEqual(expected, response.data.decode())

    def test_calculate_by_not_filled_year(self):
        expected = 'Суммарные траты за 2023 год: 0 рублей.'
        response = self.app.get('/calculate/2023')
        self.assertEqual(expected, response.data.decode())

    def test_calculate_by_invalid_year(self):
        response = self.app.get('/calculate/year')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Not Found", response.data)

    def test_calculate_by_year_and_month(self):
        expected = 'Суммарные траты за 4/2024: 500 рублей.'
        response = self.app.get('/calculate/2024/04')
        self.assertEqual(expected, response.data.decode())

    def test_calculate_by_year_and_not_filled_month(self):
        expected = 'Суммарные траты за 3/2024: 0 рублей.'
        response = self.app.get('/calculate/2024/03')
        self.assertEqual(expected, response.data.decode())

    def test_calculate_by_invalid_year_and_month(self):
        response = self.app.get('/calculate/year/month')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Not Found", response.data)

    def test_add_throw_error_on_invalid_date(self):
        response = self.app.get('/add/2024/437')
        self.assertEqual(response.status_code, 500)
        self.assertIn(b"Internal Server Error", response.data)

    def test_add_throw_error_on_empty_amount(self):
        response = self.app.get('/add/20240404')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Not Found", response.data)

    def tearDown(self):
        expenses.clear()

