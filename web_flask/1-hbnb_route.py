#!/usr/bin/python3
"""Script that starts a Flask web application"""


from flask import Flask

app = Flask(__name__)
app.strict_slashes = False


@app.route("/")
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_world():
    return "HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
