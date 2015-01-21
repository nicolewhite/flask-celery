import unittest
import json

from webapp import app
app = app.test_client()

class TestCelery(unittest.TestCase):

    def setUp(self):
        pass

    def testAddingNode(self):
        payload = {'name':'Nicole'}
        headers = {'content-type': 'application/json'}
        response = app.post('/add_stuff', headers=headers, data=json.dumps(payload))
        self.assertEqual(response.status_code, 200)