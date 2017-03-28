#!/usr/bin/python3

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<string:s>')
def c(s):
    new_s = s.replace("_", " ")
    return "C {}".format(new_s)


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:s>')
def python(s="is cool"):
    new_s = s.replace("_", " ")
    return "Python {}".format(new_s)


@app.route('/number/<int:n>')
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
