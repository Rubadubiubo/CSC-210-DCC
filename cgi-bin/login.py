#!usr/bin/env python

import cgi
import cgitb
import sqlite3
import hashlib

cgitb.enable()

account_data = cgi.FieldStorage()

def authenticate(username, password):
	'''
	Authenticates a password encrypted with timestamp using sha256
	encryption connected to a unique username.  Should return false
	if the username does not exist or if the password does not match
	records.
	'''

	# set up connection and get cursor
	conn = sqlite3.connect('users.db')
	cursor = conn.cursor()

	# get user from database
	users = cursor.execute('SELECT * FROM users WHERE username = ?', [username])

	if users.arraysize != 1:  # no such username exists (usernames are unique)
		conn.close()
		return False

	else:
		user = users.next()
		encrypted = user[1]
		salt = user[2]

		# select hash function, and add the password and salt to the hasher
		hasher = hashlib.sha256()
		hasher.update(password)
		hasher.update(salt)

		# compute the hash
		digest = hasher.hexdigest()

		conn.close()
		return digest == encrypted



login_data = cgi.FieldStorage()

