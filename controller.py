from flask import Flask
from flask import render_template
from form import MainForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "ssss"

@app.route('/')
def index():
	form = MainForm()
	return render_template('index.html', form = form)
	
	