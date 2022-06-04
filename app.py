# import flask here
from flask import Flask

# create new flask app here
app = Flask(__name__)

# define routes for your new flask app
@app.route('/', methods=['GET'])
def index():
    return 'Hello, world!'

@app.route('/welcome', methods=['GET'])
def welcome():
    return '<b>Welcome to an amazing Flask app!</b>'

@ app.route('/goodbye', methods=['GET'])
def goodbye():
    return 'Thanks for looking around, I guess. Come back again soon. Or don\'t?'

@ app.route('/multiply', methods=['GET'])
def multiply():
    first=int(input('first'))
    second=int(input('second'))
    return str(first * second)