
from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['GET'])
def BMI():
	height=float(input("enter your height in m: "))
	weight=float(input("enter your weight in kgs: "))
	Index=weight/(height)**2
	return(str(Index))
	
if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8000,debug=True)
