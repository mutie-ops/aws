from flask import Flask


application= app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello world'

