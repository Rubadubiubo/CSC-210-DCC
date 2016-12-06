/*
This is meant to replace the scripts in the create_account.html file.
It both checks to see if a username is taken as the user types AND prevents the
form from being sent if the username is taken.

The type returned from the script is a plain utf-8 text word, either "collision" or "ok".
*/

$(function() {
	$('#username').on('input', function(event) {
		username_check(event, false);  // do not stop event if uname is taken
	});

	$('#password').on('input', function(event) {
		password_check(event, false, $('#password'));
	});

	$('#confirm-password').on('input', function(event) {
		password_check(event, false, $('#confirm-password'));
	});

	$('#account_info').submit(function(event) {
		// must fix so default is prevented in the event that AT LEAST one is stopped
		valid_pass = password_check(event, true, $('#password'));  // doesn't matter which pswd field gets passed in
		if (valid_pass === true) {  // still a need to check the username (but can't check first because of ajax)
			username_check(event, true);  // stop event if uname is taken
		}
	});
});  // document ready


var username_check = function(event, preventDefault) {
	// check the username status when any key is pressed in the username field
	// allow the function to prevent the default of the event if necessary
	if ($('#username').val() === '') {
		$('#username-error').text('Username field is empty.');
		if (preventDefault === true) {
			event.preventDefault();
		}
	}

	else {
		var $uname_err = $('#username-error');
		$uname_err.text('');  // clear previous username error to check for new one
		$.ajax({  // perform ajax check
			url: '{{ url_for("user_auth.uname_collision_check") }}',  // this is why template is needed
			data: {username: $('#username').val()},
			type: 'POST',
			dataType: 'text',
			success: function (data) {
				// data is to be either "collision" or "ok"
				if (data == 'collision') {  // put "already taken" message in html and optionally halt event
					$uname_err.text('Username is already taken.');
					if (preventDefault === true) {
						event.preventDefault();
					}
				}
			},
			error: function(request) {
				// this should be treated as a script error and should not ever occur in the finished product
				console.log('ERROR: Checking for username conflicts failed.');
				console.log('Request: %s', request.toString());
			}
		});  // ajax
	}
};

var password_check = function(event, preventDefault, $field) {
	// allow for the function to prevent the default action for an event if possible
	// $field should be the jquery obj representing the field to check, either password or confirm-password

	var pswd = $field.val();  // password entered in whichever password field is of interest
	var $pswd_err = $('#password-error');
	var pswd_regex = /^(?:(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[,.\/\\\[\]\-{}|+=_!@#$%^&*()~`<>?'"]).{8,})|(.{18,})$/;
	/* 
	 * (at least one uppercase, lowercase, digit and symbol and 8 or more characters long) OR (at least 18
	 * characters long, to allow for strong passwords like those that RStJ suggested (series of random words
	 * strung together)
	 */

	if (pswd_regex.test(pswd) === false) {
		$pswd_err.text('Password must either be 8 or more characters long and contain an uppercase letter, '+
		 'lowercase letter, digit and special character or be 18 or more characters long.');  // error msg
		if (preventDefault === true) {
			event.preventDefault();  // stop form from being submitted, if necessary
		}
		return false;
	}

	else if ($('#password').val() != $('#confirm-password').val()) {
		$pswd_err.text('Password fields do not match.');
		if (preventDefault === true) {
			event.preventDefault();  // stop form from being submitted, if necessary
		}
		return false;
	}

	else {
		$pswd_err.text('');  // everything is ok
		return true;
	}
};

