import unittest
from logins import Logins

class TestLogins(unittest.TestCase):
    '''
    test subclasses........
    '''
# First Test
    def setUp(self):
        '''
        method will run before each individual logins test method runs
        '''
        self.new_myaccount = Logins("Facebook", "Robbin", "HakunaPassword")
        
    def test_init(self):
        '''
        checking if a new login instace has been instatiated correctly
        '''
        self.assertEqual(self.new_myaccount.myaccount_name, "Facebook")
        self.assertEqual(self.new_myaccount.user_name, "Robbin")
        self.assertEqual(self.new_myaccount.password, "HakunaPassword")
        
    def tearDown(self):
        '''
        this methods cleans up each test after every run.
        '''
        Logins.logins_list = []
        
    # second test
    
    def test_save_myaccount(self):
        '''
        this will test if new logins acconts have been saved in the new logins lists
        '''  
        self.new_myaccount.save_myaccount()
        self.assertEqual(len(Logins.logins_list),1)
    
    # Third test
    def test_save_multiple_accounts(self):
        '''
        testing to see if we can save many login credetials to the login list
        '''
        self.new_myaccount.save_myaccount()
        test_logins = Logins("Facebook", "Robbin", "HakunaPassword")
        test_logins.save_myaccount()
        self.assertEqual(len(Logins.logins_list),2)
    
    # forth test
    def test_find_myaccount_by_name(self):
        ''''
        find account to display information
        '''
        self.new_myaccount.save_myaccount()
        test_myaccount = Logins("Facebook", "Robbin", "HakunaPassword")
        test_myaccount.save_myaccount()
        
        the_login = Logins.findby_account_name("Facebook")
        self.assertEqual(the_login.user_name, test_myaccount.user_name)
        
if __name__ == '__main__':
    unittest.main()  
    