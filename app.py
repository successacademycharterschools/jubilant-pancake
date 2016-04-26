#!/usr/bin/env python
from flask import Flask
from flask import render_template
from flask import make_response
from flask import jsonify
from flask import request
from flask.ext.api import status
from flask_bootstrap import Bootstrap

from levenshtein import levenshtein

DEBUG = True
SECRET_KEY = 'add_a_real_key_in_production'

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    """
    Render index template with edit distance calculator
    """
    return render_template('index.html')


@app.route('/edit_distance', methods=['POST', ])
def edit_distance():
    """
    Calculates the edit distance between two strings
    via JSON POST
    """
    try:
        req_json = request.get_json()
        a, b = req_json['a'], req_json['b']
    except KeyError:
        return api_error("Please enter two values")
    data = {
        'result': levenshtein(a, b)
    }
    return api_success(data)


# API Helpers

def api_success(data):
    json = jsonify(data)
    return api_response(json, status.HTTP_200_OK)


def api_error(message):
    json = jsonify({'error': message})
    return api_response(json, status.HTTP_400_BAD_REQUEST)


def api_response(data, status_code):
    response = make_response(data)
    response.mimetype = 'application/json'
    return response, status_code


if __name__ == '__main__':
    app.run()
