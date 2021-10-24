#!/usr/bin/env python3.9

from  passwordlock import User
from logins import Logins
import random
import string
import os
os.system("clear")

# the user class methods

def create_user(username, password):
    '''
    this method will create a new account
    '''
    
    new_user = User(username , password)
    return new_user

def save_user(user):
    '''
    method saves the new user account
    '''
    user.save_user()
    

    