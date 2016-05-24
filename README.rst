The Jubilant Pancake
--------------------
We would like to see a front end page that contains a two textfield form which when submitted
sends two strings to a backend service. The backend service computes the edit distance between two strings
(returns the minimum number of operations required to transform one string into another). The computed output
is then returned to the end user.

Installing the Node app
-----------------------

In `Node` folder

:code:`node install`

:code:`node index.js`

This initializes the Node-powered front-end page on port 3000

Installing the Angular app
--------------------------

In `Angular2` folder

:code:`node install`

:code:`gulp`

This initializes the Angular-powered front-end page on port 8000

*Alternatively, you can copy the contents of `Angular2/app` folder into `Node/public` folder. This way, you only need to run the Node app to view the page*