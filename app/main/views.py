from flask import render_template
from . import main
from .forms import PitchForm
from ..models import Pitch
from flask_login import login_required

#views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Pitch Raine'
    pitches = Pitch.query.all()
    One_Word_Pitch = Pitch.query.filter_by(category='One_Word_Pitch').all()
    Question_Pitch = Pitch.query.filter_by(category='Question_Pitch').all()
    Rhymic_Pitch = Pitch.query.filter_by(category='Rhymic_Pitch').all()
    Twitter_Pitch = Pitch.query.filter_by(category='Twitter_Pitch').all()
    Tech_Pitch = Pitch.query.filter_by(category='Tech_Pitch').all()
    return render_template('index.html', title=title,pitches=pitches, One_Word_Pitch=One_Word_Pitch,Question_Pitch = Question_Pitch,Rhymic_Pitch = Rhymic_Pitch,Twitter_Pitch = Twitter_Pitch, Tech_Pitch = Tech_Pitch)
    
    
    return render_template('index.html' ,title=title)