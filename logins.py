import random
import string


class Logins:
    '''
    class to generate new logins
    '''
    logins_list = []
    
    def __init__(self,myaccount_name, user_name, password):
        '''
        this is a constructor for logins
        '''
        self.myaccount_name = myaccount_name
        self.user_name = user_name
        self.password = password
        
    def save_myaccount(self):
        '''
        this method will append ne myaccount to the list
        '''
        Logins.logins_list.append(self)
       #to find account it must first exist  
  
    
    @classmethod
    def findby_account_name(cls, myaccount_name):
        '''
        search account by name of the account
        '''
        for account in cls.logins_list:
            if account.myaccount_name == myaccount_name:
                return account
            
        
    def delete_account(self):
        '''
        method to remove account
        '''
        Logins.logins_list.remove(self)
        
    @classmethod
    def account_exist(cls, myaccount_name):
        '''
        this will check if an account exists in the list
        '''
        for account in cls.logins_list:
            if account.myaccount_name == myaccount_name:
                return True
            
        return False
                
    @classmethod
    def display_account(cls):
        '''
        this will give us all the accounts present
        '''  
        return cls.logins_list
    
    
    