from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return "There's no reason this shouldn't work."


application = app