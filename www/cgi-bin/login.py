#!/usr/bin/python2.7
#HASHBANG CHANGED FOR LINUX COMPATIBILITY

import cgi
import cgitb
import mysql.connector
import Cookie
import hashlib
import datetime
import os
import cookie_handler

from home import generateUserAccountPage  # function creating the home page

cgitb.enable()

def authenticate(username, password):
	#'''
	#Authenticates a password encrypted with timestamp using sha256
	#encryption connected to a unique username.  Should return false
	#if the username does not exist or if the password does not match
	#records.
	#'''

	# set up connection and get cursor
	conn = mysql.connector.connect(user='DCC', password='abcd', database='Ocean')
	cursor = conn.cursor(buffered=True)

	# get user from database
	query = ("SELECT * FROM Users "
        "WHERE UserName='" + username+ "'")
	
	cursor.execute(query)

	if cursor.rowcount < 1:  # no such username exists (usernames are unique)
                #print (cursor._last_executed)
		cursor.close()
		conn.close()
		return False

	else:
                
		user = cursor.next()
		#print(user)
		#print("are in User")
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
		#print(digest + "\n")
		#print("               BREAKKKK            ")
		#print(salt + "\n")
		return digest == encrypted

def main():
       
	# get the user data from the sent form
	login_data = cgi.FieldStorage()
	username = login_data['username'].value
	password = login_data['password'].value

	if authenticate(username, password):
		cookie_handler.generateLoginCookieHeader(username)
		# generateUserAccountPage(username)
		print("Content-type: text/html\n\n")
		print("true")

	else:  # redirect back to the login page with a name-value pair
		#print "Location: ../login.html?status=failed"

		print("Content-type: text/html\n\n")
		# print("Authentication Failed")
		print("false")



if __name__ == "__main__":
	'''
	should only allow main to run if this file is run directly (rather
	then used within another file).  Usually good practice when using
	python.  If we needed to use the authenticate f(n) in another file,
	we could without running main().
	'''
	main()






