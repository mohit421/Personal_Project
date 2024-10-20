from flask import Flask

#create an flask app
app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"