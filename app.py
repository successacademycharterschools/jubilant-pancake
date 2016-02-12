from flask import Flask, jsonify, render_template, request, abort
import json
import distance

app = Flask(__name__, static_url_path="")

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gomix', methods=['POST'])
def ajax():
        if not request.json:
            abort(400)
        else:
            ingredient1 = request.json.get('ingredient1')
            ingredient2 = request.json.get('ingredient2')
            edit_distance = distance.levenshtein(ingredient1, ingredient2)
            return jsonify({'distance': edit_distance})

if __name__ == "__main__":
    app.run(debug=True)

