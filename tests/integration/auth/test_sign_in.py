import requests
import unittest

class TestSignIn(unittest.TestCase):
    """ Test Class responsible for handling sign in test cases """

    def setUp(self):
        self.fake_data = {
            "username": "fake user",
            "password": "fake123",
            "email": "fake@email.com"
        }
        self.base_url = "http://0.0.0.0:8000/api/v1/auth"
        self.user_id = None

    def test_sign_up_and_login(self):
        sign_up_response = requests.post(f"{self.base_url}/sign-up/", json=self.fake_data)
        self.assertEqual(sign_up_response.status_code, 201)

        sign_up_json = sign_up_response.json()
        self.assertIn("payload", sign_up_json)

        self.user_id = sign_up_json["payload"].get("id")
        self.assertIsNotNone(self.user_id)

        form_data = {"username": self.fake_data["email"], "password": self.fake_data["password"]}
        login_response = requests.post(f"{self.base_url}/sign-in/", data=form_data)
        self.assertEqual(login_response.status_code, 200)

        login_json = login_response.json()
        self.assertIn("access_token", login_json)
        self.assertIn("token_type", login_json)
        self.assertTrue(login_json["access_token"].startswith("eyJ"))

if __name__ == "__main__":
    unittest.main()
