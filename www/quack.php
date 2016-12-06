<!DOCTYPE html>
<!-- Template by quackit.com -->
<!-- http://www.quackit.com/html/templates/download/preview.cfm?template=/html/templates/layout_templates/2_column_left_menu.cfm -->
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<link rel="shortcut icon" href="/images/favicon.png">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
		<title>Ocean</title>
		<style type="text/css">
		
			body{
				margin:0;
				padding:0;
				font-family: Sans-Serif;
				line-height: 1.5em;
			}
			
			main {
				padding-bottom: 10010px;
				margin-bottom: -10000px;
				float: left;
				width: 100%;
			}
			
			#nav {
				float: left;
				width: 230px;
				margin-left: -100%;
				padding-bottom: 10010px;
				margin-bottom: -10000px;
				background: #ddeeff;
				border-top-right-radius: 45px;
				border-style: solid;
				border-width: 1px;
			}
			
			#bottlebar {
				background: #ddeeff;
				border-radius: 15px;
				border-style: solid;
				border-width: 1px;
				margin: 15px;
				margin-top: 3px;
				padding: 15px;
				padding-top: 0;
				padding-left: 5%;
				/*display: inline-block;*/
			}

			#bottlebar input,textarea,button {
				max-width: 85%;
				font-size:12px; 
			    width:20em; 
			    padding:0; 
			    margin:0
			}

			#bottlebar label {
				color: #555;
				font-size: 10px;
			}

			#anon {
				vertical-align: middle;
			}

			#content-container {
				padding:35px;
				padding-top: 0;
				/*background-color: #eeeeee;*/
			}


			#wrapper {
				overflow: hidden;
			}
			
			#content {
				margin-left: 230px; /* Same as 'nav' width */
			}

			#logout_button {
				/*visibility: hidden;*/
			}


			.innertube {
				margin: 15px; /* Padding for content */
				margin-top: 0;
			}
			
			.bottlecontent {
				padding-left: 30px;
			}

			footer p {
				color: #555;
				font-size: 10px;
				margin-left: 50px;
				margin-right: 50px;
				margin-bottom: 0px;
				padding: 0;
			}

			p {
				color: #555;
			}
	
			nav ul {
				list-style-type: none;
				margin: 0;
				padding: 0;
			}
			
			a {
				color: darkblue;
				text-decoration: none;
			}

			a:active {
				color: orange;
				text-decoration: none;
			}

		</style>	
	</head>
	
	<body>
		<?php
    		$cookie_name = "previous_login";
		    if(isset($_COOKIE[$cookie_name])) {
        		include "inc/logged_in.inc";
    		} else {
        		include "inc/header_not_logged_tyler.inc";
			}
		?>
	</body>
</html>