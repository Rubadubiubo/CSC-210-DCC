/*
This script ensures the nav element is always at the right until it collapses below the menu
*/

$(function () {
	var navbar = $('nav:first');
	var content = $('#content');
	var sidebar = $('#sidebar');
	var initial_navbar_width = navbar.width();  // initial navbar width
	var oceanLogoWidth = $('#ocean-logo-container').width();  // initial logo width
	var content_min_width = parseInt($('#content').css("min-width"));

	$('#subnav-collapse').click(function (event) {  // to make the submenu dissapear when collapsed
		var $this = $(this);
		if ($this.html() === "[Hide Menu]") {
			$('#subnav').css("display", "none");
			$this.html("[Show Menu]");
		} else {
			$('#subnav').css("display", "block");
			$this.html("[Hide Menu]");
		}
	});

	function expandContent() {  // because will need to be repeated
		$('#subnav-collapse').css("display", "none");
		$('#subnav-collapse').html("[Hide Menu]");  // in case the html indicated that the menu was hidden
		$('#subnav').css("display", "block");  // in case the menu was hidden
		sidebar.css({"display": "inline-block", "min-width": "240px", "text-align": "left",
			"margin-left": "0", "border-left": "none"});
		content.css({"display": "inline-block"});
		$('h1').css("text-align", "left");
	}

	function resizeHandle() {
		var oceanLogoData = $('#ocean-logo').css(['max-width', 'margin-left']);
		var bodyWidth = $('body').width();

		// compute desired margin from width of body and components
		var navbarMargin = bodyWidth - 15 - (initial_navbar_width + oceanLogoWidth);

		if (bodyWidth <= oceanLogoWidth + initial_navbar_width) {
			//navbar.css('display', 'block');  // allow to spill onto next line
			//navbar.width(navbarInitialWidth);  // to make sure navbar width can be accurately computed
			navbar.css({'padding-bottom': '5px', 'margin-left': '0', 'text-align': 'center', 
				'display': 'block', 'margin': '0 auto'});
			$("#ocean-logo-container").css({"display": "block", "margin": "0 auto", "width": "400px"});
		} else {
			navbar.css({'display': 'inline-block', 'margin-left': navbarMargin + "px", 'padding-bottom': '0'});
			$("#ocean-logo-container").css({"display": "inline-block", "margin-left": "5px", "width": "225px"});
		}

		// handle the collapse of the submenu if it exists, etc.
		if (sidebar.length > 0) {
			var clientWidth = document.documentElement.clientWidth;
			
			if (clientWidth < content.width() + sidebar.width() + parseInt(content.css("padding-left")) + 40) {
			// must do some collapsing, since viewport is being shrunk past the width of the content / sidebar
				if (clientWidth >= content_min_width + sidebar.width() + parseInt(content.css("padding-left")) + 40) {
					//console.log("content can be shrunk");
					content.width(clientWidth - sidebar.width() - parseInt(content.css("padding-left")) - 40);
					expandContent();
				} else {
					//console.log("content must be collapsed");
					$('#subnav-collapse').css("display", "block");
					sidebar.css({"display": "block", "width": "240px", 
						"margin-left": (document.documentElement.clientWidth/2 - 120).toString() + "px",
						// half the sidebar width ^^^
						"border-left": "1px solid #000066"});
					content.css({"display": "block", "margin": "0 auto"});
					$('h1').css("text-align", "center");
				}

			} else {
				if (clientWidth >= content_min_width + sidebar.width() + parseInt(content.css("padding-left")) + 40) {
					//console.log("content can be expanded");
					content.width(clientWidth - sidebar.width() - parseInt(content.css("padding-left")) - 40);
				}
				expandContent();
			}
		}  // end sidebar exists
	}  // end resizeHandle

	resizeHandle();  // initial call to make sure nav is where it belongs at page load
	window.addEventListener('resize', resizeHandle);  // recompute values upon resize
});

