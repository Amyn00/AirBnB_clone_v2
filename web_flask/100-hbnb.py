#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def states_list_route():
    """
    Cities of states: display a HTML page: (inside the tag <BODY>)
    Returns:
        html: Template that lists all cities states and amenity sort by name desc
    """
    data = {
        "states": storage.all("State").values(),
	"places": storage.all("Place").values(),
	"amenities": storage.all("Amenity").values()
    }
    return render_template("100-hbnb.html", models=data)


@app.teardown_appcontext
def close_db(exception=None):
    """
    After each request remove the current SQLAlchemy Session:
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
