import re
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
    return render_template('Inkiranya.html')
@app.route('/juju')
def juju():
    return render_template('juju.html')
@app.route('/Majika')
def Majika():
    return render_template('Majika.html')
@app.route('/mbalax')
def mbalax():
    return render_template('mbalax.html')
@app.route('/ndombolo')
def ndombolo():
    return render_template('Ndombolo.html')
@app.route('/palmwine')
def palmwine():
    return render_template('palmwine.html')
@app.route('/rababah')
def Rababah():
    return render_template('Rababah.html')
@app.route('/shaabi')
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
def ChineseTraditionalOpera():
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

@app.route('/Reggae')
def Reggae():
    return render_template('Reggae.html')
@app.route('/Rocksteady')
def Rocksteady():
    return render_template('Rocksteady.html')

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
@app.route('/Acapella')
def Acapella():
  return render_template('Acapella.html')
@app.route('/Celtic')
def Celtic():
  return render_template('Celtic.html')
@app.route('/Drum')
def Drum():
  return render_template('Drum.html')
@app.route('/Euro')
def Euro():
  return render_template('Euro.html')
@app.route('/Flamenco')
def Flamenco():
  return render_template('Flamenco.html')
@app.route('/Glitch')
def Glitch():
  return render_template('Glitch.html')
@app.route('/Grime')
def Grime():
  return render_template('Grime.html')
@app.route('/Opera')
def Opera():
  return render_template('Opera.html')
@app.route('/Polka')
def Polka():
  return render_template('Polka.html')
@app.route('/Trance')
def Trance():
  return render_template('Trance.html')



@app.route('/Latin')
def Latin():
    return render_template('Latin.html')
@app.route('/Bachata')
def Bachata():
    return render_template('Bachata.html')
@app.route('/Balada')
def Balada():
    return render_template('Balada.html')
@app.route('/Bossa')
def Bossa():
    return render_template('Bossa.html')
@app.route('/Compas')
def Compas():
    return render_template('Compas.html')
@app.route('/Cumbia')
def Cumbia():
    return render_template('Cumbia.html')
@app.route('/Mariachi')
def Mariachi():
    return render_template('Mariachi.html')
@app.route('/Merengue')
def Merengue ():
    return render_template('Merengue.html')
@app.route('/Mesitzo')
def Mesitzo():
    return render_template('Mesitzo.html')
@app.route('/Ranchera')
def Ranchera():
    return render_template('Ranchera.html')
@app.route('/Reggaeton')
def Reggaeton():
    return render_template('Reggaeton.html')
@app.route('/Salsa')
def Salsa():
    return render_template('Salsa.html')
@app.route('/Samba')
def Samba():
    return render_template('Samba.html')
@app.route('/Tango')
def Tango():
    return render_template('Tango.html')
@app.route('/Vallenato')
def Vallenato():
    return render_template('Vallenatto.html')


@app.route('/North')
def North():
    return render_template('North.html')
@app.route('/AmericanFolk')
def AmericanFol():
    return render_template('Americanfolk.html')
@app.route('/Bluegrass')
def Bluegrass():
    return render_template('Bluegrass.html')
@app.route('/Blues')
def Blues():
    return render_template('Blues.html')
@app.route('/CanadianFolk')
def CanadianFolk():
    return render_template('CanadianFolk.html')
@app.route('/Industrial')
def Industrial():
    return render_template('Industrial.html')
@app.route('/Swing')
def Swing():
    return render_template('Swing.html')
@app.route('/Tejano')
def Tejano():
    return render_template('Tejano.html')
@app.route('/Zydeco')
def Zydeco():
    return render_template('Zydeco.html')

@app.route('/Top')
def Top():
    return render_template('Top.html')
@app.route('/Classical')
def Classical():
    return render_template('Classical.html')
@app.route('/Country')
def Country():
    return render_template('Country.html')
@app.route('/EDM')
def EDM():
    return render_template('EDM.html')
@app.route('/Hiphop')
def Hiphop():
    return render_template('Hiphop.html')
@app.route('/Indierock')
def Indierock():
    return render_template('Indierock.html')
@app.route('/Jazz')
def Jazz():
    return render_template('Jazz.html')
@app.route('/Kpop')
def Kpop():
    return render_template('kpop.html')
@app.route('/Metal')
def Metal():
    return render_template('Metal.html')
@app.route('/Oldies')
def Oldies():
    return render_template('Oldies.html')
@app.route('/Pop')
def Pop():
    return render_template('Pop.html')
@app.route('/Rap')
def Rap():
    return render_template('Rap.html')
@app.route('/RB')
def RB():
    return render_template('RB.html')
@app.route('/Rock')
def Rock():
    return render_template('Rock.html')
@app.route('/Techno')
def Techno():
    return render_template('Techno.html')
