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
    
    
    return render_template('index.html', title=title)
    
    
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches = Pitch.query.filter_by(user_id = user.id).order_by(Pitch.date_posted.desc()).all()
    

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,pitches =pitches)

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
# @login_required
def pitches():
    pitches = Pitch.query.order_by(Pitch.date_posted.desc()).all()
    One_Word_Pitch = Pitch.query.filter_by(category='One Word Pitch').order_by(Pitch.date_posted.desc()).all()
    Question_Pitch = Pitch.query.filter_by(category='Question Pitch').order_by(Pitch.date_posted.desc()).all()
    Rhymic_Pitch = Pitch.query.filter_by(category='Rhymic Pitch').order_by(Pitch.date_posted.desc()).all()
    Twitter_Pitch = Pitch.query.filter_by(category='Twitter Pitch').order_by(Pitch.date_posted.desc()).all()
    Tech_Pitch = Pitch.query.filter_by(category='Tech Pitch').order_by(Pitch.date_posted.desc()).all()
    upvotes = Upvote.query.all()
    user = current_user
    return render_template('pitch_render.html', pitches=pitches, One_Word_Pitch= One_Word_Pitch, Question_Pitch=Question_Pitch, Rhymic_Pitch=Rhymic_Pitch, Twitter_Pitch=Twitter_Pitch, Tech_Pitch= Tech_Pitch)


@main.route('/new_pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data
        user_id = current_user._get_current_object().id
        pitch_obj = Pitch(pitch=pitch, title=title, category=category,user_id=user_id)
        pitch_obj.save()
        return redirect(url_for('main.index'))
    return render_template('Newpitch.html', form=form)

@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def like(id):
    get_pitches = Upvote.query_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitches',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, pitch_id=id)
    new_vote.save()
    return redirect(url_for('main.pitches',id=id))

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def dislike(id):
    pitch = Downvote.query_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitched in pitch:
        to_str = f'{pitched}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitches',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, pitch_id=id)
    new_downvote.save()
    return redirect(url_for('main.pitches',id = id))

@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,pitch_id = pitch_id,user_id = user_id,)
        new_comment.save()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('comments.html', form =form, pitch = pitch,all_comments=all_comments)


