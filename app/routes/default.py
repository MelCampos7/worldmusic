from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/African')
def African():
    return render_template('African.html')

@app.route('/Asian')
def Asian():
    return render_template('Asian.html')

@app.route('/Caribbean')
def Caribbean():
    return render_template('Caribbean.html')

@app.route('/European')
def European():
    return render_template('European.html')

@app.route('/Latin')
def Latin():
    return render_template('Latin.html')

@app.route('/North')
def North():
    return render_template('North.html')

@app.route('/Top')
def Top():
    return render_template('Top.html')