#!/usr/bin/python
"""  a script that starts a Flask web application and display "Hello HBNB!", 
    display c/<text>, display python/<text> """

from flask import Flask, escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This route displays "Hello HBNB!" when accessed.

    Returns:
        str: The message "Hello HBNB!"
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This route displays "HBNB" when accessed.

    Returns:
        str: The message "HBNB"
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    This route displays "C " followed by the value of the text variable,
    with underscores (_) replaced by spaces.

    Args:
        text (str): The text to display.

    Returns:
        str: The formatted message.
    """
    return 'C {}'.format(escape(text.replace('_', ' ')))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    This route displays "Python " followed by the value of the text variable,
    with underscores (_) replaced by spaces. The default value for text is "is cool."

    Args:
        text (str): The text to display.

    Returns:
        str: The formatted message.
    """
    return 'Python {}'.format(escape(text.replace('_', ' ')))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
