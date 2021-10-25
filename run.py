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



def response_none(Question):
    '''
    Here the user will respond to whethere to generate password
    '''
    response = None
    while response not in ("Yes", "No"):
        response = input(Question).lower()
    return response

def main():
    print (f"hello welcome to PasswordLock")
    print('\n')
    print("Create your Account")
    print('\n')
    
    print("Enter username") 
    user_name = input()
    print(f"Enter password")
    password = input()
    save_user(create_user(user_name, password))
    print('\n')
    refresh()
    
    print('\n')
    print(f"Hi {user_name}, You have succefully created your account.")
    print('\n')
    
    print("Login")
    print('\n')
    
    print("Enter username") 
    user_name = input()
    print(f"Enter password")
    password = input()
    print('\n')
    
    if check_existing_user(user_name, password):
        fetch_user = find_user(user_name,password)
        
        while True:
           print('\n')
           print("Please choose, na - to create new account, sa - to show/display account, fa- to find an account, da- to delete an account, ex -exit")
           print('\n')
           
           user_reply = input().lower()
           
           if user_reply == 'na':
               print("New user Account")
               print("*"*10)
               
               print("Account Name")
               myaccount_name =  input()
               
               print("Username")
               user_name = input()
               
               generate = response_none("Click y for automatic password (y/n)")
               if generate == "y":
                   value = 16
                   upper = string.ascii_uppercase
                   lower = string.ascii_lowercase
                   num = string.digits
                   all = upper + lower + num
                   temp = random.sample(all,value)
                   password = "".join(temp)