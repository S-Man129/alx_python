#!/usr/bin/python3
from flask import Flask, escape
""" Importing flask and escape 
    Flask: This module is imported to create and manage the Flask web application
    escape (from Flask): This function is imported from Flask and is used to 
    safely escape and format text for HTML output.
"""

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
def c_with_text(text):
    """
    This route displays "C " followed by the value of the text variable.

    Args:
        text (str): The text to be displayed.

    Returns:
        str: The formatted message.
    """
    # Replace underscores with spaces
    formatted_text = escape(text).replace('_', ' ')
    return f'C {formatted_text}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
