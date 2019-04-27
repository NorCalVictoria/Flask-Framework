from flask import Flask , jsonify

app = Flask(__name__)

@app.route('/')           #decorator (default en requests : GET only )
def index():
	return '<h1>Hello, World!</h1>'   #function (what to do when someone routes to here )

@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Citizen'})
                  #input from user'name'
@app.route('/home/<name>', methods=['GET', 'POST']) # GET & POST permissions (route methods)
def home(name):
	return '<h1>{}, You landed on the home page . Nice one!</h1>'.format(name) 

@app.route('/json')
def json():
	return jsonify({'key' : 'value', 'key2' : [1,2,3]})

 





if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

 