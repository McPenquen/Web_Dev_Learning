from flask import Flask, redirect, url_for, abort
app = Flask(__name__)

@app.route('/')
def root():
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    start = '<img src="'
    url = url_for('static', filename='warrior.png')
    end = '">'
    return '<h3>Welcome warrior...</h3><br>'+start+url+end, 200

@app.route('/village')
def village():
    return 'Here is the village Somewood'


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