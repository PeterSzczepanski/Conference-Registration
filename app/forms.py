from wtforms import Form, BooleanField, TextField, PasswordField, validators, IntegerField, SelectField, StringField
from wtforms.validators import InputRequired, Email, Regexp, Required
from wtforms.fields.html5 import EmailField

from firebase import firebase
firebase = firebase.FirebaseApplication('https://dazzling-inferno-8618.firebaseio.com/', None)


class AttendeeRegistrationForm(Form):
	name = TextField("Name", validators=[InputRequired('Please enter your name.')])
	email = EmailField("Email",  validators=[InputRequired("Please enter your email address."), Email("Please enter your email address.")])
	clientId = IntegerField('Client #', [validators.NumberRange(min=1, max=len(firebase.get('/clients', None))), InputRequired("Please enter your client id.")])


class ClientRegistrationForm(Form):
	name = TextField("Name", validators=[InputRequired('Please enter your name.')])
	email = EmailField("Email",  validators=[InputRequired("Please enter your email address."), Email("Please enter your email address.")])
	phone = TextField('Phone (###-###-#### format)', validators= [validators.Length(min=6, max=35), Regexp('^\d{3}-\d{3}-\d{4}$'), InputRequired("Please enter your number in 111-222-3333 format.")])
	street = TextField('Street', validators=[InputRequired('Please enter your street.'), validators.Length(min=4, max=35)])
	city = TextField('City', validators=[InputRequired('Please enter your city.'), validators.Length(min=2, max=15)])
	state = TextField('State (Abbreviation)', validators=[InputRequired('Please enter your state\'s two letter abbreviation.'), Regexp('^[A-Za-z]{2}$')])
	zipCode = TextField('Zip Code', validators=[InputRequired('Please enter your zipcode.'), Regexp('^\d{5}$')])
