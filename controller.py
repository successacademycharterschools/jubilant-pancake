from flask import Flask, request, redirect, url_for, abort, render_template, Response, session, jsonify, make_response


app = Flask(__name__)
app.config['SECRET_KEY'] = "ssss"

def get_edit_distance(string1, string2, len1, len2):
	#Init matrix for DP
	"""
	table = [0] * (len1 + 1)
	for i in range(len2 + 1):
		table[i] * len2
	"""

	table = [[0 for x in range(len2+1)] for x in range(len1 + 1)]
	
	#i is len of string 1, j is length of string 2
	
	for i in range(len1 + 1):
		for j in range(len2 + 1):
			#First row/col of table is 0-len(string)
			
			#If string 1 is empty, need j operations
			if i == 0:
				table[i][j] = j
				
			#If string 2 is empty, need i operations
			elif j == 0:
				table[i][j] = i
			
			#If letter is different, take the minimum number of operations from surrounding diagonals			
			elif string1[i-1] != string2[j-1]:
				table[i][j] = 1+ min(table[i-1][j], table[i-1][j-1], table[i][j-1])
				
			#If letter is the same, number of operations is the same as previous. Get diagonal.
			else:
				table[i][j] = table[i-1][j-1]
				
				
	#Return last element 
	return table[i][j]

@app.route('/index', methods=['GET', 'POST'])
def index():

	edit_distance = 0
	
	if request.method == 'POST':
		print("POST: contentType", request.content_type)
		if request.content_type != "application/json":
			response = make_response(render_template('index.html', edit_distance = edit_distance))
			return response
		array_data = request.get_json()
		data = {}
		for item in array_data:
			data[item['name']] = item['value']
	
		string1 = data.get('string1')
		string2 = data.get('string2')
		
		print(string1, string2)
		
		
		edit_distance = get_edit_distance(string1, string2, len(string1), len(string2))
			
		print('EDIT: ', edit_distance)
			
		response = make_response(render_template('index.html', edit_distance = edit_distance))
		print(response.content_type)
		return response
	
	else:
		print("non-POST")
		response = make_response(render_template('index.html', edit_distance = edit_distance))
		return response
		
	

			
				
			
		
	
	
	