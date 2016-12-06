from flask import Blueprint, request, redirect, url_for, current_app, render_template, abort

from aux_functions import modify30DayLoginCookie

user_site = Blueprint('user_site', __name__)

@user_site.route('/home/')
def user_home():
	if 'user_logged' not in request.cookies:
		return redirect(url_for('login'))
	return modify30DayLoginCookie(request, render_template('user_home.html', uname=request.cookies['user_logged'],
		page_subname="Home", subnav_menu_item_id='subnav-home'))
	# must return the login cookie here in case page is redirected from and to within page

@user_site.route('/home/oceans/')
@user_site.route('/home/oceans/<default>')  # to allow for the page to be redirected to with a different default subpage
def user_oceans(default = 'default_browse'):
	if 'user_logged' not in request.cookies:
		return redirect(url_for('login'))

	default = default.split('_')
	valid_defaults = ['browse']
	if default[0] != 'default' or default[1] not in valid_defaults:  # default not correctly supplied
		abort(404)

	return modify30DayLoginCookie(request, render_template('user_oceans.html', uname=request.cookies['user_logged'],
		default = default[1], page_subname="Oceans", subnav_menu_item_id='subnav-oceans'))

@user_site.route('/logout/')
def logout():
	# erase any cookies regardless of who is logged in
	redir = redirect(url_for('login'))
	return modify30DayLoginCookie(request, redir, add=False)  # the redirect takes the place of the rendered template here
	# the other cookie is removed automatically

@user_site.route('/home/conversations/chat/<user>')  # the chat api
def chat(user):
	if user == request.cookies['user_logged']:
		# do something because a user cannot chat with themself
		pass
	pass







