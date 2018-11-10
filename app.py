from flask import Flask
import sentenceGenerator
# from modules import 'listogram.py'

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'