#!/usr/bin/python3
"""
    Starts a flask application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """home screen"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Wolcome to hbnb"""
    return "HBNB"
	

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)