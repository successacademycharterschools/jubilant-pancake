import os
import sys

# Add the local server/lib/ directory to path for import purposes.
lib_path = os.path.join(os.path.dirname(__file__), 'lib')
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)


import json

from flask import Flask
from flask import render_template
from flask import request

from utils import med


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    '''
    Load the base template
    '''
    return render_template('index.html')

@app.route('/api/edit-distance/', methods=['POST'])
def edit_distance():
    '''
    Take two strings and return the minimum-edit-distance between them

    Method: POST
    Params:
      - str1 - the first string we want to compare, if not provided, defaults to
               ''
      - str2 - the second string we want to compare, if not provided, defaults
               to ''

    Returns:
      A JSON object with one key "steps" and an integer value representing the
      edit distance between the two strings.
    '''
    data = json.loads(request.data)
    str1 = data.get('str1', '')
    str2 = data.get('str2', '')

    result = {
        'steps': med(str1, str2)
    }

    return json.dumps(result)



if __name__ == '__main__':
    app.run()
