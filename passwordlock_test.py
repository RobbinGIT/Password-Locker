import unittest
from passwordlock import User  #importing the class created in the passwordlock.py

class TestClass(unittest.TestCase):
    '''
    class to test fuser functions
    '''
    # Test 1 - check for correct instantion of objects
    def setUp(self):
        '''
        this function will run before anyother individual function
        '''
        self.new_user = User('Robbin','HakunaPassword')
        
    def test_init(self):
        '''
        this method checks if the the instance has been initilalized properly
        '''
        self.assertEqual(self.new_user.username,'Robbin')
        self.assertEqual(self.new_user.password, "HakunaPassword")
        
    # Test 2 - save created account's credentials
    def test_save_user(self):
        """
            test if new user has been saved to the new user_list
        """
        self.new_user.save_user()  # add user to list
        self.assertEqual(len(User.user_list), 1)  # check length of list
        
    # test 3 - if object actually exists
    def test_user_exits(self):
        """ method to check if user exists in the users list"""
        self.new_user.save_user()
        check_user = User("RobbinGit", "HakunaPassword")
        check_user.save_user()
        user_exists = User.user_exist("RobbinGit", "HakunaPassword")
        self.assertTrue(user_exists)
            
        
if __name__ == '__main__':
    unittest.main()  
    
    