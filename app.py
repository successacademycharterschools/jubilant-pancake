from flask import Flask, request, json, jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('appForm.html')


# Service to actually recieve and test the string
@app.route('/test_string', methods=['POST'])
def testString():
	# Retrieving our request parameters & decoding them
	requestParams = request.get_json()
	str1 = requestParams['str1']
	str2 = requestParams['str2']

	moves = getEditDistance(str1, str2)

	return jsonify({'moves': moves}), 201


# function to actually calculates edit distance of 2 strings
def getEditDistance(str1, str2):

	# if both strings are equal, return 0
	if str1 == str2:
		return 0

	# if str1 if empty, then return str2 len
	# NOTE: this means we move all characters from str1 to str2
	if len(str1) == 0:
		return len(str2)

	# if str1 if empty, then return str2 len
	# NOTE: this means we move all characters from str1 to str2
	if len(str2) == 0:
		return len(str1)

	# Actual do matrix
	# x coordinates
	xCoorLen = len(str1) + 1

	# y coordinates
	yCoorLen = len(str2) + 1

	# creating a matrix
	matrix = [[-1 for i in range(xCoorLen)] for j in range(yCoorLen)]

	# looping through
	for i in range(xCoorLen):
		matrix[0][i] = i

	for j in range(yCoorLen):
		matrix[j][0] = j

	# Doing actual range
	for i in range(1, yCoorLen):
		for j in range(1, xCoorLen):
			# if str1 char & str2 char are equal, then use upper-left char to current
			if str1[j - 1] == str2[i - 1]:
				matrix[i][j] = matrix[i - 1][j - 1]
			else:
				# if str1 char & str2 char aren't equal, then use minimum of upper-left, upper-current, & current-left chars
				matrix[i][j] = min(
									matrix[i - 1][j] + 1,
									matrix[i][j - 1] + 1,
									matrix[i - 1][j - 1] + 1
								)

	# return the bottom-right corner of the matrix - this is our distance
	return matrix[yCoorLen - 1][xCoorLen - 1]


if __name__ == '__main__':
	app.debug = True
	app.run(port=5002)
	# app.run(port=5002)