from flask import Flask
from flask import render_template, request, send_file
from yose.challenges.ping import pong 
from yose.challenges.primefactors import poweroftwo

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def alive():
    return pong()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/primeFactors')
def primeFactors():
    return poweroftwo(int(request.args.get('number')))

@app.route('/minesweeper')
def board():
    return send_file('challenges/minesweeper.html')
    