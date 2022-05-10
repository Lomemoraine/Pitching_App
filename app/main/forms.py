from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators=[InputRequired()])
    pitch = TextAreaField('Pitch Message', validators=[InputRequired()])
    category = SelectField('Pitch Category', choices=[('One Word Pitch', 'One Word Pitch'), ('Question Pitch', 'Question Pitch'), ('Rhymic Pitch', 'Rhymic Pitch'), ('Twitter Pitch', 'Twitter Pitch'),('Tech Pitch', 'Tech Pitch')],
                           validators=[InputRequired()])
    submit = SubmitField('POST PITCH')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please share something interesting about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')
    

class CommentForm(FlaskForm):
    comment = TextAreaField('Add Comment', validators=[InputRequired()])
    submit = SubmitField('Submit')


class Vote(FlaskForm):
    submit = SelectField('Upvote')

