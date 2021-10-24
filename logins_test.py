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
    

        
if __name__ == '__main__':
    unittest.main()  
    