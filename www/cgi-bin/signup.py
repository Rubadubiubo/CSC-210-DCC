#!/usr/bin/python2.7


#CC
import cgitb
import cgi
import mysql.connector
import hashlib
import datetime
import Cookie
import datetime
import os
import cookie_handler

from home import generateUserAccountPage  # the function that generates the user's page after successful login
from mysql.connector import errorcode


#import home.generateUserAccountPage  # the function that generates the user's page after successful login


cgitb.enable()


def insert_user(username, password):
    salt = str(datetime.datetime.now())

    hasher = hashlib.sha256()
    hasher.update(password)
    hasher.update(salt)
    encrypted = hasher.hexdigest()

    conn = mysql.connector.connect(user='this', database='Ocean')
    cursor = conn.cursor()
    add_user = ("""INSERT INTO Users
            (UserName, Pass, Salt, UID)
            VALUES (%s, %s, %s, %s)""")
    userToAdd = (username, encrypted, salt, "1")

    cursor.execute(add_user, userToAdd)
    conn.commit()

    cursor.close()
    conn.close()



def dupliCheck(username):
    #conn = mysql.connector.connect(user='sudoAppli', password='pass',
    #                          host='127.0.0.1',
    #                           database='Ocean')


    try:
        conn = mysql.connector.connect(user='this', database='Ocean')
    
    except mysql.connector.Error as err:
        print("Content-type: text/html\n\n")
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            #return false
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            #return False
        else:
            #return false
            
            print(err)
    else:
        cursor = conn.cursor(buffered=True)

        query = ("SELECT * FROM Users "
        "WHERE UserName='" + username+ "'")
        
        a = cursor.execute(query)
        if cursor.rowcount >= 1:
            cursor.close()
            conn.close()
            return False
        return True




    

    


#Code here
form = cgi.FieldStorage()
    
username = form['username'].value
password = form['password'].value

if dupliCheck(username):
    insert_user(username, password)
    cookie_handler.generateLoginCookieHeader(username)
    generateUserAccountPage(username)
else:
    print("Content-type: text/html\n\n")
    print("Username already taken.")
   





