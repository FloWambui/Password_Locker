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
