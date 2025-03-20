import requests
import unittest

class TestSignUp(unittest.TestCase):
    """ Test Class responsible for handling sign up test cases """

    def setUp(self):
        self.fake_data = {
            "password": "fake123",
            "email": "fake@email.com",
            "username": "fake user"
        }
        self.remaining_ids = []

    def test_sign_up_user(self):
        data = self.fake_data
        response = requests.post("http://0.0.0.0:8000/api/v1/auth/sign-up/", json=data)
        response_json = response.json()
        self.assertEqual(response.status_code, 201)
        assert "payload" in response_json
        payload = response_json['payload']
        self.remaining_ids.append(payload['id'])
        assert response.status_code == 201
        assert isinstance(response_json, dict)
