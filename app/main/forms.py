from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators=[InputRequired()])
    post = TextAreaField('Pitch Message', validators=[InputRequired()])
    category = SelectField('Pitch Category', choices=[('One Word Pitch', 'One Word Pitch'), ('Question Pitch', 'Question Pitch'), ('Rhymic Pitch', 'Rhymic Pitch'), ('Twitter Pitch', 'Twitter Pitch'),('Tech Pitch', 'Tech Pitch')],
                           validators=[InputRequired()])
    submit = SubmitField('POST PITCH')
