from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
	name= StringField('Name',validators=[DataRequired('A name is required!')])
	email= StringField('Email Address',validators=[DataRequired('A email Address is required!')])
	subject= StringField('Subject',validators=[DataRequired('A subject is required!')])
	message= TextAreaField('Message', validators=[DataRequired('A message is required')])
	submit= SubmitField('send')