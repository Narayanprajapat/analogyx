from flask import make_response, jsonify


def response_maker(status_code, body):
    return make_response(jsonify(body), status_code)
