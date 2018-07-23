#!flask/bin/python

from flask import Flask, request, json, jsonify
app = Flask(__name__)

# Service to actually recieve and test the string
@app.route('/test_string', methods=['POST'])
def testString():
	# Retrieving our request parameters & decoding them
	requestParams = request.get_json()
	str1 = requestParams['str1']
	str2 = requestParams['str2']


	return jsonify({'str1': str1, 'str2': str2}), 201



if __name__ == '__main__':
	app.debug = True
	app.run(port=5002)
	# app.run(port=5002)