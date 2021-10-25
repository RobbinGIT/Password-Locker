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

def generate_password():
    '''
    this method generate a random password
    '''
    auto_password = Logins.generatePassword()
    return auto_password
    
    
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
            print("Please choose, na - to create new account, sa - to show/display account,Tp- type own password, Gp-generate password fa- to find an account, da- to delete an account, ex -exit")
            print('\n')
            
            user_reply = input().lower().strip()
            
            if user_reply == 'na':
               print("New user Account")
               print("*"*10)
               
               print("Account Name")
               myaccount_name =  input()
               
               print("Username")
               user_name = input()
               
               while True:
                   
                print("Tp- to type own pass word:\n Gp -to generate random password")
                password_Choosen = input().lower().strip()
                # generate = response_none("would you like automatically generated passwaord? (y/n):")
                if password_Choosen == "tp":
                    password = input("Type password")
                    break
                elif password_Choosen == 'gp':
                    password = generate_password()
                    break
                else:
                    print("Please input a valid password")
                    
    
                    
                # creating and saving the new login details
                save_account(create_account(myaccount_name,user_name,password))
                print('\n')
                print(f"New account: {myaccount_name} and username: {user_name} and: {password}")
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
        
        main()
    print('\n')
                    
            
if __name__ == '__main__':

    main()

               
   
                  
            