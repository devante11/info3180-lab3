from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, Submitfield
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
	name= TextField('Name' validators=[DataRequired('A name is required!')])
	email= TextField('Email Address'validators=[DataRequired('A email Address is required!')])
	subject= TextField('Subject'validators=[DataRequired('A subject is required!')])
	message= TextAreaField('Message' validators=[DataRequired('A message is required')])
	submit= Submifield('send')