# TO RUN THE APP DO:
'
.\env\Scripts\activate
set FLASK_APP=myapp.py
set FLASK_ENV=development
python -m flask run



deactivate
'

# FLASK
'set FLASK_APP=file_name.py' - set the app entrypoint file
'set FLASK_ENV=development' - set the mode to use for the app deployment to development
'python -m flask run --host=0.0.0.0' - tun the app


# Controlling the virtual environment
'py -m venv env' - get the venvenv
'.\env\Scripts\activate' - activate the venvenv
'where python' - check the location of the virtual env
'deactivate' - close the virtual env

# Requests
'curl -i -X POST http://127.0.0.1:5000/.../..' - post to the route .../..


