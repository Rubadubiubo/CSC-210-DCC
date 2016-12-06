<!DOCTYPE html>
<html lang="en-us">

<head>
	<meta charset="utf-8">
	<meta name="author" content="DCC, Inc.">
	<link rel="stylesheet" type="text/css" href="css/dccstyles.css">
	<link rel="shortcut icon" href="images/favicon.png">
	<!-- add jquery -->
	<script src="https://code.jquery.com/jquery-1.10.2.js"></script>
	<title>Create Account</title>
</head>

<body>
	<!--
	<script>  // adds error message if username is taken
			// this script should be replaced with an ajax lookup
		$(function() {
			if (window.location.href.indexOf("status=failed") != -1) {
				// the name-value pair is in the url: add the failure message
				$('#account-creation-error').text("Error: username is already taken.  Please try again.")
			} else {
				$('#account-creation-error').text("");
			}
		});
	</script>
	-->

	<?php
	$cookie_name = "previous_login";
	if(isset($_COOKIE[$cookie_name])) {
		header('Location: /testtheme.php');
	} else {
		include "inc/header_not_logged.inc"; 
	} ?>

	<div class="content">
		<h1>Create Account</h1>
		<p id="account-creation-error" class="error">
		<form method="post" id="account_info" action="cgi-bin/signup.py">
			<label for="username">Username: </label>
			<input type="text" name="username" id="username" class="vertical-form-input">
			<label for="password">Password: </label>
			<input type="password" name="password" id="password" class="vertical-form-input">
			<label for="confirm-password">Confirm Password: </label>
			<input type="password" name="confirm-password" id="confirm-password" class="vertical-form-input">
			<input type="submit" value="Create Account">
		</form>
		<p id="username-error" class="error"></p>
		<p id="password-error" class="error"></p>
	</div>  <!-- content -->
	<!--
	<script>
		$(function() {
			$('#account_info').submit(function(event) {
				var pswd = $('#password').val()
				if ($('#username').val() === "") {
					$('#username-error').text("Username field is empty.");
					event.preventDefault();
				} else {
					$('#username-error').text("");
				}
				if (pswd === "") {
					$('#password-error').text("Password field is empty.");
					event.preventDefault();
				} else {
					$('#password-error').text("");
				}
			});
		});
	</script>
	-->
	<script src="js/signup_extreme_vetting.js"></script>
	<script src="js/nav-handler.js"></script>
	<script src="js/menu-highlighter.js"></script>  <!-- defines the function highlightMenuItemFromId(id_no_hashtag) -->

	<script>

	highlightMenuItemFromId("nav-create-account");

	</script>  <!-- call the previously defined function -->

</body>

</html>



