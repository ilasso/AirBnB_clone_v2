#!/usr/bin/python3
"""
    Basic WebApplication
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Basic WebApplication
    """
    return 'Hello HBNB!'


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


@app.route('/states_list', strict_slashes=False)
def getstateslist():
    """
    display sorted states inside tag body in HTML page
    """
    list = storage.all(State).values()
    return render_template('7-states_list.html', states=list)


@app.teardown_appcontext
def close(error):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def getcitesbystatelist():
    """
    display sorted states and cities inside tag body in HTML page
    """
    list = storage.all(State).values()
    return render_template('8-cities_by_states.html', lstates=list)


@app.route('/states', strict_slashes=False)
def states():
    """
    list of states
    """
    list = storage.all(State).values()
    return render_template('9-states.html', lstates=list)


@app.route('/states/<id>', strict_slashes=False)
def statesid(id):
    """
    list of specfic state
    """
    list = storage.all(State).values()
    for i in list:
        if i.id == id:
            return render_template('9-states.html', stateid=i)
    return render_template('9-states.html')


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
    hbnn clone whith data from DB mysql
    includes amenities
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    hbnn clone whith data from DB mysql
    includes places and users data
    """
    amenities = storage.all(Amenity).values()
    states = storage.all(State).values()
    places = storage.all(Place).values()
    users = storage.all(User).values()
    return render_template('100-hbnb.html', amenities=amenities, states=states,
                           places=places, users=users)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
