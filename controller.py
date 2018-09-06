import os
from flask import Flask, request, render_template, Response, jsonify, make_response, json



app = Flask(__name__)

def get_edit_distance(string1, string2, len1, len2):
	#Init matrix for DP
    table = [[0 for x in range(len2+1)] for x in range(len1 + 1)]
	
	#i is len of string 1, j is length of string 2
    #First row/col of table is 0-len(string)
    for i in range(len1 + 1):
        for j in range(len2 + 1):
			
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
				
				
	#Return last element: minimum number of operations to convert the whole string
    return table[i][j]

@app.route("/index", methods=["GET", "POST"])
def index():

    edit_distance = 0
    response = make_response(render_template("index.html", edit_distance = edit_distance))
	
    if request.method == "POST":
        print("POST: contentType", request.content_type)
        
        #If we receive non-JSON (invalid content type), render the page and return.
        if request.content_type != "application/json":
            return response
            
        #Extract string1 and string2 from JSON request
        json_request = request.get_json()
        data = {}
        for item in json_request:
            data[item["name"]] = item["value"]
	
        string1 = data.get("string1")
        string2 = data.get("string2")
		
        #Calculate edit distance, create JSON map for response.
        edit_distance = str(get_edit_distance(string1, string2, len(string1), len(string2)))
        data = {"string1":string1, "string2":string2, "edit_distance":edit_distance}

        #Return response as JSON. 
        return jsonify(data)
	
	
    #If request method is GET, just render the page.
    return response


if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)	
		
	

			
				
			
		
	
	
	