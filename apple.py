from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/dojos')
def dojos():
	return render_template("dojos.html")

@app.route('/dojos/new', methods=['POST'])
def new_ninja():
	print(request.form['first_name'])
	print(request.form['last_name'])
	print(request.form['email'])
	print(request.form['password'])
	print(request.form['gender'])
	print(request.form['favorite_language'])
	return redirect('/')

@app.route('/ninjas')
def ninjas():
	return render_template("ninjas.html")

app.run(debug=True)