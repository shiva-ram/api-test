'''
height=float(input("enter your height in m: "))
weight=float(input("enter your weight in kgs: "))
BMI=weight/(height)**2
print(BMI)
'''
'''
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods=['GET'])
def BMI():
	height=float(input("enter your height in m: "))
	weight=float(input("enter your weight in kgs: "))
	Index=weight/(height)**2
	return(Index)
	
app.run()
'''
from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name
@app.route('/', methods=['GET'])
def BMI():
	height=float(input("enter your height in m: "))
	weight=float(input("enter your weight in kgs: "))
	Index=weight/(height)**2
	return(str(Index))
	
if __name__ == '__main__':
   app.run(host='0.0.0.0/0',port=8000,debug=True)
