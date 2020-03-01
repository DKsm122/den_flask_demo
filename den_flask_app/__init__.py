from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/hello/<user>')
def hello_user(user):
    return f'Hello, {user}!'