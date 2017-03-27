## `0-hello_route.py`

Write a script that starts a Flask web application:
- Your web application must be listening on `0.0.0.0`, port `5000`
- Must have root route `/` that displays "Hello HBNB!"

To run the file:
$ `python3 -m web_flask.0-hello_route`

And to test it:
$ `curl 0.0.0.0:5000 ; echo "" | cat -e`


## `1-hbnb_route.py`

In addition to the script from `0-hello_route.py`, add:
- Route `/hbnb` that displays "HBNB"

To run the file:
$ `python3 -m web_flask.1-hbnb_route`

And to test it:
$ `curl 0.0.0.0:5000/hbnb ; echo "" | cat -e`


## `2-c_route.py`

In addition to the script from `1-hbnb_route.py`, add:
- Route `/c/<text>` that displays "C " followed by value of `text`
- The `text` value should replace any underscores with spaces

To run the file:
$ `python3 -m web_flask.2-c_route`

And to test it:
$ `curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e`
$ `curl 0.0.0.0:5000/c/cool ; echo "" | cat -e`
$ `curl 0.0.0.0:5000/c`

Note: The last tests should return html formatted 404 Not Found.


## `3-python_route.py`

In addition to the script from `2-c_route.py`, add:
- Route `/python/<?text?>` that displays "Python is cool" as a default
- If `text` is given, display "Python " and the text given

To run the file:
$ `python3 -m web_flask.3-python_route`

And to test it:
$ `curl 0.0.0.0:5000/python/is_magic ; echo "" | cat -e`
$ `curl 0.0.0.0:5000/python ; echo "" | cat -e`
$ `curl 0.0.0.0:5000/python/ ; echo "" | cat -e`

Note: The last 2 tests above should return "Python is cool"

