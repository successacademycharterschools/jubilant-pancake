import os
from flask import Flask, request, render_template, Response, jsonify, make_response, json

"""
Flask server to receive two strings from front end index.html in JSON form.

Computes the edit distance between the two strings and returns a JSON response containing the computed value. 
"""

#Create an instance of imported Flask class. "Name" is the name of application package.
app = Flask(__name__)

def get_edit_distance(string1, string2, len1, len2):
    """
    Use Dynamic Programming to calculate the Edit Distance between two Strings.
    
    Takes in two strings and their lengths as arguments. Returns an integer value representing the minimum number of operations
    needed to convert one string to the other.
    Initialize a matrix of size len(string1) * len(string2) to store values of previously computed edit distances. 
    """
    
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
    """
    Main routing function. 
    
    When the user accesses "/index" this function is called. The "route" dectorator binds the "/index" url to
    this function. Uses both GET and POST HTTP methods when accessing "/index". Upon GET request, this function will
    simply render the base "index.html" file and return. Upon a POST request, we first confirm that the request is in 
    JSON form, and if so, we parse the JSON request and retrieve the two strings. We then compute the edit distance and
    send back a JSON response. If the request is not in JSON form we render the base "index.html" file and return.
    """

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
    """
    Main function, runs the Flask application on localhost:5000.
    """
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)	
		
	

			
				
			
		
	
	
	