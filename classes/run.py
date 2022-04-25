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