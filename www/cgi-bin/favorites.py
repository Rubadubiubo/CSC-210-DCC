#!C:/Python27/python.exe

import cgi
import cgitb
import mysql.connector
import Cookie
import hashlib
import datetime
import os
import cookie_handler

cgitb.enable()

conn = mysql.connector.connect(user='DCC', password='abcd', database='Ocean')
query = "Select * FROM Favorites WHERE "