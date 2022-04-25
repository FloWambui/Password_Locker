import random
import string

class Credentials():
    user_credentials = []

    def __init__(self, social_account, user_account_username, user_account_password):
        """
        social_account - property for new credentials class account
        user_account_password - new credentials password
        """
        self.social_account = social_account
        self.user_account_name = user_account_username
        self.user_account_password = user_account_password

    def save_credentials(self):
        """
        save credntials to the user credentials list
        """
        Credentials.user_credentials.append(self)

    def delete_credentials(self):
        """
        Deletes credentials
        """
        Credentials.user_credentials.remove(self)

    @classmethod
    def find_by_social_account(cls, social_account):
        """
        Method to take text and return credentials that match account_credentials
        """
        for credentials in cls.user_credentials:
            if credentials.social_account == social_account:
                return Credentials
        return False

    @classmethod
    def display_credentials(cls):
        """
        Method to return the credentials list
        """
        return cls.user_credentials

    @classmethod
    def generate_password(cls, password_length):
        """
        Method for random password generation for new user
        """
        alpa = string.ascii_letters+string.digits
        password = ''.join(random.choice(alpa)
                            for i in range(password_length))
        return password
                        