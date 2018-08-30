from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MainForm(FlaskForm):
	string1 = StringField('First String', validators=[DataRequired()])
	string2 = StringField('Second String', validators=[DataRequired()])
	submit = SubmitField('Get Edit Distance')
	