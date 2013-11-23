from flask import jsonify, make_response
from yose import app

@app.route('/ping', methods=['GET'])
def alive():
    return make_response(jsonify(
        {'alive': True}
    ))
