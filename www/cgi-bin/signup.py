#!/usr/bin/env python
#CC
import cgitb
import cgi
import mysql.connector
import hashlib
import datetime

import home.generateUserAccountPage  # the function that generates the user's page after successful login

def insert_user(username, password):
    salt = str(datetime.datetime.now())

    hasher = hahlib.sha256()
    hasher.update(password)
    hasher.update(salt)
    encrypted = hasher.hexdigest()

    conn = mysql.connector.connect(user='webConn', password='pass',
                               host='127.0.0.1',
                               database='WebApp')
    cursor = conn.cursor()
    add_user = ("INSERT INTO users"
            "(username, pass, salt)"
            "VALUES (%s, %s, %s)")
    userToAdd = (username, password, salt)

    cursor.execute(add_user, userToAdd)
    conn.commit()

    cursor.close()
    conn.close()



def dupliCheck(username):
    conn = mysql.connector.connect(user='webConn', password='pass',
                               host='127.0.0.1',
                               database='WebApp')
    cursor = conn.cursor()

    a = cursor.execute("SELECT * FROM pizza_orders WHERE username=?", [username])
    if (len(a) >= 1):
        return false
    return true


#Code here
form = cgi.FieldStorage()
    
username = form['username'].value
password = form['password'].value

if(dupliCheck(username)):
    insert_user(username, password)
    generateUserAccountPage(username)

else:
    
    tryAgain = "/create_account.html?status=failed"
    print 'Location: %s' % tryAgain
   





