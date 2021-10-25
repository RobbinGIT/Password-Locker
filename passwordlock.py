class User:
    '''
    this user class generates new instances for a user
    '''
    
    user_list = []
    
    def __init__(self,username,password):
        '''
        properties of the user...defined in this method
        '''
        self.username = username
        self.password = password
        
    def save_user(self):
        """ append new user to list"""
        User.user_list.append(self)
        
    @classmethod
    
    def user_exist(cls, username, password):
        '''
        this method will check if user actually exist from the list
        '''
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return True # this returns a boolean value as the argument
            
        return False
    
    @classmethod
    
    def finduserbyname(cls,username,password):
        '''
        this method is to help to find a user by their names
        '''
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return user