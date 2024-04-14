import unittest
from mod5.task2.remote_execution import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()

    def test_run_code_success(self):
        with app.test_client() as client:
            response = client.post('/run_code', data=dict(
                code='print("Hello, world!")',
                timeout=10
            ))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Hello, world!', response.data)


    def test_run_code_timeout(self):
        with app.test_client() as client:
            response = client.post('/run_code', data=dict(
                code='import time; time.sleep(2);',
                timeout=1
            ))
            self.assertEqual(response.data.decode(), 'исполнение кода не уложилось в данное время')

if __name__ == '__main__':
    unittest.main()
