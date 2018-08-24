from flask import Flask
from flask import jsonify, make_response

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def alive():
    return make_response(jsonify(
        {'alive': True}
    ))

@app.route('/')
def index():
    return '<a id="repository-link" href="https://github.com/ericminio/python2.7-flask0.10-example">The source</a>'