#!/usr/bin/python3
'''starts a Flask web application
must be listening on 0.0.0.0, port 5000
/: display “Hello HBNB!”
/hbnb: display “HBNB”'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    '''returns a string Hello HBNB!'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''returns a string "hbnb"'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )'''
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    '''display “Python ”, followed by the value of the text variable'''
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''display “n is a number” only if n is an integer'''
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
