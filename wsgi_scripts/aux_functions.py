from flask import request, make_response, redirect, url_for
from datetime import datetime, timedelta
import mysql.connector
import hashlib

from random import choice


def get30CharRandomStr():
	return "".join(list(choice('0123456789abcdefghijklmnopqrstuvwxyz!@#$^&*()=+-[]') for i in range(30)))


def modify30DayLoginCookie(request, rendered_template, user = '[None]', add = True, addIfNotExists = False):
	''' returns a response containing a 30-day cookie keeping the user logged in
	the parameters are:
	1. a request which may or may not contain a cookie ('previous_login')
	2. a template rendered using the render_template function included in flask
	3. a boolean indicating whether the cookie is to be added or removed in the operation
	4. a boolean indicating whether the cookie should be added if not already in request

	The defaults should be sufficient to a standard cookie-driven replacement for render_template:
	the function, if supplied only with request and rendered_template, should renew the cookie
	if it already exists addIfNotExistsd do nothing otherwise.
	'''
	# debug
	#import inspect
	#print(inspect.stack())

	resp = make_response(rendered_template)
	exp_time = datetime.utcnow()

	if add == True:  # add the cookie
		if 'user_logged' not in request.cookies:
			if addIfNotExists == False:  # otherwise user is set already
				return resp  # response returned without adding cookie
			addNewId = True
		else:
			user = request.cookies['user_logged']  # reset cookie as previous username
			#return make_response(user)
			addNewId = False
		exp_time = exp_time + timedelta(30)
	else:  # remove the cookie
		exp_time = exp_time - timedelta(30)
		# cookie will immediately be removed since it expired 30 days ago
		addNewId = None  # id will be removed
	
	conn = mysql.connector.connect(user='DCC_NoPswd', host='localhost', database='Ocean')
	cursor = conn.cursor(buffered=True)

	if addNewId == True:  # must add a new key
		#return make_response("addNewId == True")
		cookie_pass = get30CharRandomStr()
		cookie_salt = get30CharRandomStr()
		login_id = get30CharRandomStr()

		query = "SELECT * FROM User_Login_Keys WHERE LoginId = %s"
		cursor.execute(query, [login_id])
		while cursor.rowcount != 0:  # to get a unique string (are over 10^45 possibilities)
			login_id = get30CharRandomStr()
			cursor.execute(query, [login_id])

		hasher = hashlib.sha256()
		hasher.update(cookie_pass.encode('utf-8'))
		hasher.update(cookie_salt.encode('utf-8'))

		hash_pass = hasher.hexdigest()

		# add the key
		cursor.execute("INSERT INTO User_Login_Keys (LoginId, Username, CookiePass, CookieSalt, DateAccessed) " +
			"VALUES (%s, %s, %s, %s, %s)", [login_id, user, hash_pass, cookie_salt, datetime.utcnow()])

		cookie_key_str = login_id + '|' + cookie_pass

		conn.commit()

		cursor.close()
		conn.close()

	elif addNewId == False:  # we can expect the login key cookie to already exist
		#return make_response("addNewId == False")
		if "user_login_key" in request.cookies:
			cookie_key_str = request.cookies["user_login_key"]
			valid = checkUserLoginKey(cursor, request, user)
			print(valid)
		else:  # stop the login if the cookie does not exist
			cookie_key_str = "[None]"
			valid = False
		if valid == False:
			exp_time = exp_time - timedelta(60)  # make sure cookies are removed since there was an error
			# can't say if the login should be removed or will accidentally delete another login - leave alone and redirect
			resp = redirect(url_for("login"))

	elif addNewId == None:
		#return make_response("addNewId == None")
		if "user_login_key" in request.cookies:
			# delete the key and the cookie holding it
			key = request.cookies["user_login_key"].split('|')[0]
			cursor.execute("DELETE FROM User_Login_Keys WHERE LoginId = %s", [key])
			conn.commit()

		cookie_key_str = "[None]";  # doesn't matter since cookie is doomed

	cursor.close()
	conn.close()
		
	resp.set_cookie('user_logged', value=user, expires=exp_time, httponly=True)
	# above cookie probably does not need to be httponly, but attackers may still try to grab usernames, so
	# better safe than sorry
	resp.set_cookie('user_login_key', value=cookie_key_str, expires=exp_time, httponly=True)

	return resp
	

def checkUserLoginKey(cursor, request, user):
	'''
	cursor is a mysql.connector Cursor object
	request is a flask request

	Method assumes that the cookie exists, but does all other processing
	'''
	data = request.cookies["user_login_key"].split('|')
	if len(data) != 2:  # data is incorrect or corrupted somehow
		return False

	cursor.execute("SELECT CookiePass, CookieSalt, Username FROM User_Login_Keys WHERE LoginId = %s", [data[0]])

	if cursor.rowcount != 1:  # no such key exists
		return False

	row = cursor.fetchone()
	hasher = hashlib.sha256()
	hasher.update(data[1].encode('utf-8'))  # add pass from data
	hasher.update(row[1].encode('utf-8'))  # add salt from MySQL row

	return hasher.hexdigest() == row[0] and user == row[2]  # check against salt from MySQL row and return result


def cleanUserLoginKeyTable():
	'''
	This function cleans the user key table of old logins that were not removed from table
	because the login expired or the cookie's identifying info was modified.
	'''
	conn = mysql.connector.connect(user='DCC_NoPswd', host='localhost', database='Ocean')
	cursor = conn.cursor(buffered=True)

	time = datetime.utcnow() - timedelta(30)
	cursor.execute("DELETE FROM User_Login_Keys WHERE DateAccessed < %s", [time])
	conn.commit()
	cursor.close()
	conn.close()



