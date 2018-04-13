from flask import Flask, render_template
import datetime

app=Flask(__name__)

@app.route('/')
def loops():
	names=['Ashish','Kapish','Swapnil']
	return render_template('merapage.html',names=names)

@app.route('/birthday')
def bday():
	now=datetime.datetime.now()
	# print(now.month, now.day)
	birthday= now.month==2 and now.day==15
	return render_template('merapage1.html', birthday=birthday)
'''
@app.route('/')
def index():
	headline = "ashish"
	return render_template('merapage.html',headline=headline)
@app.route("/")
def index():
    return "Hello, world!"

@app.route('/ashish')
def ashish_hello():
	return "Bhiya raom!"

@app.route('/<string:name>')
def habhai(name):
	name=name.capitalize()
	return f'<h1>Ha bhai {name}</h1>
'''

if __name__=='__main__':
	app.run(debug=True)