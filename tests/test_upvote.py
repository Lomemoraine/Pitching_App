import unittest
from app.models import User,Pitch,Upvote

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user =User()
        self.pitch = Pitch()
        self.new_Upvote = Upvote(user = self.new_user, pitch=self.pitch)
    def test_check_instance(self):
            self.assertEquals(self.new_Upvote.pitch,self.pitch)
            self.assertEquals(self.new_Upvote.user,self.new_user)
            
            pass
    