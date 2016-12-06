#!C:/Python27/python.exe

import os, cgi, cgitb; cgitb.enable()

fieldData = cgi.FieldStorage()
loginInfo = fieldData['username'].value
passInfo = fieldData['password'].value
returnHTML = "Error: return HTML not assigned"
##success html TBD
successfulHTML = "YES"
##Same as Login page HTML but with failed message
failedHTML = "<html><head><title>login here</title></head><body><h1 style=\"color:red;\">Login failed!</h1><br/><form action=\"/cgi-bin/login.py\" method=\"POST\"><h1>Username:</h1><br/><input type=\"text\" name=\"userfield\"/><h1>Password:</h1><br/><input type=\"password\" name=\"passwordfield\"/><br/><br/><input type=submit value=\"login\"/></form></body></html>"

def auth(login, password):
	return False
	
if auth(1, 0):
	returnHTML = successfulHTML
else:
	returnHTML = failedHTML

print 'Content-type: text/html\r\n\r\n'
for key in fieldData.keys():
	print fieldData[key].value
print returnHTML