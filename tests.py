import unittest
import app
import json

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_1(self):
        rv = self.app.get('/TRSclaim')
        data = json.loads(rv.data)
        assert data['found'] == 'False'

    def test_2(self):
        rv = self.app.get('/TRSclaim?claim_id=fasdfhwkjfqwkjdf')
        data = json.loads(rv.data)
        assert data['found'] == 'False'

    def test_3(self):
        rv = self.app.get('/TRSclaim?claim_id=001ebb7f-a194-43ff-9906-6c2ba3070a11')
        data = json.loads(rv.data)
        assert data['found'] == 'True'


if __name__ == '__main__':
    unittest.main()