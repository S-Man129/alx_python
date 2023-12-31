#!/usr/bin/python3
"""  a script that starts a Flask web application and display "Hello HBNB!" """
from flask import Flask
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
