from flask import Flask
import dictogram
import listogram
# from modules import 'listogram.py'

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'