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
@app.route('/Balia')
def Balia():
    return render_template('Balia.html')

@app.route('/Carnatic') 
def Carnatic ():
    return render_template('Carnatic.html') 
@app.route('/ChineseFolk') 
def ChineseFolk():
    return render_template('Chinesefolk.html')
@app.route('/ChineseTraditionalOpera') 
def ChineseTradionalOpera():
    return render_template('ChineseOpera.html')  
@app.route('/Cpop') 
def Cpop ():
    return render_template('Cpop.html') 
@app.route('/Dangdut') 
def Dangdut ():
    return render_template('Dangdut.html') 
@app.route('/GagakuCourtMusic') 
def GagakuCourtMusic ():
    return render_template('Gagakucourt.html') 
@app.route('/GoaTrance') 
def GoaTrance ():
    return render_template('Goatrance.html') 
@app.route('/Hindustani') 
def Hindustani ():
    return render_template('Hindustani.html') 
@app.route('/JapaneseFolk') 
def JapaneseFolk ():
    return render_template('Japanesefolk.html') 
@app.route('/Jpop') 
def Jpop ():
    return render_template('Jpop.html') 
@app.route('/Ktrot') 
def Ktrot ():
    return render_template('ktrot.html') 
@app.route('/Punjabi') 
def Punjabi ():
    return render_template('Punjabi.html') 
@app.route('/Rafi') 
def Rafi ():
    return render_template('Rafi.html') 
@app.route('/Ragarock') 
def Ragarock ():
    return render_template('Ragarock.html') 
@app.route('/Vpop') 
def Vpop ():
    return render_template('Vpop.html') 

@app.route('/Caribbean')
def Caribbean():
    return render_template('Caribbean.html')

@app.route('/Calypso')
def Calypso():
    return render_template('Calypso.html')
@app.route('/Dancehall')
def Dancehall():
    return render_template('Dancehall.html')
@app.route('/Mambo')
def Mambo():
    return render_template('Mambo.html')
@app.route('/Mento')
def Mento():
    return render_template('Mento.html')
@app.route('/Merengue')
def Merengue ():
    return render_template('Merengue.html')
@app.route('/Reggae')
def Reggae():
    return render_template('Reggae.html')
@app.route('/Rocksteady')
def Rocksteady():
    return render_template('Rocksteady.html')
@app.route('/Salsa')
def Salsa():
    return render_template('Salsa.html')
@app.route('/Ska')
def Ska():
    return render_template('Ska.html')
@app.route('/Soca')
def Soca():
    return render_template('Soca.html')
@app.route('/Steel')
def Steel():
    return render_template('Steel.html')
@app.route('/Zouk')
def Zouk ():
    return render_template('Zouk.html')



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