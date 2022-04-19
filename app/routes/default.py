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

@app.route('/Afrobeats')
def Afrobeats():
    return render_template('Afrobeats.html')
@app.route('/Benga')
def Benga():
    return render_template('Benga.html')
@app.route('/Chimurenga')
def Chimurenga():
    return render_template('Chimurenga.html')
@app.route('/Ethio')
def Ethio():
    return render_template('Ethio.html')
@app.route('/Gnawa')
def Gnawa():
    return render_template('Highlife.html')
@app.route('/Highlife')
def Highlife():
    return render_template('Highlife.html')
@app.route('/Hiplife')
def Hiplife():
    return render_template('Hiplife.html')
@app.route('/Inkiranya')
def Inkiranya():
    return render_template('Inkiraya.html')
@app.route('/Juju')
def Juju():
    return render_template('juju.html')
@app.route('/Majika')
def Majika():
    return render_template('Majika.html')
@app.route('/Mbalax')
def Mbalax():
    return render_template('mbalax.html')
@app.route('/Ndombolo')
def Ndombolo():
    return render_template('Ndombolo.html')
@app.route('/Palmwine')
def Palmwine():
    return render_template('palmwine.html')
@app.route('/Rababah')
def Rababah():
    return render_template('Rababah.html')
@app.route('/Shaabi')
def Shaabi():
    return render_template('Shaabi.html')
@app.route('/somalijazz')
def somalijazz():
    return render_template('somalijazz.html')
@app.route('/soukou')
def soukou():
    return render_template('soukou.html')
@app.route('/ubongo')
def ubongo():
    return render_template('ubongo.html')
@app.route('/zilin')
def zilin():
    return render_template('zilin.html')
@app.route('/zouglou')
def zouglou():
    return render_template('zouglou.html')

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