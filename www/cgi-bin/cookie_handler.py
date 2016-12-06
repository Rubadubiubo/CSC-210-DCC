
#This file is for checking and creating cookies.

#There are currently a method for generating and reading cookie headers
#that keep users logged in.

import Cookie
import datetime
import os

cookie_time_string = "%a, %d %b %Y %H:%M:%S GMT"  # string for formatting a cookie
login_cookie_expiration_days = 30  # number of days until login cookie expires from date last sent


def generateLoginCookieHeader(username):
	# return the cookie generated from the username
	# can be printed directly in an HTTP header without any further formatting

	cookie = Cookie.SimpleCookie()
	cookie['previous_login'] = username
	cookie['previous_login']['path'] = '/'
	# make the expiration date
	expDate = datetime.datetime.utcnow() + datetime.timedelta(days=login_cookie_expiration_days)
	cookie['previous_login']['expires'] = expDate.strftime(cookie_time_string)
	cookie['previous_login']['httponly'] = True  # stop client-side scripts from accessing cookie
	print(cookie)


def readLoginCookieHeader():  
	# return the username stored in the cookie or an empty string if there is none

	stored_cookie_string = os.environ.get('HTTP_COOKIE')
	cookie = Cookie.SimpleCookie(stored_cookie_string)
	if 'previous_login' in cookie:  # ckeck if the cookie has been sent
		return cookie['previous_login'].value
	else:
                return ''  # empty username cannot happen, and thus clearly indicates failure

