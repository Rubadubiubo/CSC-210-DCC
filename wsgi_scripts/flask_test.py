from flask import Flask

development = False  # for running on flask development server (True) OR in production (False)
# changing this will allow developer to change between the development server packaged with flask and wsgi

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World'

@app.route('/wsgi_test/')
def wsgi_routing_test():
	return 'WSGI routing test was successful if the above url is localhost/scripts/flask_test.py/wsgi_test/.'

# the following can be cut and pasted into different applications and should still work
if development:  # run in development
	if __name__ == '__main__':
		app.run(debug = True)
else:  # run in production with wsgi
	# wsgi accepts the Flask instance as a callable object called application
	application = app