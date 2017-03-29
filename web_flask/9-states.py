#!/usr/bin/python3

from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states')
def states():
    states = storage.all("State")
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def states_given_id(id):
    states = storage.all("State")
    found_state = ""
    for s_id in states:
        if s_id == id:
            found_state = states[s_id]

    return render_template('9-states.html',
                           state=found_state)


@app.teardown_appcontext
def teardown(err):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
