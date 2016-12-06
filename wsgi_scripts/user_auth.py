'''
This is a blueprint, which contains other functions for creating other pages.  It helps to properly separate
the app into different files in order to better keep track of where things are.
'''
from flask import request, Blueprint, redirect, url_for, current_app, make_response, abort
import hashlib
from datetime import datetime
import mysql.connector
from aux_functions import modify30DayLoginCookie
from random import choice

user_auth = Blueprint('user_auth', __name__)

@user_auth.route('/login_processing/', methods = ['POST'])
def login_processing():
	if request.referrer not in [url_for('login', _external=True), url_for('login', failed="failed", _external=True)]:
		abort(403)

	username = request.form['username']
	rawpswd = request.form['password']

	# User: DCC  Pawssword: DCCInfinity
	# get MySQL cursor and desired login data
	conn = mysql.connector.connect(user='DCC_NoPswd', host='localhost', database='Ocean')
	cursor = conn.cursor(buffered = True)
	cursor.execute("SELECT Pass, Salt FROM Users WHERE UserName=%s", [username])
	if cursor.rowcount == 0:
		cursor.close()
		conn.close()
		return redirect(url_for('login', failed = 'failed'))  # no such username

	user = cursor.fetchone()
	password = user[0]
	salt = user[1]

	hasher = hashlib.sha256()
	hasher.update(rawpswd.encode('utf-8'))
	hasher.update(salt.encode('utf-8'))
	encpswd = hasher.hexdigest()

	# check password
	if password == encpswd:  # login successful
		cursor.close()
		conn.close()
		redir = redirect(url_for('user_site.user_home'))
		return modify30DayLoginCookie(request, redir, user=username, addIfNotExists=True)  # add cookie here

	else:  # login failed
		cursor.close()
		conn.close()
		return redirect(url_for('login', failed = 'failed'))


@user_auth.route('/signup_processing/', methods=['POST'])
def signup_processing():
	if request.referrer not in [url_for('signup', _external=True)]:
		abort(403)

	# get form data
	username = request.form['username']
	password = request.form['password']

	conn = mysql.connector.connect(user='DCC_NoPswd', host='localhost', database='Ocean')
	cursor = conn.cursor()

	# hash the password
	hasher = hashlib.sha256()
	hasher.update(password.encode('utf-8'))
	# no need to check for collisions, because form would not have been submitted if there was one
	cursor.execute("INSERT INTO Users (UserName, Pass, Salt) VALUES (%s, %s, %s)", 
		[username, hasher.hexdigest(), datetime.utcnow()])
	conn.commit()
	cursor.close()
	conn.close()

	redir = redirect(url_for('user_site.user_home'))
	return modify30DayLoginCookie(request, redir, user=username, addIfNotExists=True)  # log the user in and send them home


@user_auth.route('/uname_collision_check/', methods=['POST'])
def uname_collision_check():
	if request.referrer not in [url_for("signup", _external = True)]:
		abort(403)
	username = request.form['username']
	conn = mysql.connector.connect(user='DCC_NoPswd', host='localhost', database='Ocean')
	cursor = conn.cursor(buffered=True)
	cursor.execute("SELECT * FROM Users WHERE UserName=%s", [username])
	if cursor.rowcount > 0:  # just a placeholder
		data = 'collision'
	else:
		data = 'ok'

	cursor.close()
	conn.close()
	return current_app.make_response(data)  # return the correct string for the ajax




