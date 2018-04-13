from flask import Flask, render_template, request, session
from flask_session import Session
import datetime

app=Flask(__name__)

app.config['SESSION_PERMANENT']= False
app.config['SESSION_TYPE']='filesystem'
Session(app)

# notes=[]

@app.route('/',methods=['GET','POST'])
def note():
	if session.get('notes') is None:
		session['notes']=[]
	if request.method == "POST":
		newnote=request.form.get('note')
		session['notes'].append(newnote)
	return render_template('note.html',notes=session['notes'])

'''
@app.route('/')
def loops():
	names=['Ashish','Kapish','Swapnil']
	return render_template('page.html',names=names)

@app.route('/bdayform')
def bdayform():
	return render_template('page2.html')

@app.route('/birthday')
def bday():
	now=datetime.datetime.now()
	# print(now.month, now.day)
	birthday= now.month==2 and now.day==15
	return render_template('page1.html', birthday=birthday)

@app.route('/registeration',methods=['POST'])
def register():
	names=request.form.get("textnames")
	print(names)
	return render_template('page_hello.html',name=names)

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