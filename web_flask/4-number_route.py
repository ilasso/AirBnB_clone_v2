#!/usr/bin/python3
"""
    Basic WebApplication
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Basic WebApplication
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def only_hbnb():
    """
    Basic WebApplication
    """
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def Cis(text):
    """
    Basic WebApplication
    """
    return 'C'+' '+text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
def pythonis(text):
    """
    Basic WebApplication
    """
    return 'Python'+' '+text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
def pythonis2(text):
    """
    Basic WebApplication
    """
    return 'Python'+' '+text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def nisanumber(n):
    """
    Basic WebApplication
    """
    return '{} is a number'.format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
