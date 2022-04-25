#!/usr/bin/env python3.6

from this import d
from user import User

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

def check_user_password(username, password):
    """
    Function to check the user has entered the correct username and password
    """
    return User.check_user(username, password)


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
                if check_user_password(username, password):
                    print("\n")
                    print(f"Welcome back {username}")
                    print('*'*50)
                    while True:
                        print("Continue with the options below: \n")
                        print("1. ")


if __name__ == '__main__':

    main()

