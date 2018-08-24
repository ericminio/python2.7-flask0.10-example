from flask import Flask
from flask import render_template, make_response, jsonify, request
from challenges.ping import pong

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def alive():
    return pong()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/primeFactors')
def primeFactors():
    number = int(request.args.get('number'))
    decomposition = []
    while number % 2 == 0 :
        decomposition.append(2)
        number = number / 2

    return make_response(jsonify(
        {
            'number': int(request.args.get('number')),
            'decomposition': decomposition
        }
    ))