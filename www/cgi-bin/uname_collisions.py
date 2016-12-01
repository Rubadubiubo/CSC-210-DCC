#!C:/Python27/python.exe

import cgi
import cgitb
import mysql.connector
import json

cgitb.enable()

def checkForCollisionsText(username):

	# query the database and check if the value is there
	conn = mysql.connector.connect(user='webConn', password='pass',
								host='127.0.0.1', database='WebApp')
	cursor = conn.cursor()

	data = cursor.execute('SELECT * FROM users WHERE username = %s', [username])

	if data.rowcount > 0:  # username already exists
		return 'collision'
	else:
    	return 'ok'

def main():
	print "Content-type: text/plain; charset=UTF-8\r\n\r\n"  # alls we need to send is one value
	username = cgi.FieldStorage()['username'].value  # username user has typed so far
	print checkForCollisionsText(username)

if __name__ == '__main__':
	main()







