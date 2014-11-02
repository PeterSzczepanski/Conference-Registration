from flask import render_template, request, redirect, url_for, flash
from app import app
import forms

# Realtime Scalable Database, returns JSON. Easily integrate with mobile apps later.
from firebase import firebase
firebase = firebase.FirebaseApplication('https://dazzling-inferno-8618.firebaseio.com/', None)

@app.route('/')
@app.route('/index')
def index():
	return render_template("intro.html")

@app.route('/home')
def info():
	info = firebase.get('/conference', 0)
	return render_template("home.html",
		title = "Home",
		info = info)

@app.route('/clients')
def showClients():
	clients = firebase.get('/clients', None)
	return render_template("clients.html",
		title = "Clients",
		clients = clients
		)

@app.route('/attendees')
def showAttendees():
	attendees = firebase.get('/attendees', None)
	return render_template("attendees.html",
		title = "Attendees",
		attendees = attendees)

@app.route('/register')
def register():
	return render_template("register.html",
		title = "Registration")

@app.route('/register/client', methods=['GET', 'POST'])
def regClient():
	form = forms.ClientRegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		firebase.post('/clients', {'Id': getNewClientId(), 'Name':form.name.data, 'Email':form.email.data, 'Phone':form.phone.data,
		 'Street':form.street.data,'City':form.city.data,'State':form.state.data,'ZipCode':form.zipCode.data})
		flash('SUCCESSFUL: Thank you for registering.')
		return redirect('/clients')
	return render_template("regClient.html",
		title = "Client Registration",
		type="Client", form=form)

@app.route('/register/attendee', methods=['GET', 'POST'])
def regAttendee():
	form = forms.AttendeeRegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		firebase.post('/attendees', {'ClientId':form.clientId.data, 'Name':form.name.data, 'Email':form.email.data})
		flash('SUCCESSFUL: Thank you for registering.')
		return redirect('/attendees')
	return render_template("regAttendee.html",
		title = "Attendee Registration",
		type="Attendee", form=form)

def getNewClientId():
	attendees = firebase.get('/clients', None)
	return len(attendees) + 1
