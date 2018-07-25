The Jubilant Pancake
-----------------------
The purpose of this project is to take two strings and calculate the edit distance (the least amount of operations it takes to transform one string into another).  This project uses Python 2.7.6 as the server-side language and Angular 1.2.

File-List
-----------------------
- __init__.py 								Treats this project as an package
- app.py 									Webservice that contains core function "getEditDistance" as well as routes to display the page
- static/css/styles.css 					Main Style-Sheet
- static/javascript/angular-animate.js 		3rd Party plugin for fade-effects
- static/javascript/angular.min.js 			Main file that provides Angular functionality
- static/javascript/service.js 				Service file that makes the rest-call to "getEditDistance"
- templates/appForm.html 					Main html file
- test_app.py 								Unit-test service to test multiple test-cases


Explanation of how we are calculating the distance between two strings
-----------------------------------------------------------------------------------------
https://en.wikipedia.org/wiki/Levenshtein_distance


Unit-tests
-----------------------
- testStrsEqual()			Tests cases to see if two strings are equal
- testStrBlank				Test cases to see if one string is blank. (NOTE: We do not allow two null strings.  This is blocked in service.js)
- test2Strings				Test cases to check two or more strings.

To run the test cases:
Go to your project root and enter:
python test_app.py