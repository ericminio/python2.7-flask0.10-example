from flask import Flask
from flask import render_template
from challenges.ping import pong

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def alive():
    return pong()

@app.route('/')
def index():
    return render_template('home.html')