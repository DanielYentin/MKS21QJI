PREDICTIONS:
* We think that post will return the data back to the user instead of returning it back to flask.

DISCO:
* You invoke the post method by adding "method = 'POST'" into the form tag
Example: <form action="/auth" method = 'POST'>
* When using the POST method, the print(header.args) prints ImmutableMultiDict([]) *it is empty* while print(header.form) prints ImmutableMultiDict([('username', 'testname'), ('sub1', 'Submit Query')]) *contains the arguments*
The URL is http://127.0.0.1:5000/auth after submitting the username in the query.
This is unlike the GET method where after auth you would also see the inputted username along wit sub1 and submit query
Example: http://127.0.0.1:5000/auth?username=testname&sub1=Submit+Query *note the ?username=testname&sub1=Submit+Query after auth
* POST is probably a more secure way of doing forms since the URL wouldn't return your password if you entered it
* GET puts the arguments into URL
* request.method returns the method that was used for the form
* When using POST copying the url:http://127.0.0.1:5000/auth to a new tab doesn't work and returns BadRequestKeyError.
This is probably because request.args['username'] cannot find a value since it is empty due to the fact that POST is being used.

QCC:
* Are there other purposes for POST other than security?
* When is it practical to use GET if POST is more secure?
* Is there automated way to switch between POST and GET methods?
