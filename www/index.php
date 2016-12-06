<!DOCTYPE html>
<!-- colin.corliss@gmail.com -->
<html lang="en-us">

<head>
	<meta charset="utf-8">
	<meta name="author" content="DCC, Inc.">
	<link rel="stylesheet" href="css/dccstyles.css">
	<link rel="shortcut icon" href="images/favicon.png">
	<script src="https://code.jquery.com/jquery-1.10.2.js"></script>
	<title>Ocean - Welcome!</title>
</head>



<body>
	<?php
	$cookie_name = "previous_login";
	if(isset($_COOKIE[$cookie_name])) {
		header('Location: /testtheme.php');
		// include "inc/header_logged.inc";
	} else {
		include "inc/header_not_logged.inc";
} ?>

	

	<script src="js/nav-handler.js"></script>
</body>

</html>
