The Jubilant Pancake
--------------------
We would like to see a front end page that contains a two textfield form which when submitted sends two strings to a backend service. The backend service computes the edit distance between two strings (returns the minimum number of operations required to transform one string into another). The computed output is then returned to the end user.

Getting Started
---------------

```
cd jubilantPancake
pip install -r requirements.txt
python manage.py runserver

```

open index.html and enable CORS on browser

Todo: 

#. move request from frontend to node server
#. memoize requests
#. dockerize env
#. deploy on aws
