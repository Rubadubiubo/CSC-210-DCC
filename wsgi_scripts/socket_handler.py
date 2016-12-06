from flask_socketio import emit, join_room, leave_room


def on_join(data):
	'''
	This function adds the user to a chat room with another user
	'''
	username = data['username']
	room = data['room']
	join_room(room)

def on_leave(data):
	username = data['username']
	room = data['room']
	leave_room(room)

def handle_chat_message(data):
	'''
	Handles a message when sent from a user to another.
	The JSON data is as follows:
	'''
	emit()



'''
A set of test functions that allow a test of the capabilities of the room
'''