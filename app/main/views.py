from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm,UpdateProfile,CommentForm
from .. import db,photos

from ..models import Pitch,User,Comment,Upvote,Downvote
from flask_login import login_required,current_user

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
    
    
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
@main.route('/pitches')
@login_required
def pitches():
    pitches = Pitch.query.all()
    upvotes = Upvote.query.all()
    user = current_user
    return render_template('pitch_render.html', pitches=pitches, upvotes=upvotes, user=user)


@main.route('/new_pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data
        user_id = current_user._get_current_object().id
        pitch_obj = Pitch(pitch=pitch, title=title, category=category, user_id=user_id)
        pitch_obj.save()
        return redirect(url_for('main.index'))
    return render_template('Newpitch.html', form=form)


