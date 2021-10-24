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
    
def save_account(logins):
    '''
    save new account
    '''
    logins.save_account()


def find_account(myaccount_name):
    '''
    this method will find account by name and will return that account
    '''
    return Logins.findby_account_name(myaccount_name)

def check_existing_account(myaccount_name):
    '''
    this function check if account exixt withi account name and will return a boolean value
    '''
    return Logins.account_exist(myaccount_name)

def delete_account(logins):
    '''
    removes an account
    '''
    logins.delete_account()
    
def display_account():
    '''
    returns all the saved accounts
    '''
    return Logins.display_account()
    
    
# main functions