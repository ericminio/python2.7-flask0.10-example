from flask import Flask
from flask import jsonify, make_response

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def alive():
    return make_response(jsonify(
        {'alive': True}
    ))