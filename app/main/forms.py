from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators=[InputRequired()])
    post = TextAreaField('Pitch Message', validators=[InputRequired()])
    category = SelectField('Pitch Category', choices=[('One Word Pitch', 'One Word Pitch'), ('Question Pitch', 'Question Pitch'), ('Rhymic Pitch', 'Rhymic Pitch'), ('Twitter Pitch', 'Twitter Pitch'),('Tech Pitch', 'Tech Pitch')],
                           validators=[InputRequired()])
    submit = SubmitField('POST PITCH')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please share something interesting about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')
    

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[InputRequired()])
    submit = SubmitField('Post')


class Vote(FlaskForm):
    submit = SelectField('Like')

