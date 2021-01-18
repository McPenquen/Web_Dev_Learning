import configparser
import logging

from flask import Flask, redirect, url_for, abort, request, render_template, session, flash
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.secret_key = 'WOWO/4141/POPO/2121'

def init(app):
    config = configparser.ConfigParser()
    try:
        config_location = "etc/defaults.cfg"
        config.read(config_location)

        app.config['DEBUG'] = config.get("config", "debug")
        app.config['ip_address'] = config.get("config", "ip_address")
        app.config['port'] = config.get("config", "port")
        app.config['url'] = config.get("config", "url")

        app.config['log_file'] = config.get("logging", "name")
        app.config['log_location'] = config.get("logging", "location")
        app.config['log_level'] = config.get("logging", "level")
    except:
        print("Couldn't read configs from: ", config_location)

def logs(app):
    log_pathname = app.config['log_location'] + app.config['log_file']
    file_handler = RotatingFileHandler(log_pathname, maxBytes=1024*1024*10, backupCount=1024)
    file_handler.setLevel(app.config['log_level'])
    formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(module)s | %(funcName)s | %(mesage)s")
    file_handler.setFormatter(formatter)
    app.logger.setLevel(app.config["log_level"])
    app.logger.addHandler(file_handler)

init(app)
logs(app)

@app.route('/')
def root():
    return redirect(url_for('welcome'))

@app.route('/config')
def config():
    s = []
    s.append('debug: ' + str(app.config['DEBUG']))
    s.append('port: ' + str(app.config['port']))
    s.append('url: ' + str(app.config['url']))
    s.append('ip_address: ' + str(app.config['ip_address']))
    return ', '.join(s)

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap-demo.html')

@app.route('/welcome')
def welcome():
    app.logger.info('New user was welcomed.')
    return render_template('welcome.html'), 200

@app.route('/restart')
def restart():
    session.pop('name', None)
    return "Game was restarted"

@app.route('/profile')
@app.route('/profile/<name>')
def profile(name=None):
    user = {'name' : name}
    session['name'] = name
    return render_template('profile-page.html', user=user)

@app.route('/profile/curses')
def curses():
    return render_template('curses.html')

@app.route('/profile/picture', methods=['POST', 'GET'])
def picture():
    try:
        name = ''
        if(session['name']):
            name = str(session['name'])
    except KeyError:
        pass

    if request.method == 'POST':
        f = request.files['datafile']
        f.save('static/profile.jpg')
        return '<h3>Your profile picture changed to:</h3><br><img src="'+ url_for('static', filename='profile.jpg') +'">' 
    else:
        pic = '<img src="'+ url_for('static', filename='profile.jpg') +'">'
        if name != '':
            pic = '<h2>' + name + ':</h2>'+ pic
        page = ''' 
        <html><body>
            <form action="" method="post" name="form" enctype="multipart/form-data">
                <input type="file" name="datafile"/>
                <input type="submit" name="submit" id="submit"/>
            </form>
        </body><html>
        '''
        return pic + page, 200

@app.route('/village')
def village():
    places = ['smith', 'soldier', 'wizard', 'witch']
    return render_template('village.html', places=places)

@app.route('/village/witch')
@app.route('/village/witch/<curse>')
def witch(curse=None):
    if (curse != None):
        flash(curse)
        return "Haha! You are cursed now! Muhahaha..."
    else:
        return 'GET OUT OF HERE!!!'

@app.route('/village/soldier', methods=['GET','POST'])
def soldier():
    if request.method == 'POST':
        print(request.form)
        name = request.form['name']
        return "Get out of here %s and don't do any trouble" % name
    else:
        page= ''' 
        <html><body>
            <form action="" method="post" name="form>
                <label for="name">What's your name?</label>
                <input type="text" name="name" id="name"/>
                <input type="submit" name="submit" id="submit"/>
            </form>
        </body><html>
        '''
        return page

@app.route('/village/smith', methods=['GET','POST'])
def smith():
    if request.method == 'POST':
        return "You have interacted with the smith."
    else:
        return "You see the smith."

@app.route('/village/wizard')
def wizard():
    return "Oogy loogy boo yoo.. bye... pufff"

@app.route('/village/find/')
def find_in_village():
    thing = request.args.get('name', '')
    if thing == '':
        return "Are you looking for something in the village?"
    elif thing == 'wizard':
        return redirect('/village/wizard')
    elif thing == 'smith':
        return redirect('/village/smith')
    elif thing == 'soldier':
        return redirect('/village/soldier')
    elif thing == 'witch':
        return redirect('/village/witch')
    else:
        return "%s is nowhere to be found" % thing

@app.route('/town')
def town():
    return 'Here is the town Dreamwill'

@app.route('/trigger404')
def trigger404():
    abort(404)

@app.errorhandler(404)
def page_not_found():
    return "Couldn't find the page requested.", 404 

if __name__ == '__main__':
    init(app)
    app.run(
        host = app.config['ip_address'],
        port = app.config['port'],
        debug = True
    )