class User:
    """
    class generating a new instance of users
    """
    user_details = []

    def __init__(self, first_name, last_name, username, password):
        """
        properties for the password lock object
        """

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
     
    #  Saving User

    def save_user(self):
        """
        save_user method saves user to user_details list
        """

        User.user_details.append(self)

    def delete_user(self):
        """
        Deleting user from the list
        """

        User.user_details.remove(self)

    @classmethod
    def find_by_username(cls,username):
        """
        Method that takes in the text and return a username matching that text
        """

        for user in cls.user_details:
            if user.username == username:
                return user

    @classmethod
    def user_exist(cls,username):
        """
        Method to check existence of a username ftom the user list
        """

        for user in cls.user_details:
            if user.username == username:
                return True
            return False

