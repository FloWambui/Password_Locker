import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test
        """
        self.new_credentials = Credentials(
            "Facebook", "Florence", "pass@1234")

    def test_init(self):
        """
        Test case to test if credential object is created
        """
        self.assertEqual(self.new_credentials.social_account,"Facebook")
        self.assertEqual(self.new_credentials.user_account_name,"Florence")
        self.assertEqual(self.new_credentials.user_account_password,"pass@1234")
        