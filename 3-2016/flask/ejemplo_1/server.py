from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/hello")
def hola():
	return "pepe"

@app.route('/contact')
def contact():
	return 'contact'

@app.route('/user/<username>')
def hello_user(username):
	return 'Hello! {}'.format(username)

@app.route('/sum/<int:n_one>/<int:n_two>')
def sum(n_one,n_two):
	return '{} + {} = {}'.format(n_one,n_two,n_one+n_two)



if __name__ == "__main__":
	app.run(debug=True)