Quick Setup: AWS Ubuntu 14.04 AMI with Anaconda
---------------------
As user **ubuntu**

* cd /home/ubuntu
* wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
* chmod u+x Miniconda3-latest-Linux-x86_64.sh
* ./Miniconda3-latest-Linux-x86_64.sh
* source .bashrc
* sudo apt-get install git
* mkdir -p apps
* cd apps
* git clone https://github.com/todmitry/jubilant-pancake.git
* cd jubilant-pancake
* conda env create -f config/requirements.yml
* chmod go-wrx config
* source activate py35c
* nohup python webapp.py &

There is also a config/requirements.txt file for use with pip instead of Anaconda.

Quick Build
-----------
* npm install
* npm run build


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
