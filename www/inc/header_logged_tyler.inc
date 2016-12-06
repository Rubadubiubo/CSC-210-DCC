

<header>
	<nav>
			<?php
			if (!empty($_GET['act'])) {
			setcookie("previous_login", " ", time() - 3600);
			header("Refresh:0");
		} else { }
		?>
		<form action="index.php" method="get">
			<input type="hidden" name="act" value="run">
			<input type="submit" value="Logout" class="button" id="logout">
		</form>
</nav>
</header>
<body>
<!-- .wrapper -->
	<div class="wrapper">
		<!-- .sidebar -->
		<aside class="sidebar left">
			<!-- .inner -->
			<div class="inner">
				<!-- header -->
				<header>
					
					<h1>
						<a href="/testtheme.php">Ocean</a>
					</h1>
					
					<p>Welcome to Ocean, a free, anonymous, user-driven messaging and chat experience!</p>
						
								<!--<select name="menu-links" onchange="javascript:parent.location=this.options[this.selectedIndex].value;"> Performs action upon selection-->
								<select id="menu-links">
									<option value="/testtheme.php"></option>
									<option value="/account_details.php">My account</option>
									<option value="">Send a bottle</option>
									<option value="">Recieve a bottle</option>
									<option value="https://lh3.googleusercontent.com/-2rj78ZwMvmA/AAAAAAAAAAI/AAAAAAAAAA8/fvpmcm1iITA/photo.jpg">DEARGODLETMELIVE</option>
									<option value="/learn_more.php">Learn More</option>
								</select>
								<button id="confirm_menu" class="button">Confirm</button>				
				</header>
				<!--/ header -->

				<!-- Insert any sidebar stuff here -->
					
					<input class="textinput" type="text" id="title" placeholder="Title your bottle...">
					<input class="textinput" type="text" id="message" placeholder="Send a bottle!">
					<button id="confirm_send" class="button">Send!</button>
					<span class="checkedinput">
						<label for="anon"><input type="checkbox" id="anon"/><span class="meta">anonymous?</span></label>
					</span>
					<div id="submission_status"></div> <!--JQuery shows when message submitted-->
					
					<!-- <label class="checkinput"><span>anonymous?</span><input type="checkbox" id="anon"></label> -->
			
				<footer>
					<br>
					<small class="meta">
						<p>DCC, 2016. All rights reserved.</p>
					</small>
				</footer>
			</div>
			<!--/ .inner -->
		</aside>
		<!--/ .sidebar -->
		
		<!-- .content -->
		<div class="content">
			<!-- .inner -->
			<div class="inner">
				<!-- .posts -->
				<ol id="post-container" class="posts masonry one-col">
					<!-- .post.text -->
					<li class="post text masonry-item">
						<!-- .post-container -->
						<div class="post-container">
							<!-- .post-body -->
							<div class="post-body">
																														
								<h2 class="title">
									<a>AAAARRRRG</a>
								</h2>

								<blockquote>
									<p>Welcome to Ocean!</p>
									<p>Get in and have a nice swim</p>
								</blockquote>
							</div>

							<div class="post-meta meta">
							</div>
						</div>
					</li>

				</ol>
				
				<div class="clearfix"></div>
				
				<br><br>
						
			</div>
		</div>
	</div>


	<!--<script type='text/javascript' src='http://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js'></script>-->
	<script type='text/javascript' src='http://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js'></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/js-cookie/2.1.3/js.cookie.min.js"></script>
	<script type="text/javascript">
		function generatePost(title, content, date) {
			return "<li class=\"post text masonry-item\">"+
						"<div class=\"post-container\">"+
							"<div class=\"post-body\">"+
								"<h2 class=\"title\">"+
									"<a>"+title+"</a>"+
								"</h2>"+
								"<div class=\"closer\">"+
								"<blockquote>"+
									"<p>"+content+"</p>"+
								"</blockquote>"+
							"</div>"+
							"<div class=\"post-meta meta\">"+
								"Posted on "+date+
							"</div>"+
								"</div>"+
						"</div>"+
					"</li>";
		}

		// function eventHandler(event) {
		// 	alert(event.target.nodeName);
		// 	var target = $(event.target);
		// 	if (target.is("a")) {
		// 		target.children().toggle();
		// 	}
		// }

		// $(document).on('click', ".post-container .title", function(event) {
		// 	$(event.target).find("div").toggle();
		// });

		// $('.post-container .title').click(eventHandler).find(".post-container .title").hide();
				$(function pullReplies(RepId, title){
			var reps = RepId;
			var test = true;
			//while(test){
				$.ajax({
						type: "POST",
						dataType: "json",
						data: {"RepId":reps},
						url: "cgi-bin/recReply.py",
						success: function(dataR, status) {
								test = false;
								var title = dataR["Title"];
								var message = dataR["Data"];
								var user = dataR["UnameSent"];
								var time = dataR["Posttime"];
								var rep = dataR["ReplyId"]
								
								if (title == "") {
									title = "---";
								}
								if (user == "") {
									user = "Anonymous";
								}

								
								var titleText = title+"	|	By: "+user;
								var dateText = time;
								reps = rep;
								if(rep != "NULL"){
									test = true;
								}
								$(generatePost(titleText, message, dateText)).prependTo("#post-container").hide().fadeIn('slow'); //Generate HTML to display recieved data
								
								
							},
							error: function(dataR, status) {
								test = false;
								alert("Unable to complete request.");
							}
			
				});
				
			
			
			
		});
		
		$(function pullMsg(){
			$.ajax({
						type: "GET",
						dataType: "json",
						url: "cgi-bin/recMessage.py",
						success: function(data, status) {
								var title = data["Title"];
								var message = data["Data"];
								var user = data["UnameSent"];
								var time = data["Posttime"];
								var rep = data["ReplyId"]
								
								if (title == "") {
									title = "---";
								}
								if (user == "") {
									user = "Anonymous";
								}

								
								var titleText = title+"	|	By: "+user;
								var dateText = time;
								$(generatePost(titleText, message, dateText)).prependTo("#post-container").hide().fadeIn('slow'); //Generate HTML to display recieved data
								if(rep != "NULL"){
									pullReplies(rep);
								}
								
							},
							error: function(data, status) {
								alert("Unable to complete request.");
							}
			});
		});
		

		
		$(function(){

			// $(document).on('click', ".post-container .title", function(event) {
				
			// 	$(".closer").slideToggle();
			// });

			$("#confirm_menu").click(function() {
				var option = $("#menu-links option:selected").text(); //Retrieve menu option select when "Confirm" clicked
				var option_value = $("#menu-links option:selected").val();
				switch (option) { //Do various actions based on the value of the selection
					case "My account": //Redirect to accounts page
						window.location.href = option_value;
						break;
					case "Send a bottle": //Give focus to the send message bar
						$("#message").focus();
						break;
					case "Recieve a bottle": //Query recMessage.py to query database to get new posts
						pullMsg();
						break;
					case "Learn More": //Redirect to learn more
						window.location.href = option_value;
						break;
				}
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
						error: function(data) {
							console.log(data);
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

		});
	</script>


	<script>

		// $(function() {
		// 	$('#messageSub').submit(function(event) {
		// 		if ($('#message').val() === "") {  // field is empty
		// 			$('#message-error').text("Message field is empty.");
		// 			event.preventDefault();  // stop form from being submitted
		// 		} else {
		// 			$('#message-error').text("");
		// 		}
		// 	});
	</script>



	<!--<h1>Send a message!</h1>
	<form id="messageSub" method="post" action="cgi-bin/subMessage.py">
			<input type="text" name="message" id="message" class="vertical-form-input">
			<input type="submit" value="SEND">
	</form>-->
</body>

