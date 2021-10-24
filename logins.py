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
        
    def save_account(self):
        '''
        this method will append ne myaccount to the list
        '''
        Logins.logins_list.append(self)
        
        
    
        
    