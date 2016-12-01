<!DOCTYPE html>

<?php
	$cookie_name = "previous_login";
	if(isset($_COOKIE[$cookie_name])) {
		header('Location: /index.php');
	} else {} 
	?>
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
	<?php include "inc/header_not_logged.inc"; ?>

	<script>  // adds error message if login was not successful
		$(function() {
			if (window.location.href.indexOf("status=failed") != -1) {
				// the name-value pair is in the url: add the failure message
				$('#login-error').text("Error: username or password is incorrect.  Please try again.")
			} else {
				$('#login-error').text("");
			}
		});
	</script>

	<div class="content">
		<h1>Login</h1>
		<p id="login-error" class="error"></p>
		<form id="login" method="post" action="cgi-bin/login.py">
			<label for="username">Username: </label>
			<input type="text" name="username" id="username" class="vertical-form-input">

			<label for="password">Password: </label>
			<input type="password" name="password" id="password" class="vertical-form-input">

			<input type="submit" value="Login">
		</form>
		<!-- error messages to be set if there is an error -->
		<p id="username-error" class="error"></p>
		<p id="password-error" class="error"></p>
	</div>  <!-- content -->


	<script>
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

