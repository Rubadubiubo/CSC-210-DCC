'''
Script forming the page if user successfully authenticated.

There shouldn't be a need to import anything because the scripts using it should.
'''

def generateUserAccountPage(username):
	print '''
			
Content-type: text/html\r\n\r\n
<html lang="en-us">
<head>
	<meta charset="utf-8">
	<meta name="author" content="DCC, Inc.">
	<link rel="stylesheet" href="css/dccstyles.css">
	<link rel="shortcut icon" href="images/favicon.png">
	'''
	print '	<title>' + username + ' - Home</title>'
	print '</head><body>'
	print '<h1>Welcome, ' + username + '!</h1> </body> </html>'
