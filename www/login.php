<!DOCTYPE html>
<html lang="en-us">

<head>
	<meta charset="utf-8">
	<meta name="author" content="DCC, Inc.">
	<link rel="stylesheet" type="text/css" href="css/dccstyles.css">
	<link rel="shortcut icon" href="images/favicon.png">
	<!-- add jquery -->
	<script src="https://code.jquery.com/jquery-1.10.2.js"></script>
	<title>Login</title>
</head>

<body>

	<?php
	$cookie_name = "previous_login";
	if(isset($_COOKIE[$cookie_name])) {
		header('Location: /testtheme.php');
		//Add a suggestion to redirect in case page doesn't do it automatically
	} else {
		include "inc/header_not_logged.inc"; 
	} ?>

<!-- TODO: Make a unique .inc for no-previous-login and put all the below html in it so none of it can be accessed while the user has a login cookie -->

<!-- 
	<script>  // adds error message if login was not successful
		$(function() {
			if (window.location.href.indexOf("status=failed") != -1) {
				// the name-value pair is in the url: add the failure message
				$('#login-error').text("Error: username or password is incorrect.  Please try again.")
			} else {
				$('#login-error').text("");
			}
		});
	</script> -->

	<div class="content">
		<h1>Login</h1>
		<p id="login-error" class="error"></p>
		<form id="login" method="post" action="cgi-bin/login.py">
			<label for="username">Username: </label>
			<input type="text" name="username" id="username" class="vertical-form-input">

			<label for="password">Password: </label>
			<input type="password" name="password" id="password" class="vertical-form-input">

			<input id="login" type="submit" value="Login">
		</form>
		<!-- error messages to be set if there is an error -->
		<p id="username-error" class="error"></p>
		<p id="password-error" class="error"></p>
	</div>  <!-- content -->


	<script>
		function wrongCredentials() {
			$('#login-error').show();
			return $('#login-error').text("Error: username or password is incorrect. Please try again.");
		}

		$(function() {
			$('#login').submit(function(event) {
				if ($('#username').val() === "") {  // field is empty
					$('#username-error').text("Username field is empty.");
					event.preventDefault();  // stop form from being submitted
				} else {
					$('#username-error').text("");
				}

				if ($('#password').val() === "") {
					$('#password-error').text("Password field is empty.");
					event.preventDefault();
				} else {
					$('#password-error').text("");
				}

				var username = $('#username').val();
				var password = $('#password').val();
				$('#login-error').hide(); //Causes element to flash quickly for user feedback
				event.preventDefault();
				if (!(username === "" || password === "")) {
					$.ajax({
						type: "post",
						url: "/cgi-bin/login.py",
						data: {"username":username, "password":password},
						success: function(data, status) {
							data = data.replace(/(\r\n|\n|\r)/gm,""); //Strip newlines from return data
							if (data == "true") {window.location.reload(true);}
							else if (data == "false") {wrongCredentials();} //See function up top
							else {alert("Database malfunctioned!");} //Otherwise it's spewing back an error stacktrace
						},
						error: function(data, status) {
							alert("Unable completing request!");
						}
					});
				}

			});
		});
	</script>

	<script src="js/nav-handler.js"></script>
	<script src="js/menu-highlighter.js"></script>  <!-- defines the function highlightMenuItemFromId(id_no_hashtag) -->

	<script>

	highlightMenuItemFromId("nav-login");

	</script>  <!-- call the previously defined function -->

</body>

</html>

