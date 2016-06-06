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


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/edit-distance/', methods=['POST'])
def edit_distance():
    data = json.loads(request.data)
    str1 = data.get('str1', '')
    str2 = data.get('str2', '')

    result = {
        'step_count': 3,
        'steps': [
            'a',
            'ab',
            'abc',
        ],
    }
    return json.dumps(result)



if __name__ == '__main__':
    app.run()
