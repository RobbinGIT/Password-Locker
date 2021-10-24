import unittest
from passwordlock import User  #importing the class created in the passwordlock.py

class TestClass(unittest.TestCase):
    '''
    class to test fuser functions
    '''
    
    def setUp(self):
        '''
        this function will run before anyother individual function
        '''
        self.new_user = User('Robbin','HakunaPassword')
        
    def test_init(self):
        '''
        this method checks if the the instance has been nitilalized
        '''
        self.assertEqual(self.new_user.username,'Robbin')
        self.assertEqual(self.new_user.password, "HakunaPassword")
    