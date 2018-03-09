from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'lakdjf;lakjdf;'

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/dojos')
def dojos():
	return render_template("dojos.html")

@app.route('/dojos/new', methods=['POST'])
def new_ninja():
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['email'] = request.form['email']
	session['password'] = request.form['password']
	return redirect('/view_info')

@app.route('/ninjas')
def ninjas():
	return render_template("ninjas.html")

@app.route('/view_info')
def view_info():
	user_fn = session['first_name']
	user_ln = session['last_name']
	user_email = session['email']
	user_pw = session['password']
	return render_template("view_info.html", first_name=user_fn, last_name=user_ln, email=user_email, pw=user_pw)

app.run(debug=True)