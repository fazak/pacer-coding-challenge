from django.test import Client, SimpleTestCase
from rest_framework import status

import json


class ScoreViewTestCase(SimpleTestCase):
    """A class to test ScoreView"""

    def setUp(self):
        """Set API path"""

        self.path = "/api/score/get_score/"

    def test_getscore_get(self):
        """
        Test for:
        - 200 OK response when getting score correctly
        - Response data is in the correct format
        """

        c = Client()
        input = 1
        resp = c.get(self.path, { "input": 1 })
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp["Content-Type"], "application/json")
        self.assertEqual(type(resp.content), bytes)

        data = json.loads(resp.content.decode('utf-8'))
        self.assertIsInstance(data, dict)
        self.assertIn("score", data)
        self.assertEqual(type(data["score"]), int)
        self.assertEqual(data["score"], input + 1)

    def test_getscore_get2(self):
        """Test for GET request with wrong query parameter value. Expected response
        status code should be 400"""

        c = Client()
        resp = c.get(self.path, { "input": "abc" })
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_getscore_get3(self):
        """Test for GET request with wrong query parameter. Expected response
        status code should be 400"""

        c = Client()
        resp = c.get(self.path, { "wrongparams": 123 })
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_getscore_post(self):
        """Test for POST request. Expected response status code should be 405"""

        c = Client()
        resp = c.post(self.path, {})
        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)