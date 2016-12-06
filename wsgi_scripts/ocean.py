from flask import Flask, render_template, request, make_response, redirect, url_for, abort

from user_auth import user_auth
from user_site import user_site
from ocean_handler import ocean_handler

'''
note that an unexpected import error caused by these lines may be because the directory containing both
files is not on the python load path; an error which should, for the purposes of portability, be considered
an Apache problem.  Rather than adding a hardcoded path in the file, add a WSGIPythonPath to your httpd.conf file:

WSGIPythonPath "path/to/the/containing/directory"
'''

from aux_functions import modify30DayLoginCookie

# generate app
app = Flask(__name__)  # the Flask object is a wsgi callable object (that can be passed to wsgi for production)

app.register_blueprint(user_auth, url_prefix = '/user_auth')  # for user authorization
app.register_blueprint(user_site)  # the site once logged in
app.register_blueprint(ocean_handler, url_prefix = '/ocean_handler')


# Following are views that can be used to generate dynamic webpages.


@app.route('/')  # routes the "root" of the file (i.e. path.../site.py/) to this function
def index():
	from aux_functions import cleanUserLoginKeyTable
	cleanUserLoginKeyTable()
	return modify30DayLoginCookie(request, render_template('index.html', nav_menu_item_id=None))
	# renders a template with the variables put in, then sends to a function that renews the cookie if it exists
	# (i.e. if user is logged in)


@app.route('/login/')  # routes login to this function if no "failed" parameter added
@app.route('/login/<failed>')  # routes the url path.../site.py/login/<failed (a variable)> to this function
def login(failed = ''):  # default parameter is an empty string to put after the slash
	if 'user_logged' in request.cookies:  # user has already logged in
		return redirect(url_for('user_site.user_home'))

	# render the login template if a user is not logged in
	if failed in ['failed', '']:
		return render_template('login.html', failed=failed, nav_menu_item_id="nav-login")
	else:
		abort(404)  # don't accept other variables


@app.route('/signup/')
def signup():
	if 'user_logged' in request.cookies:
		return redirect(url_for(user_site.user_home))

	# render the signup template if a user is not logged in
	return render_template('signup.html', nav_menu_item_id="nav-signup")


@app.route('/learn_more/')
def learn_more():
	return modify30DayLoginCookie(request, render_template('learn_more.html', nav_menu_item_id="nav-learn-more"))

if __name__ == '__main__':
	app.debug = True
	app.run()



