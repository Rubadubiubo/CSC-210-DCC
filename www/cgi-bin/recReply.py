#!C:/Python27/python.exe
#HASHBANG CHANGED FOR better COMPATIBILITY

import cgi
import cgitb
import mysql.connector
import Cookie
import hashlib
import datetime
import os
import cookie_handler
import json

cgitb.enable()

messageInfo = cgi.FieldStorage()

content = messageInfo['RepId'].value



conn = mysql.connector.connect(user='DCC', password='abcd', database='Ocean')
cursor = conn.cursor()
query = "SELECT Title, Data, Sent, Posttime, ReplyId FROM Replies WHERE mID='"+content+"'"
cursor.execute(query)
result = cursor.fetchall()
result = result[0]
jsonreturn = {"Title": result[0], "Data": result[1], "UnameSent": result[2], "Posttime": result[3], "ReplyId": result[4]}

conn.close()




print ("Content-type: text/html\n\n")
print json.dumps(jsonreturn)
