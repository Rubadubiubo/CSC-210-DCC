#!usr/bin/env python

import cgi
import cgitb
import mysql.connector
import hashlib

cgitb.enable()

def authenticate(username, password):
	'''
	Authenticates a password encrypted with timestamp using sha256
	encryption connected to a unique username.  Should return false
	if the username does not exist or if the password does not match
	records.
	'''

	# set up connection and get cursor
	conn = mysql.connector.connect(user='webConn', password='pass', host='127.0.0.1', database='WebApp')
	cursor = conn.cursor()

	# get user from database
	cursor.execute('SELECT * FROM users WHERE username = %s', [username])

	if cursor.arraysize != 1:  # no such username exists (usernames are unique)
		cursor.close()
		conn.close()
		return False

	else:
		user = cursor.next()
		encrypted = user[1]
		salt = user[2]

		# select hash function, and add the password and salt to the hasher
		hasher = hashlib.sha256()
		hasher.update(password)
		hasher.update(salt)

		# compute the hash
		digest = hasher.hexdigest()

		cursor.close()
		conn.close()
		return digest == encrypted

def main():
	# get the user data from the sent form
	login_data = cgi.FieldStorage()
	username = login_data['username'].value
	password = login_data['pass'].value

	if authenticate(username, password):
		print '''
		Content-type: text/html\r\n\r\n
		<html lang="en-us">
		<head>
			<meta charset="utf-8">
			<meta name="author" content="DCC, Inc.">
			<link rel="stylesheet" href="css/dccstyles.css">
			<title>Message In A Bottle</title>
		</head>
		<body>
		'''
		print '<p>Welcome, ' + username + '!'
		# probably more to add here, idk
		print '</body> </html>'

	else:  # redirect back to the login page with a name-value pair
		print "Location: login.html?status=failed"



if __name__ == "__main__":
	'''
	should only allow main to run if this file is run directly (rather
	then used within another file).  Usually good practice when using
	python.  If we needed to use the authenticate f(n) in another file,
	we could without running main().
	'''
	main()






