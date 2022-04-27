from turtle import title
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
           author = current_user.id, 
           title = form.title.data,
           composer = form.composer.data,
           vidLink = form.vidLink.data
           
        )
       
        newVideo.save()

        return redirect(url_for('video',VideoId=newVideo.id))

    return render_template('videoform.html',form=form)
    
@app.route('/video/<VideoId>')
@login_required
def video(VideoId):
    thisVideo = Video.objects.get(id = VideoId)
    return render_template('video.html',video = thisVideo)

@app.route('/video/delete/<VideoId>')
@login_required
def videoDelter(VideoId):
    delVideo = Video.objects.get(id = VideoId)
    flash(f"Deleting Video.")
    delVideo.delete()
    return redirect(url_for('videoList'))

@app.route('/video/list')
@login_required
def videoList():
    videos = Video.objects()
    return render_template('videos.html',videos = videos )

@app.route('/video/edit/<VideoId>', methods=['GET', 'POST'])
@login_required
def videoEdit(VideoId):
    form = VideoForm()
    editVideo = Video.objects.get(id=VideoId)
   
    if form.validate_on_submit():

        editVideo.update(
           title = form.title.data,
           composer = form.composer.data,
           vidLink = form.vidLink.data
        )

        return redirect(url_for('video',VideoId=editVideo.id))

    form.title.data = editVideo.title
    form.composer.data = editVideo.composer
    form.vidLink.data = editVideo.vidLink

    return render_template('videoform.html',form=form)


