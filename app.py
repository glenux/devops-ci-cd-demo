"""Small Flask server demo"""

from flask import Flask

APP = Flask(__name__)

@APP.route('/')
def root_get():
    """Handles the root url with a welcoming message"""
    return "Hello world !"


@APP.route('/hello/<name>')
def hello_get(name):
    """Handles the /hello url with a personalized welcoming message"""
    return "Hello {} !".format(name)

if __name__ == "__main__":
    APP.run()
