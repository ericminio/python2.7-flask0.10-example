from flask import Flask
from flask import jsonify, make_response, render_template

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def alive():
    return make_response(jsonify(
        {'alive': True}
    ))

@app.route('/')
def index():
    return render_template('home.html')