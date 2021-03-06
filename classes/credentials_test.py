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
        

    def test_save_credentials(self):
        """
        Test case to check whether a new credential object is saved in the list
        """
        self.assertEqual(len(Credentials.user_credentials), 0)
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.user_credentials), 1)

    def test_delete_credentials(self):
        """
        Test case to delete credentials from the list
        """
        self.assertEqual(len(Credentials.user_credentials), 0)
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.user_credentials), 1)
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.user_credentials), 0)

    def test_find_credentials_by_social_account(self):
        """
        Test case to find credentials by social account
        """
        self.found_credentials = Credentials.find_by_social_account("Facebook")

if __name__ == '__main__':
    unittest.main()