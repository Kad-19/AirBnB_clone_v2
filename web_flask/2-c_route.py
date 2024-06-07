#!/usr/bin/python3
"""
    Starts a flask application
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """home screen"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Wolcome to hbnb"""
    return "HBNB"


@app.route('/c/<text>')
def c_then_params(text):
    """C is fun"""
    text_mod = text.replace('_', ' ')
    return "C {}".format(text_mod)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
