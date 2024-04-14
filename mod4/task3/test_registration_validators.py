import unittest

from mod4.task2.registration import app


class TestWtformsValidatorsAdv(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = '/registration'

    def test_valid_email(self):
        response = self.app.post(self.base_url, data=dict(
            email='test@example.com',
            phone='1234567890',
            name='John Doe',
            address='123 Main St',
            index='12345',
            comment='This is a test comment'
        ))
        self.assertEqual(response.status_code, 200)

    def test_invalid_email(self):
        response = self.app.post(self.base_url, data=dict(
            email='',
            phone='1234567890',
            name='John Doe',
            address='123 Main St',
            index='12345',
            comment='This is a test comment'
        ))
        self.assertEqual(response.status_code, 400)

    def test_valid_phone(self):
        response = self.app.post(self.base_url, data=dict(
            email='test@example.com',
            phone='1234567890',
            name='John Doe',
            address='123 Main St',
            index='12345',
            comment='This is a test comment'
        ))
        self.assertEqual(response.status_code, 200)

    def test_invalid_phone(self):
        response = self.app.post(self.base_url, data=dict(
            email='test@example.com',
            phone='',
            name='John Doe',
            address='123 Main St',
            index='12345',
            comment='This is a test comment'
        ))
        self.assertEqual(response.status_code, 400)

    def test_valid_name(self):
        response = self.app.post(self.base_url, data=dict(
            email='test@example.com',
            phone='1234567890',
            name='John Doe',
            address='123 Main St',
            index='12345',
            comment='This is a test comment'
        ))
        self.assertEqual(response.status_code, 200)

    def test_invalid_name(self):
        response = self.app.post(self.base_url, data=dict(
            email='test@example.com',
            phone='1234567890',
            name='',
            address='123 Main St',
            index='12345',
            comment='This is a test comment'
        ))
        self.assertEqual(response.status_code, 400)

    def test_valid_address(self):
        response = self.app.post(self.base_url, data=dict(
            email='test@example.com',
            phone='1234567890',
            name='John Doe',
            address='123 Main St',
            index='12345',
            comment='This is a test comment'
        ))
        self.assertEqual(response.status_code, 200)

    def test_invalid_address(self):
        response = self.app.post(self.base_url, data=dict(
            email='test@example.com',
            phone='1234567890',
            name='John Doe',
            address='',
            index='12345',
            comment='This is a test comment'
        ))
        self.assertEqual(response.status_code, 400)

    def test_valid_index(self):
        response = self.app.post(self.base_url, data=dict(
            email='test@example.com',
            phone='1234567890',
            name='John Doe',
            address='123 Main St',
            index='12345',
            comment='This is a test comment'
        ))
        self.assertEqual(response.status_code, 200)

    def test_invalid_index(self):
        response = self.app.post(self.base_url, data=dict(
            email='test@example.com',
            phone='1234567890',
            name='John Doe',
            address='123 Main St',
            index='',
            comment='This is a test comment'
        ))
        self.assertEqual(response.status_code, 400)

    def test_valid_comment(self):
        response = self.app.post(self.base_url, data=dict(
            email='test@example.com',
            phone='1234567890',
            name='John Doe',
            address='123 Main St',
            index='12345',
            comment='This is a test comment'
        ))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
