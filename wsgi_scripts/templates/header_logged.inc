<header>
	<div id="ocean-logo-container">
		<object id="ocean-logo" type="image/svg+xml" data="{{ url_for('static', filename='images/richie_logo1.svg') }}">
			<img id="ocean-logo-fallback" src="{{ url_for('static', filename='images/richie_logo1.png') }}" alt="Ocean Logo">
		</object>
	</div> <!-- ocean-logo-container -->
	<nav>
		<ul>
			<li><a id="nav-home" href="{{ url_for('user_site.user_home') }}">{{ uname }}</a></li><!--
			--><li><a id="nav-edit-account" href=".">Edit Account</a></li><!--
			--><li><a id="nav-logout" href="{{ url_for('user_site.logout') }}">Log Out</a></li>
		</ul>
	</nav>
</header>

