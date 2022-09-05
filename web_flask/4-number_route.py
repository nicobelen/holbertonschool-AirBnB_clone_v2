#!/usr/bin/python3
"""Script that starts a Flask web application"""


from flask import Flask

app = Flask(__name__)
app.strict_slashes = False


@app.route("/")
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def text(text):
    string = text.replace("_", " ")
    return "C {}".format(string)


@app.route("/python/")
@app.route("/python/<text>")
def python(text="is cool"):
    string = text.replace("_", " ")
    return "Python {}".format(string)


@app.route("/number/<n:int>")
def isnumber(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
