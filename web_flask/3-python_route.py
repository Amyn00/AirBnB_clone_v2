#!/usr/bin/python3
"""
listening on 0.0.0.0, port 5000
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """ display Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ display HBNB """
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """ display C text """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/<text>")
def python_text(text="is cool"):
    """ display Python text """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
