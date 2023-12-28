#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states_list_route():
    """
    States: display a HTML page: (inside the tag <BODY>)
    Returns:
        html: Template that lists all cities by states sort by name desc
    """
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


@app.route('/states/<id>')
def states_by_id(id):
    """
    Get state by id's
    Returns:
        Html: Template that list all cities of state sorted by name
    """
    state = None
    for s in storage.all("State").values():
        if s.id == id:
            state = s
            break
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def close_db(exception=None):
    """
    After each request remove the current SQLAlchemy Session:
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
