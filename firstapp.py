from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config['DEBUG'] = True # without this errors cause site to crash

#
@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/')
def index():
    return render_template('base.html')


# example of using html template and 
@app.route('/sayhello/<name>')
def sayhello(name):
	return render_template('me.html', name = name)

# lil' taste of html
@app.route('/name/<yourName>')
def myName(yourName):
	return "<h1>"+yourName+"</h1>"

# returns true if x or y has a character in it
# caesar said creating and calling functions like this
# will be the bulk of what we work on
def checkAlpha(x,y):
	if x.isalpha() or y.isalpha():
		return True

# performs operations on the x and y included in url 
# don't use carrot brackets when typing the url
@app.route('/add/<x>/<y>')
def add(x,y):
	if checkAlpha(x,y):
		return "ERROR"
	return "The sum is " + str(int(x)+int(y))

@app.route('/sub/<x>/<y>')
def sub(x,y):
	if checkAlpha(x,y):
		return "ERROR"
	return "The difference is " + str(int(x)-int(y))

@app.route('/mult/<x>/<y>')
def mult(x,y):
	if checkAlpha(x,y):
		return "ERROR"
	return "The product is "+str(int(x)*int(y))

@app.route('/div/<x>/<y>')
def div(x,y):
	if checkAlpha(x,y):
		return "ERROR"
	return "The quotient is "+ str(int(x) / int(y))

if __name__ == "__main__":
	app.run()