from flask import Flask ,render_template,request,redirect,flash
# from flask_sqlalchemy import SQLAlchemy
# import json

app = Flask(__name__)
# app.secret_key = 'super-secret-key'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3308/portfolio'
# db = SQLAlchemy(app)
#
# class Contacts(db.Model):     #will define the tables of sql
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(40), unique=False, nullable=False)
#     email = db.Column(db.String(50), unique=False, nullable=False)
#     msg = db.Column(db.String(100), unique=False, nullable=False)

@app.route('/')
def myHome():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)



def write_to_file(data):
	with open('database.txt','a') as database:
		email= data['email']
		name= data['name']
		message= data['message']
		file = database.write(f'\n {name} , {email} , {message} ')


@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
	if request.method == 'POST':
			# name = request.form.get('name')
			# email = request.form.get('email')
			# message = request.form.get('message')
			# entry = Contacts(name=name, email=email,msg=message)
			# db.session.add(entry)
			# db.session.commit()
			try:

				data = request.form.to_dict()

				write_to_file(data)
				return redirect('/contacts.html')
			except:
				return 'Something went wrong not able to connect to the database!'
			else:
				return 'Something went wrong visit after some time.'

app.run(debug=True)