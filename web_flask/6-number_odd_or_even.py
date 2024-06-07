#!/usr/bin/python3
"""
    Starts a flask application
"""
from flask import Flask, render_template

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


@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def python_then_params(text):
    """Python is cool"""
    text_mod = text.replace('_', ' ')
    return "Python {}".format(text_mod)


@app.route('/number/<int:n>')
def number(n):
    """is it a number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Number template"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Number is even or odd"""
    even_or_odd = "even" if n % 2 == 0 else "odd"
    values = {
        "number": n,
        "even_or_odd": even_or_odd
    }
    return render_template('6-number_odd_or_even.html', values=values)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
