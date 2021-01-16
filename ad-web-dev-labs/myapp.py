from flask import Flask, redirect, url_for, abort, request
import time
app = Flask(__name__)

# debugg tool: request.method, request.path, request.form

@app.route('/')
def root():
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    start = '<img src="'
    url = url_for('static', filename='warrior.png')
    end = '">'
    return '<h3>Welcome warrior...</h3><br>'+start+url+end, 200

@app.route('/profile/<name>')
def profile(name):
    return "<h3>Name: %s <br>Age: 22<br> Class: Warrior</h3>" % name

@app.route('/profile/picture', methods=['POST', 'GET'])
def picture():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save('static/profile.jpg')
        return '<img src="'+ url_for('static', filename='profile.jpg') +'">' 
    else:
        pic = '<img src="'+ url_for('static', filename='profile.jpg') +'">' 
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
    return 'Here is the village Somewood'

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
    app.run(host='0.0.0.0', debug=True)