from flask import Flask

app = Flask(__name__)

@app.route('/')
def root_get():
    return "Hello world !"


@app.route('/hello/<name>')
def hello_get(name):
    return "Hello {} !".format(name)

if __name__ == "__main__":
    app.run()
