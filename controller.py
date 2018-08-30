from flask import Flask, request, render_template
from form import MainForm


app = Flask(__name__)
app.config['SECRET_KEY'] = "ssss"

@app.route('/', methods=['GET', 'POST'])
def index():
	form = MainForm()
	if request.method == 'POST':
		string1 = request.form.get('string1')
		string2 = request.form.get('string2')
		
		return '''<h1> String1 is: {}</h1>
				  <h1> String2 is: {}</h2>'''.format(string1, string2)
	return render_template('index.html', form = form)
	
	