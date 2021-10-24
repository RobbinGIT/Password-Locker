#!/usr/bin/env python3.9

from  passwordlock import User
from logins import Logins
import random
import string
import os
os.system("clear")

# the user class methods

def create_user(user_name, password):
    '''
    this method will create a new account
    '''
    
    new_user = User(user_name , password)
    return new_user

def save_user(user):
    '''
    method saves the new user account
    '''
    user.save_user()
    
def find_user(user_name,password):
    '''
    
    '''
    return User.finduserbyname(user_name,password)

def check_existing_user(user_name,password):
    '''
    
    '''
    return User.user_exist(user_name, password)

def refresh():
    os.system("clear")
    
    
# the class functions

def create_account(myaccount_name, user_name, password):
    '''
    create new account
    '''
    new_account = Logins(myaccount_name, user_name,password)
    
def save_account(credential):
    '''
    save new account
    '''
    Logins.save_account()
    

    