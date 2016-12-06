<header>
	<div id="ocean-logo-container">
		<object id="ocean-logo" type="image/svg+xml" data="{{ url_for('static', filename='images/richie_logo1.svg') }}">
			<img id="ocean-logo-fallback" src="{{ url_for('static', filename='images/richie_logo1.png') }}" alt="Ocean Logo">
		</object>
	</div> <!-- ocean-logo -->
	<nav>
		<ul>
			<li><a id="nav-login" href="{{ url_for('login', failed = '') }}">Login</a></li><!--
			--><li><a id="nav-signup" href="{{ url_for('signup') }}">Sign Up</a></li><!--
			--><li><a id="nav-learn-more" href="{{ url_for('learn_more') }}">Learn More</a></li>
		</ul>
	</nav>
</header>

