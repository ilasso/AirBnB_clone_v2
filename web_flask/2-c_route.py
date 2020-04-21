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

if __name__ == "__main__":
    app.run(host='0.0.0.0')
