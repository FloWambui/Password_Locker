#!/usr/bin/env python3.6

from user import User
from credentials import Credentials

def create_new_user(first_name, last_name, username, password):
    """
    Function to create a new user
    """
    new_user = User(first_name, last_name, username, password)
    return new_user

def save_user(user):
    """
    Function to save user
    """
    user.save_user()

def delete_user(username):
    """
    Function to delete user
    """
    User.delete_user(username)

def check_user(username):
    """
    Function to check if user exists
    """
    return User.find_by_username(username)

# def check_user_password(username, password):
#     """
#     Function to check the user has entered the correct username and password
#     """
#     return User.user_exist(username, password)

# Credentials Instance

def create_new_credential(account_name, user_name, account_password):
    """
    Function to create new credentials
    """
    new_credential = Credentials(account_name, user_name, account_password)
    return new_credential

def save_credentials(credentials):
    """
    Function to save credentials
    """
    credentials.save_credentials()

def display_credentials():
    """
    Function to diasplay credentials
    """
    return Credentials.display_credentials()

def delete_credentials(social_account):
    """
    Fucntion to delete credentials
    """
    return Credentials.delete_credentials(social_account)

def find_credentials(user_account):
    """
    Function to find credential by ser account
    """
    return Credentials.find_by_social_account(user_account)

def generate_password(password_lenght):
    """
    Function to generate random password
    """
    return Credentials.generate_password(password_lenght)


def main():
    #Username Prompt
    print("Hola! What is your name? ")
    name = input()

    print(f"Welcome to Password Locker {name}. Kindly Navigate the Page")
    while True:
        print('*'*50)
        print("Use these short codes to navigate password locker:\n cc - create a new user account,\n lg - log into your account,\n da -display your account,\n ex-exit password locker")
        print('*'*50)
        short_code = input().lower()
        if short_code == 'cc':
            print("Create New User Account")
            print('*'*50)
            print("Enter you First Name....")
            first_name = input()
            print("Enter you Last Name....")
            last_name = input()
            print("Enter your Username....")
            username = input()
            print("Enter your password....")
            password  = input()

            save_user(create_new_user(first_name, last_name, username, password))
            print('*'*50)
            print(f"Hola {first_name} {last_name} , Your account has been successfully created. Proceed to login")
            print('*'*50)
        elif short_code == 'lg':
            print('*'*50)
            print("Enter your User Name....")
            username = input()
            print("Enter your password....")
            password = input()
            if check_user(username):
                if check_user(username):
                    print("\n")
                    print(f"Welcome back {username}")
                    print('*'*50)
                    while True:
                        print("Continue with the options below: \n")
                        print("1. Create Credential \n2. View Credential\n3. Delete Credential\n4. Log Off ")
                        print("\n")
                        log_choice = int(input())
                        if log_choice ==1:
                            print("Enter the social account you want to Create ....Facebook, Behance, Twitter")
                            account_name = input()
                            print("Enter your social account username")
                            user_name = input()
                            print('\n')
                            #Password generate
                            print('*'*50)
                            print("Generate Random Password?\n Enter 1 to generate randomn password\n Enter 2 to create own password")
                            print('*'*10)
                            print('\n')
                            choice = int(input())
                            if choice ==1:
                                print("Choose Password Lenght")
                                password_lenght = int(input())
                                account_password = generate_password(password_lenght)
                                print(f'Generated Password: {account_password}')
                            elif choice ==2:
                                print('Entwr Password of the social account')
                                account_password = input()
                            else:
                                print("Invalid Entry")





if __name__ == '__main__':
    main()

