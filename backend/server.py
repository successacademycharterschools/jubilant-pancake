from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    response = jsonify({'some':'data'})
    # for a code test, just let cors through. 
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
