from flask import Flask
""" Import flask framework"""

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Defining the module Hello_hbnb """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
