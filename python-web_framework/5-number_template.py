#!/usr/bin/python
"""  a script that starts a Flask web application and display "Hello HBNB!", 
    display c/<text>, display python/<text> and display 'number/<n>',
    number_template/<n> """

from flask import Flask, escape, render_template

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

@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is_cool'):
    """
    This route displays "Python " followed by the value of the text variable,
    with underscores (_) replaced by spaces. The default value of text is "is_cool".

    Args:
        text (str, optional): The text to display. Defaults to "is_cool".

    Returns:
        str: The formatted message.
    """
    return 'Python {}'.format(escape(text.replace('_', ' ')))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    This route displays "n is a number" only if n is an integer.

    Args:
        n (int): The number to check.

    Returns:
        str: The message "n is a number" or an error message.
    """
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    This route displays an HTML page only if "n" is an integer.

    Args:
        n (int): The number to display.

    Returns:
        str: The HTML page with "Number: n" inside the <H1> tag in the body.
    """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
