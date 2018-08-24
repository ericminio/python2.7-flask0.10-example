from flask import Flask
from flask import render_template, request
import challenges.ping, challenges.primefactors

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def alive():
    return challenges.ping.pong()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/primeFactors')
def primeFactors():
    return challenges.primefactors.poweroftwo(int(request.args.get('number')))
    