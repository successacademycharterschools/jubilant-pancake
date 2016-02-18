# Python
from os import environ

# External
from distance import levenshtein
from flask import abort, Flask, jsonify, render_template, request

# Local
from exceptions import InvalidUsage

app = Flask(__name__)
app.debug = True

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/edit_distance', methods=['POST'])
def edit_distance():
    if not request.json:
        raise InvalidUsage('Requires JSON')

    data = request.get_json()
    edit_distance = levenshtein(data['word1'], data['word2'])
    response = {
        'word1': data['word1'], 
        'word2': data['word2'], 
        'edit_distance': edit_distance
    }
    return jsonify(**response)

if __name__ == '__main__':
    port = int(environ.get('PORT', 3000))
    app.run(port=port)
