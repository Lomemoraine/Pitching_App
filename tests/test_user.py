import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    
    def setUp(self): #method to create an instance of User model and pass in password property
        self.new_user = User(password="banana")
        
    def test_password_setter(self): #method to ensure that when password is being hashed the pass_secure contains a value
        self.asserTrue(self.new_user.pass_secure is not None)
        
    def test_no_access_password(self): # to confirm that the application raises an attribute error when we try and access the passowrd property
        with self.assertRaises(AttributeError):
            self.new_user.password
            
    
    def test_password_verification(self): # to confirm that our password_hash can be verified when we pass in the correct password
        self.assertTrue(self.new_user.verify_password('banana'))