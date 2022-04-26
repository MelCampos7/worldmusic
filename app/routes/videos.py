from app import app, login
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Video
from app.classes.forms import VideoForm
from flask_login import login_required
import datetime as dt

@app.route('/video/new', methods=['GET', 'POST'])

@login_required

def videoNew():
   
    form = VideoForm()

   
    if form.validate_on_submit():

         
        newVideo = Video(
           author = form.author.data, 
           title = form.title.data,
           composer = form.composer.data,
           vidLink = form.vidLink
           
        )
       
        newVideo.save()

       
        return redirect(url_for('post',postID=newVideo.id))

   
    return render_template('video.html',form=form)

