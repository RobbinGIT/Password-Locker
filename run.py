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
    return new_account
    
def save_myaccount(logins):
    '''
    save new account
    '''
    logins.save_myaccount()


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
    Here the user will respond to if to generate password
    '''
    response = None
    while response not in ('y', 'n'):
        response = input(Question).lower()
    return response

def main():
    print (f"hello welcome to PasswordLock")
    print('\n')
    print("Create your Account")
    print('\n')
    
    print("Enter new username") 
    user_name = input()
    print(f"Enter new password")
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
            print("Please choose using the following: na - to create new account, sa - to show/display account, \n fa- to find an account, da- to delete an account, ex -exit")
            print('\n')
            
            user_reply = input().lower()   
           
            if user_reply == 'na':
                print("New user Account")
                print("*"*30)
                
                print("Account Name")
                myaccount_name =  input()
                
                print("Username")
                user_name = input()
                
                generate = response_none("would you like automatically generated passwaord? (y/n):")
                if generate == "y":
                        value = 8
                        upper = string.ascii_uppercase
                        lower = string.ascii_lowercase
                        num = string.digits
                        all = upper + lower + num
                        temp = random.sample(all,value)
                        password = "".join(temp)
                        
                else:
                      
                    print("password")
                    password = input()
        # to create and also save new user account     
                save_myaccount(create_account( myaccount_name, user_name, password))
                print('\n')
                print(f"New account: {myaccount_name}  with user name : {user_name} created :{password}")
                print('\n')    
                
            elif user_reply == 'sa':
                if display_account():
                   print("This is a list of all accounts")
                   print('\n') 
                        
                   for logins in display_account():
                       print(f"{logins.myaccount_name} | {logins.user_name} | {logins.password}")
                            
                else:
                    print('\n')
                    print("There are no account saved")
                print('\n')
                        
            elif user_reply == 'fa':
                print("enter the account you want to find")
                    
                search_account = input()
                if check_existing_account(search_account):
                    check_account = find_account(search_account)
                    print(f"{check_account.myaccount_name}")
                    print('-'*20)
                        
                    print(f"account name  {check_account.myaccount_name}")
                    print(f"username  {check_account.user_name}")
                else:
                    print("Oops,account does not exist")
                print('\n')
                    
            elif user_reply == 'da':
                print("which account would you like to delete?")
                search_account = input()
                if check_existing_account(search_account):
                    print("Loading ....")
                    check_account = find_account(search_account)
                    delete_account(check_account)
                    print(f"account {check_account.myaccount_name} account removed successfully")
                else:
                    print('\n')
                    print("sorry no account matching the username")
                
            elif user_reply == 'ex':
                print("bye, thanks for visiting")
                break
                
            else:
                print("sorry we did not get that")
    else:
        refresh()
        print("Account does not exist. enter valid account")
        print('\n')
                     
            
if __name__ == '__main__':
    main()
           
               
   
                  
            