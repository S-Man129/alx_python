#!/usr/bin/python3

from flask import Flask
""" Importing flask for the program"""

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This route displays "Hello HBNB!" when accessed.

    Returns:
        str: The message "Hello HBNB!"
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
