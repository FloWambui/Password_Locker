import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Florence","Wangechi","FloWambui","kenya22") # create user object


    def test_user_create(self):
        '''
        Test case to test if the user object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Florence")
        self.assertEqual(self.new_user.last_name,"Wangechi")
        self.assertEqual(self.new_user.username,"FloWambui")
        self.assertEqual(self.new_user.password,"kenya22")

    def test_save_user(self):
        '''
        Test to save user details
        '''
        self.assertEqual(len(User.user_details),0)
        self.new_user.save_user() #saving new user
        self.assertEqual(len(User.user_details),1)

    

    def test_delete_user(self):
        """
        Test to check user deletion
        """

        self.assertEqual(len(User.user_details), 0)
        self.new_user.save_user()
        self.assertEqual(len(User.user_details), 1)
        self.new_user.delete_user()
        self.assertEqual(len(User.user_details), 0)


if __name__ == '__main__':
    unittest.main()