My Jubilant Pancake
-------------------

This fork implements the assignment given below and satisfies the constraints given.

A few notes:

#. This is implemented in python 3.5.0
#. To run the example, clone the repo after the pull request is accepted and cd to the directory
#. Execute python3 jubilant.py
#. Point your browser to localhost:5555
#. There are no third-party library dependencies for python
#. The HTML page requires skeleton.css and it is pulled in from a CDN

In working on this assignment, it was my impression that you are not interested in
finding out if I can install Flask or Werkzeug and wrap a couple of views up.

Rather, I thought you would be interested in seeing what I can do using only Python's
baked-in tools. If I'm incorrect about these assumptions, I'll be happy to talk over
your thoughts and re-implement.

Thanks for your time.




The Jubilant Pancake
--------------------
We would like to see a front end page that contains a two textfield form which when submitted
sends two strings to a backend service. The backend service computes the edit distance between two strings
(returns the minimum number of operations required to transform one string into another). The computed output
is then returned to the end user.

Assignment Instructions
-----------------------
Fork this repo and when you are done with the assignment submit a pull request. Write an email (with url to the pull request included) to our HR
indicating you are done and the solution is ready for code review.)


Constraints
-----------
You must meet the following constraints in order for the project to be
considered valid:

#. No page reload
#. JSON dependent on both ends
#. Use Python as the server-side programming language
#. Do not use third-party libaries to compute the edit distance

Scoring
-------
Your code will be judged based on the following scoring system:

#. How well you've styled and used HTML/CSS on the frontend pages
#. How well the project is tested
#. How close your Python code adheres to PEP8 and PyLint ideals
