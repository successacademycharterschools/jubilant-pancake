The Jubilant Pancake
--------------------
We would like to see a front end page that contains a two textfield form which when submitted
sends two strings to a backend service. The backend service computes the edit distance between two strings
(returns the minimum number of operations required to transform one string into another). The computed output
is then returned to the end user.

This app includes:
Sass, Babel, Webpack, Angular, Node, and ES2015

* To run app - type in ``npm run dev`` into command line within the app.

Testing is done with Tape:
https://github.com/substack/tape

* To run unit test in the app run ``node -r babel-register src/tests/test.js`` into the command line.
