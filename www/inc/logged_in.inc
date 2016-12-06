<body>
	<div id="wrapper">		
		<main>
			<div id="content">
				<div id="bottlebar">
					<h5>Make a bottle...</h5>
					<input id="title" type="text" placeholder="Give it a title (optional)">
					<label for="anon">anonymous?</label><input id="anon" type="checkbox"><br>
					<textarea id="message" rows=3 columns=150 maxlength=1000 placeholder="Write your message..."></textarea><br>
					<button id="confirm_send">Cast it away!</button>
					<span id="submission_status"></span>
				</div>
				<div class="innertube" id="content-container">
					<!-- <p><script>generateText(30)</script></p> -->
				</div>
				<footer>
					<hr><hr>
					<p>DCC, 2016. All rights reserved.</p>
				</footer>
			</div>
		</main>

		<nav id="nav">
			<div class="innertube">
				<h1><b>Ocean</b></h1>
				<hr><hr>
				<h3>My Account</h3>
				<ul>
					<li><a href="#" id="accountdetails">Account Details</a></li>
					<?php
			    		if (!empty($_GET['act'])) {
			    		setcookie("previous_login", " ", time() - 3600);
			    		header("Refresh:0");
			    		} else { }
		    		?>
					<form action="index.php" method="get">
						<input type="hidden" name="act" value="run">
		    			<input type="submit" value="Logout" id="logout">
					</form>
					<!-- <li><a href="#" id="logout_link">Log out</a></li> -->
				</ul>
				<hr>
				<h3>Favorites</h3>
				<ul>
					<li><a href="#" id="favoritebottles">View Favorited Bottles</a></li>
				</ul>
				<hr>
				<h3>Feed</h3>
				<ul>
					<li><a href="#" id="updatefeed">Update feed</a></li>
				</ul>
				<hr>
				<h3>Chat</h3>
				<ul>
					<li><a href="#">See conversations</a></li>
				</ul>
				<hr>
				<!-- <select id="menu-links">
					<option value="/testtheme.php"></option>
					<option value="/account_details.php">My account</option>
					<option value="">Send a bottle</option>
					<option value="">Recieve a bottle</option>
					<option value="https://lh3.googleusercontent.com/-2rj78ZwMvmA/AAAAAAAAAAI/AAAAAAAAAA8/fvpmcm1iITA/photo.jpg">DEARGODLETMELIVE</option>
					<option value="/learn_more.php">Learn More</option>
				</select>
				<button id="confirm_menu" class="button">Confirm</button>
				<button id="favoritebottles" class="button">Get favs</button> -->
			</div>
		</nav>
	</div>




	<script type="text/javascript">
	var pulledAlready = {};

		function generatePost(title, author, content, date, favorited) {
			if (favorited === undefined) { //If no favorite status given, assume false
				favorited = false;
			}
			return "<hr>"+
					"<h3>"+title+"</h3>"+
					"<p><u><a href=\"#\"><span><img src=\"images/glyphicon-time.png\"></span> Post by "+author+", "+date+".</a></u>  "+
					"<img class=\"heart\" src=\"images/glyphicon-heart-"+favorited+".png\"></p>"+
					"<p class=\"bottlecontent\">"+content+"</p>"+
					"<br><hr>"
		}

		function clearContentStream() {
			$("#content-container").replaceWith("<div class=\"innertube\" id=\"content-container\"></div>"); //Clears and replaces content div with nothing
		}

		$(function(){
			// $(generatePost("Hey","Carl","I just met you","9/11",false)).prependTo("#content-container");
			// $("#confirm_menu").click(function() {
			// 	var option = $("#menu-links option:selected").text(); //Retrieve menu option select when "Confirm" clicked
			// 	var option_value = $("#menu-links option:selected").val();
			// 	switch (option) { //Do various actions based on the value of the selection
			// 		case "My account": //Redirect to accounts page
			// 			window.location.href = option_value;
			// 			break;
			// 		case "Send a bottle": //Give focus to the send message bar
			// 			$("#message").focus();
			// 			break;
			// 		case "Recieve a bottle": //Query recMessage.py to query database to get new posts
			// 			$.ajax({
			// 				type: "GET",
			// 				dataType: "json",
			// 				url: "cgi-bin/recMessage.py",
			// 				success: function(data, status) {
			// 						var title = data["Title"];
			// 						var message = data["Data"];
			// 						var user = data["UnameSent"];
			// 						var time = data["Posttime"];
									
			// 						if (title == "") {
			// 							title = "-";
			// 						}
			// 						if (user == "") {
			// 							user = "Anonymous";
			// 						}
									
			// 						$(generatePost(title, user, message, time)).prependTo("#content-container").hide().fadeIn('slow'); //Generate HTML to display recieved data
			// 					},
			// 					error: function(data, status) {
			// 						alert("Unable to complete request.");
			// 					}
			// 			});
			// 			break;
			// 		case "DEARGODLETMELIVE": //O Great Roko, please have mercy
			// 			window.location.href = option_value;
			// 			break;
			// 		case "Learn More": //Redirect to learn more
			// 			window.location.href = option_value;
			// 			break;
			// 	}
			// });

			$("#updatefeed").click(function() {
				$.ajax({
					type: "GET",
					// data: {"pulled":pulledAlready};
					dataType: "json",
					url: "cgi-bin/recMessage.py",
					success: function(data, status) {
						var title = data["Title"];
						var message = data["Data"];
						var user = data["UnameSent"];
						var time = data["Posttime"];
						// var id = data["mID"];
						// if (pulledAlready.indexOf(id) == -1) {pulledAlready.push(id);}
						
						if (title == "") {
							title = "-";
						}
						if (user == "") {
							user = "Anonymous";
						}
						
						$(generatePost(title, user, message, time)).prependTo("#content-container").hide().fadeIn('slow'); //Generate HTML to display recieved data
					},
					error: function(data, status) {
						alert("Unable to complete request.");
					}
				});
			});


			$("#confirm_send").click(function() {
				var message, title = "";
				var anon = $('#anon').is(":checked");
				var timestamp = new Date().toLocaleString();
				message = $('#message').val(); //Extract textfield value when "Send!" clicked
				title = $('#title').val(); //Extract title textfield
				timestamp = timestamp.replace (/,/g, " "); //Replace ',' in datestring with ' '
				//For some reason, method won't send the timestamp only if message or title is blank
				//Temporary backup is to have the server insert the current time if it's not recieved /w POST data
				if (message+title != "") {
					$.ajax({
						type: "POST",
						url: "cgi-bin/subMessage.py",
						contentType: "application/x-www-form-urlencoded",
						data: {"message":message, "title":title, "timestamp":timestamp, "anon":anon},
						success: function(data, status) {
							$("#submission_status").html("Message cast!").css({"color":"#8F8"}).show().fadeOut(4000);
							$("#confirm_send").hide().fadeIn("slow");
						},
						error: function() {
							// alert("Unable to complete request.");
							$("#submission_status").html("Request failed!").css({"color":"#bf5454"}).show().fadeOut(4000);
							$("body").append(data); //REMOVE WHEN DONE TESTING; WILL ADD CGIB ERROR TO HTML BODY
						}
					});
				}
			});

			$("#logout").click(function(event) {
				if (confirm("Logout?")) {
					window.location.reload(true);
				} else {
					event.preventDefault();
				}
			});

			// Below has been adaped for quack from bootystrap since originally in testtheme

			// $("a[href='#favoritebottles']").on('shown.bs.tab', function(e) {
			$("#favoritebottles").click(function(event) {
				var favoriteIDs;
				$.ajax({
					type: "GET",
					url: "cgi-bin/recFavs.py",
					dataType: "json",
					data: {"username":"test4"}, //USERNAME HARDCODED UNTIL FURTHER NOTICE
					success: function(data, status){
						clearContentStream(true, "favoritebottles");
						for (var i=0; i<Object.keys(data).length; i++) {
							var title = data[i.toString()]["Title"];
							var message = data[i.toString()]["Data"];
							var user = data[i.toString()]["UnameSent"];
							var time = data[i.toString()]["Posttime"];

							if (title == "") {
								title = "---";
							}
							if (user == "") {
								user = "Anonymous";
							}

							$(generatePost(title, user, message, time, true)).prependTo("#content-container").hide().fadeIn('slow');
						}
					},
					error: function(data, status){
						alert("Unable to complete request.");
						console.log(status);
					}
				});
			});


			$("body").on("click", "img", function(event) {
		        var currentSource = $(this).attr("src");
		        if (currentSource == "images/glyphicon-heart-false.png") {
		        	$(this).attr("src", "images/glyphicon-heart-true.png");
		        	// $.ajax({
		        	// 	type: "POST",
		        	// 	url: "/cgi-bin/subFav.py",
		        	// 	data: {post id goes here then server adds or removes from favorites DB and all is well},
		        	// 	success: function(){}, error: function(){}});
		        	// 	}
		        } else {
		        	$(this).attr("src", "images/glyphicon-heart-false.png");
		        }
    		});

		});
	</script>

</body>