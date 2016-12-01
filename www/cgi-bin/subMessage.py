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

cgitb.enable()

#get message data
messageInfo = cgi.FieldStorage()

content = ""
title = ""
posttime = str(datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")) #If no timestring sent, assume current time
anon = ""

if 'message' in messageInfo:
	content = messageInfo['message'].value
if 'title' in messageInfo:
	title = messageInfo['title'].value
if 'posttime' in messageInfo:
	posttime = messageInfo['timestamp'].value #Naming posttime because 'Timestamp' is a reserved keyword in Python
if 'anon' in messageInfo:
	anon = messageInfo['anon'].value
if (anon == "false" or anon == "False"):
	username = cookie_handler.readLoginCookieHeader()
else:
	username = ""
conn = mysql.connector.connect(user='this', database='Ocean')
cursor = conn.cursor()
add_Message = ("""INSERT INTO Messages
        (Data, Title, Posttime, UnameSent)
        VALUES (%s, %s, %s, %s)""")
messageToAdd = (content, title, posttime, username)

cursor.execute(add_Message, messageToAdd)
conn.commit()

cursor.close()
conn.close()

print("Content-type: text/html\n\n")
print("Message Submitted"+" anon is: "+anon)
