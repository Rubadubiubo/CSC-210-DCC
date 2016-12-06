from flask import Blueprint, request, jsonify, current_app, url_for
import mysql.connector
from datetime import datetime
from random import randrange, choice

ocean_handler = Blueprint('ocean_handler', __name__)


def get_valid_ocean(ocean_name, buffered_cursor):
	# checks to make sure ocean exists
	# passes in cursor so can be used easily inline
	buffered_cursor.execute("SELECT ID, DateCreated, Description FROM Oceans WHERE Name = %s", [ocean_name])
	if buffered_cursor.rowcount == 1:
		return buffered_cursor.fetchone()  # return the ocean data
	else:
		return None  # no ocean was found


@ocean_handler.route('/send_message/', methods=['POST'])
def send_message():  # ajax method for sending a message to an ocean
	if request.referrer not in [url_for("user_site.user_oceans", _external=True)]:
		abort(403)
	conn = mysql.connector.connect(user='DCC_NoPswd', host='localhost', database='Ocean')
	cursor = conn.cursor(buffered = True)
	
	ocean = request.form['ocean_name']
	validate = get_valid_ocean(ocean, cursor)

	textReturn = 'failure'
	if validate != None:
		textReturn = 'success'

		# send message
		title = request.form['message_title']
		message = request.form['message_text']
		ocean = request.form['ocean_name']
		user = request.form['user_sent']
		if user == "":
			user = None

		cursor.execute("INSERT INTO Messages (Title, Data, DateSent, Ocean, UnameSent) VALUES (%s, %s, %s, %s, %s)",
			[title, message, datetime.utcnow(), ocean, user])
		conn.commit()

	cursor.close()
	conn.close()
	return current_app.make_response(textReturn)


@ocean_handler.route('/get_ocean_description/', methods=['POST'])
def get_ocean_description():  # ajax method for getting ocean description from the database
	if request.referrer not in [url_for("user_site.user_oceans", _external=True)]:
		abort(403)
	conn = mysql.connector.connect(user='DCC_NoPswd', host='localhost', database='Ocean')
	cursor = conn.cursor(buffered = True)
	ocean = request.form['ocean_name']

	data = get_valid_ocean(ocean, cursor)

	json = {'ocean': '[none]'}
	if data != None:  # otherwise '[none]' will be sent
		json['ocean'] = ocean
		json['description'] = data[2]

	cursor.close()
	conn.close()
	return jsonify(json)  # return the data to the ajax caller

'''  THIS HAS BEEN REPLACED BY THE BELOW FUNCTION
@ocean_handler.route('/get_message_old/', methods=['POST'])
def get_message_old():  # ajax method for getting a message from the requested ocean
	conn = mysql.connector.connect(user='DCC_NoPswd', host='localhost', database='Ocean')
	cursor = conn.cursor(buffered=True)

	ocean = request.form['ocean_name']
	validate = get_valid_ocean(ocean, cursor)

	json = {"status": "failure"}
	if validate != None:
		json["status"] = "success"

		cursor.execute("SELECT MAX(mID), MIN(mID) FROM Messages")
		limits = cursor.fetchone()
		if limits[0] == None:
			json["status"] = "no messages"

		else:
			max_id = int(limits[0])
			min_id = int(limits[1])

			num = randrange(min_id, max_id+1)  # +1 is because max is not inclusive

			json["num"] = num
			direction = choice(["<=", ">="])

			cursor.execute("SELECT Title, Data, UnameSent FROM Messages WHERE mID " + 
				direction + " " + str(num) + " LIMIT 0,1")

			message_data = cursor.fetchone()

			json['title'] = message_data[0]
			json['data'] = message_data[1]
			json['sender'] = message_data[2]

	cursor.close()
	conn.close()

	return jsonify(json)
'''

@ocean_handler.route('/get_message/', methods=['POST'])
def get_message():
	if request.referrer not in [url_for("user_site.user_oceans", _external=True)]:
		abort(403)
	conn = mysql.connector.connect(user='DCC_NoPswd', host='localhost', database='Ocean')
	cursor = conn.cursor(buffered=True)

	ocean = request.form['ocean_name']
	validate = get_valid_ocean(ocean, cursor)

	json = {"status": "failure"}
	if validate != None:
		json["status"] = "success"

		cursor.execute("SELECT COUNT(*) FROM Messages WHERE Ocean = %s", [ocean])
		count = int(cursor.fetchone()[0])
		num = randrange(count)

		cursor.execute("SELECT Title, Data, UnameSent FROM Messages WHERE Ocean = %s LIMIT " + str(num) + ",1", [ocean])

		message_data = cursor.fetchone()

		json['title'] = message_data[0]
		json['data'] = message_data[1]
		if message_data[2] == None:
			json['sender'] = ""  # so is compatible with json format without having to place restrictions on usernames
		else:
			json['sender'] = message_data[2]

	cursor.close()
	conn.close()

	return jsonify(json)


