<!DOCTYPE html>
<html lang="en">
<head>
	<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;">
	<title>Ocean</title>
	<link rel="shortcut icon" href="/images/favicon.png">
	<style type="text/css">
		/*Copy relevant CSS over from testtheme.php*/

	</style>
</head>

<body>
	<?php
	$cookie_name = "previous_login";
	if(isset($_COOKIE[$cookie_name])) {
		include "inc/accounts_page_tyler.inc";
	} else {	
		include "inc/header_not_logged_tyler.inc";
	} ?>

	<script src="http://ajax.googleapis.org/ajax/libs/jquery/1.9.0/jquery.min.js"></script>

</body>
</html>