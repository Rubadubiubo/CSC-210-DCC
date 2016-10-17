/*
This script simply ensures the nav element is always at the right
*/

$(function () {
	var navbar = $('nav:first');
	var navbarInitialWidth = navbar.width();  // find initial width of navbar

	function navFloater() {
		var oceanLogoData = $('#ocean-logo').css(['max-width', 'margin-left']);
		var oceanLogoWidth = parseInt(oceanLogoData['max-width']) + parseInt(oceanLogoData['margin-left']);
		var bodyWidth = $('body').width();

		// compute desired margin from width of body and components
		var navbarMargin = bodyWidth - 15 - (navbar.width() + oceanLogoWidth);

		if (bodyWidth <= oceanLogoWidth + navbar.width() + 15) {
			navbar.css('display', 'block');  // allow to spill onto next line
			navbar.width(navbarInitialWidth);  // to make sure navbar width can be accurately computed
		} else {
			navbar.css('display', 'inline-block');  // pull the navbar back up next to the logo
			navbar.css('margin-left', (navbarMargin + "px"));  // add the margin
		}
	}

	navFloater();  // initial call to make sure nav is where it belongs at page load
	window.addEventListener('resize', navFloater);  // recompute values upon resize
});