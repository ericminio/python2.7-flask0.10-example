from flask import make_response, jsonify, request

def poweroftwo(input):
    number = input
    decomposition = []
    candidate = 2
    while number % candidate == 0 :
        decomposition.append(candidate)
        number = number / candidate

    return make_response(jsonify(
        {
            'number': input,
            'decomposition': decomposition
        }
    ))