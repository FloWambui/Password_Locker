import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Florence","Wangechi","FloWambui","kenya22") # create user object


    def test_save_user(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Florence")
        self.assertEqual(self.new_user.last_name,"Wangechi")
        self.assertEqual(self.new_user.username,"FloWambui")
        self.assertEqual(self.new_user.password,"kenya22")


if __name__ == '__main__':
    unittest.main()