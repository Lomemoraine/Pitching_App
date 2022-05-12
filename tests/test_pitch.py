import unittest
from app.models import Pitch,User,Comment,Downvote,Upvote
from app import db

class PitchModelTest(unittest.TestCase):
    
        def setUp(self):
            self.comment = Comment(comment ='fantastic')
            self.upvote = Upvote()
            self.downvotes = Downvote()
            self.user_lorraine = User(username = 'lorraine',password = 'potato', email = 'lorraine@gmail.com')
            self.new_Pitch = Pitch(pitch='One word',title = 'Rain',category="One word",user = self.user_lorraine,down_vote = self.downvotes ,up_vote = self.upvote,comment =self.comment)
        def tearDown(self):
                Pitch.query.delete()
                User.query.delete()
                Comment.query.delete()
                Upvote.query.delete()
                Downvote.query.delete()
        def test_check_instance(self):
            self.assertTrue(isinstance(self.new_Pitch, Pitch))
            pass
        def test_check_instance_variables(self):
            self.assertEquals(self.new_Pitch.pitch,"One word")
            self.assertEquals(self.new_Pitch.title,'Rain')
            self.assertEquals(self.new_Pitch.category,"One word")
            self.assertEquals(self.new_Pitch.user,self.user_lorraine)
            self.assertEquals(self.new_Pitch.down_vote,self.downvotes)
            self.assertEquals(self.new_Pitch.up_vote,self.upvote)
            self.assertEquals(self.new_Pitch.comment,self.comment)
            pass
        
        def test_save_pitch(self):
            self.new_Pitch.save()
            self.assertTrue(len(Pitch.query.all())>0)
            pass
        
