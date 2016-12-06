<!DOCTYPE html>
<html lang="en">
<head>
	<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;">

    
	<title>Ocean</title>
	
	<link rel="shortcut icon" href="/images/favicon.png">

	<style type="text/css">

/* --------------------------------------------------------------------------
$BODY-ELEMENTS
/--------------------------------------------------------------------------*/
body 
{
	margin:0;
	padding:20px 0;
	background-color:#d0dde6;
	font-family:sans-serif;
	font-size:13px;
	color:#333333;
	text-shadow:#ffffff 0 1px 1px;	
	line-height:auto;
	
	}

nav
{
	position: relative;
	float: right;
	margin-right: 10px;
	margin-bottom: 30px;
}

a
{
	text-decoration:none;
	color:#2c89e7;
}
	a:hover 
	{
		text-decoration:underline;
		color:#0c0c0c;
	}

blockquote 
{
	font-style:none;
	border-left:5px solid #cccccc;
	margin-left:0;
	width:100%;
	background:#f7f7f7;
}

blockquote p 
{
	margin:0;
	padding:10px;
	padding-left:40px;
	font-family:Georgia;
	font-size:15px;
	color:#555555;
}

blockquote + cite 
{
	margin-top:-10px;
	display:block;
	text-align:right;
	font-style:normal;
	font-size:12px;
	color:#888;
}
blockquote + cite:before 
{
	content: '\2014\0020';
}

/* --------------------------------------------------------------------------
	$LAYOUT
/--------------------------------------------------------------------------*/
.wrapper 
{
	width:90%;
	margin:0 auto;
}

.sidebar, 
.content 
{
	float:left;
	/* Float both divs left */
}

.content 
{
	width:75%;
	/* 70% of the wrapper */
}
	.content > .inner 
	{
		padding-bottom:20px;
		margin-left:30px;
		/* Spacing between sidebar and content */
	}

.sidebar 
{
	width:25%;
	/* Take 30% of wrapper width */
	word-wrap:break-word;
	/* Don't want overlap into content */
}		
	.sidebar.right 
	{
		float:right;
		/* If we're positioning the sidebar on the right, float right and... */
	}
	.sidebar.right + .content > .inner
	{
		margin-left:0;
		margin-right:30px;
		/* ...and flip the margins */
	}
	

.sidebar.top, 
.sidebar.top + .content
{
	width:100%;
}
.sidebar.top 
{
	margin-bottom:30px;
}
.sidebar.top + .content > .inner 
{
	margin-left:0;
}


/* --------------------------------------------------------------------------
	$SIDEBAR
/--------------------------------------------------------------------------*/
.sidebar 
{
	text-align:center;
	background:#eeeeee;
	border-radius:10px;
	box-shadow:0 0 10px 2px rgba(60, 60, 60, 0.1);
	/* Drop shadow */
	font-family:sans-serif;
}
	.sidebar .inner 
	{
		padding-top:20px;
		padding-bottom:10px;
		padding-left:10px;
		padding-right:10px;
		border-radius:10px;
	}
	.sidebar header 
	{
		margin-bottom:20px;
		/* Give some bottom spacing from the sidebar header */
	}

	.sidebar .textinput
	{
		position: auto;
		float: left;
		margin-right: 0px;
		margin-left: 25px;
	}

	/*.checkedinput CSS need to properly format checkbox label*/
	.checkedinput label {
		display: block;
		float: left;
		margin-left: 25px;
		padding-right: 10px;
		white-space: nowrap;
	}
	.checkedinput input {
		vertical-align: middle;
	}
	.checkedinput label span {
		vertical-align: middle;
	}

	.sidebar .portrait 
	{
		width:138px;
		/* Set portrait image container width */
		box-shadow:0 0 10px 2px rgba(60, 60, 60, 0.1);
		/* Give thin border and drop-shadow */
		margin-top:0;
		margin-bottom:20px;
				margin-left:auto;
		margin-right:auto;
				/* Align center and give vertical spacing */
	}
		.portrait img 
		{
			border:5px solid #ffffff;
			/* Give thick white border */
			width:128px;
			height:128px;
			/* Set width */
			display:block;
			/* Clear inline whitepace */
		}
	
	.sidebar header h1 
	{
		/* Blog title */
		margin:0 0 10px;
		font-size:30px;
	}
		.sidebar header h1 a
		{
			color:#222222;
			/* Title link colour */
			text-decoration:none;
			/* Remove underline (on hover) */
		}
			
	.sidebar header .menu-links a
	{
		color:#2c89e7!important;
		padding:0 2px;
	}
	
	.sidebar header .menu-links a:after
	{
		content:' / ';
	}
	.sidebar header .menu-links a:last-child:after
	{
		content:'';
	}
	
	.sidebar footer 
	{
		margin-top:15%;
		/* Give some vertical spacing */
	}

/* --------------------------------------------------------------------------
	$POSTS
/--------------------------------------------------------------------------*/

ol.posts 
{
	margin:0;
	padding:0;
	list-style:none;
	/* Remove list stylings from posts */
}

	ol.posts.masonry .post 
	{
		float:left;
	}
		ol.posts.masonry .post .post-container 
		{
			margin:0 20px;
		}
		
		ol.posts.masonry.one-col .post 
		{	
			width:100%;
		}
		
		ol.posts.masonry.two-col .post 
		{	
			width:49%;
		}
		
		ol.posts.masonry.three-col .post 
		{	
			width:33%;
		}
		
		ol.posts.masonry.four-col .post 
		{	
			width:24%;
		}
		
		ol.posts.masonry.five-col .post 
		{	
			width:19%;
		}

.post 
{
	margin-bottom:40px;
	/* Give each post listing some vertical space */
}

.post-body 
{
	padding:20px;
	/* Give some padding to the post content */
		background:#eeeeee;
		/* Background of posts */
		border-radius:10px;
		
	
		box-shadow:0 0 10px 2px rgba(60, 60, 60, 0.1);
	/* Drop shadow */
		
	text-shadow:none;
	color:inherit;
	/* Text styles */
	
	position:relative;
}

.post .title 
{
	margin:-20px;
	margin-bottom:10px;
	/* Title sticks to the top of the post-body */
		border-radius:10px 10px 0 0;
		/* Keep the top and right corners rounded */
	background:#2c89e7;
	/* Title background */
	border-bottom:1px solid #2c89e7;
	/* Give subtle bottom-shadow line */
	color:#ffffff;
	text-shadow:rgba(0, 0, 0, 0.5) 0 1px 1px;
	font-size:20px;
	font-weight:bold;
	/* Text styles */
}
	.post .title > a 
	{
		color:inherit;
		/* inherit colour */
		text-decoration:none;
		/* No underline */
		display:block;
		padding:10px 20px;
		height:100%;
		/* Full width */
	}
	
.post-meta 
{
	margin-top:10px;
	/* Seperate from post-body */
	padding:0 10px;
	/* Give some horizontal spacing from edges */
	text-align:left;
	font-size:12px;
	font-family:Arial;
	/* Text styles */
	
	}	
	.post-meta .tags, 
	.tags li
	{
		margin:0;
		padding:0;
		list-style:none;
		text-align:left;
		display:inline;
		/* Remove list styling and display inline */
	}
		.tags a 
		{
			color:#2c89e7!important;
		}
		.tags li:after 
		{
			content:', ';
		}
		.tags li:last-child:after 
		{
			content:'';
		}
		

/* Media permalinks */

.media-permalink 
{
	position:absolute;
	top:0;
	left:0;
	width:100%;
	height:100%;
	background:transparent url(http://themesltd.com/tumblr-generator/themes/default/img/000-0.7.png);
	color:#fff;
	text-align:center;
	
		border-radius:10px;
		
	
	opacity:0;
	-webkit-transition:opacity 0.5s;
}

	.media-permalink a 
	{
		color:#fff;
	}

	.photo img:hover + .media-permalink, 
	.media-permalink:hover
	{
		opacity:1!important;
	}
	
	.media-permalink span 
	{
		display:block;
		position:absolute;
		top:50%;
		left:0;
		width:100%;
		text-align:center;
		margin-top:-10px;
		height:20px;
	}
	
.media-permalink.style5, 
.media-permalink.style6 
{
	background:none;
}	
.media-permalink.style5 span, 
.media-permalink.style6 span 
{
	display:block;
	position:absolute;
	bottom:0;
	left:0;
	width:96%;
	padding:5px 2%;
	text-align:center;
	margin:0;
	top:auto;
	height:20px;
	background:transparent url(http://themesltd.com/tumblr-generator/themes/default/img/000-0.7.png);
	text-align:right;
	
		border-radius:0 0 10px 10px;
	}

.media-permalink.style6 span 
{
	text-align:left;
}
	
		
@media only screen and (max-width: 400px) 
{
	.post.photo > .post-body > .caption > span 
	{
		padding:10px;
		font-size:12px;
		/* Decrease font-size/padding for Mobile */
	}
}
	
/* --------------------------------------------------------------------------
	$QUOTE POSTS
/--------------------------------------------------------------------------*/
.post.quote blockquote p
{
	padding:20px 0;
	text-align:center;
	/* Center align */
	font-size:26px;
	/* Increase the font size */
}

@media only screen and (max-width: 400px) 
{
	.post.quote blockquote p
	{
		font-size:16px;
		/* Decrease font size for Mobile */
	}
}
/* --------------------------------------------------------------------------
	$LINK POSTS
/--------------------------------------------------------------------------*/
.post.link .post-body 
{
	padding-bottom:0;
}

.post.link.no-desc .title 
{
	margin-bottom:0;
	border-radius:5px;
	/* Remove bottom margin and make all-rounded for links with no desc */
}


/* --------------------------------------------------------------------------
	$MISC
/--------------------------------------------------------------------------*/
.subtle 
{
	color:inherit!important;
	/* Subltle links have no colour change */
}

.meta
{
	color:#9398a0;
	/* Meta text is subtle on the background */
}
	.meta a 
	{
		color:inherit;
	}
		
.pull-right 
{
	float:right;
	/* Helper class to float right */
}

.underlined 
{
	text-decoration:underline;
}

.button 
{
	border:0;
	border-radius:5px;
	padding:5px 10px;
	cursor:pointer;
	background:#2c89e7;
	color:#fff;
	/*** Replace with something much better? */
}





/* --------------------------------------------------------------------------
	$MEDIA-QUERIES
/--------------------------------------------------------------------------*/
@media only screen and (max-width: 600px) 
{
	.wrapper 
	{
		width:auto;
	}
	.sidebar,
	.sidebar.right 
	{
		float:none;
		width:100%;
		padding-top:0px;
	}
	.content 
	{
		width:100%;
		float:none;
	}
	.content > .inner 
	{
		padding-left:10px;
		padding-right:10px;
		margin-left:0!important;
		margin-right:0!important;
	}	

}

.hidden 
{
	display:none!important;
}

.clearfix 
{
	clear:both;
}




/* New Post veil stuff */


.post-veil 
{
	position:absolute;
	display:none;
	top:0;
	left:0;
	width:100%;
	height:100%;
	background:transparent url(http://themesltd.com/tumblr-generator/themes/default/img/000-0.7.png);
		border-radius:10px;
		-webkit-transition:opacity 0.5s;
	opacity:0;
}
	.post-veil.transparent 
	{
		background:none;
	}
	
	.post-veil.visible 
	{
		opacity:1;
	}
	
	.post-veil:hover 
	{
		opacity:1;
	}

/* Media Icons */



.media-icons 
{
	position:absolute;
	margin:0;
	padding:0;
	top:5px;
	left:5px;
	width:102px;
	height:30px;
	list-style:none;
	overflow:hidden;
}
	.photo img:hover + .media-icons, 
	.media-icons:hover
	{
		display:block;
		opacity:1!important;
	}
	
	.video iframe:hover + .media-icons, 
	.media-icons:hover
	{
		display:block;
		opacity:1!important;
	}

		
	.media-icons li 
	{
		float:left;
		background:transparent url(http://themesltd.com/tumblr-generator/themes/default/img/000-0.7.png);
		//background:red;
		padding:3px;
		border-radius:3px;
		margin:0 3px;
		width:22px;
		height:22px;
	}
	
	.media-icons a 
	{
		color:#fff;
		text-align:center;
		display:inline-block;
		width:100%;
		height:100%;
		text-decoration:none;
	}
	.media-icons a.icon 
	{
		background:transparent url(http://static.tumblr.com/tpqedpr/Zbmm9zw4y/master.png) no-repeat;
		text-indent:-500px;
		overflow:hidden;
		-webkit-transition:background-position 0.5s;
	}
	
		.media-icons a.like 
		{
			background-position: -3px -5px;
		}
		.media-icons a.like:hover 
		{
			background-position: -31px -5px;
		}
		
		.media-icons a.reblog 
		{
			background-position: -3px -62px;
		}
		.media-icons a.reblog:hover 
		{
			background-position: -33px -62px;
		}
		
		.media-icons a.notes 
		{
			font-size:12px;
			padding-top:3px;
			margin-left:-1px;
		}
		
		
/* Style 2 */
.media-icons.style2 
{
	top:5px;
	left:auto;
	right:5px;
}

/* Style 3 */
.media-icons.style3 
{
	top:50%;
	left:50%;
	margin:-15px 0 0 -51px;
}

.media-icons.style3 li 
{
	border-radius:50%;
}

	</style>

</head>
<body>


	<?php
	$cookie_name = "previous_login";
	if(isset($_COOKIE[$cookie_name])) {
		include "inc/header_logged_tyler.inc";
	} else {
		
		include "inc/header_not_logged_tyler.inc";
} ?>
	
	
	<script src="http://ajax.googleapis.org/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
	<!--include jquery -->


</body>
</html>