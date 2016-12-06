--><div id="sidebar">
	<a id="subnav-collapse" role="button">[Hide Menu]</a>
	<div id="subnav">
		<ul class="primary">
			<li><a id="subnav-home" href="{{ url_for('user_site.user_home') }}">Home</a></li>
			<li><a id="subnav-oceans" href="{{ url_for('user_site.user_oceans') }}">Oceans</a>
				{% if subnav_menu_item_id == 'subnav-oceans' %}  {# since this implies that the page is the oceans one #}
				{% include 'oceans_submenu.inc' %}
				{% endif %}
			</li>
			<li><a id="subnav-conversations" href="#">Conversations</a></li>
		</ul>
	</div>
</div><!--

