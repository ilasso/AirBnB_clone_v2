#!/usr/bin/python3
"""
    Basic WebApplication
"""

from flask import Flask
from flask import render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def render(n):
    """
    render number in 5-number_template template
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def renderoddoreven(n):
    """
    render number in 5-number_template template
    """
    if n % 2 == 0:
        oddoreven = 'even'
    else:
        oddoreven = 'odd'

    return render_template('6-number_odd_or_even.html', n=n, word=oddoreven)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
