from flask import Flask, render_template
import sentenceGenerator
# from modules import 'listogram.py'

app = Flask(__name__)
app.markov = sentenceGenerator.file_to_markov()

@app.route('/')
def hello_world():
    result = str(sentenceGenerator.make_quote(app.markov))
    #return result

    return render_template('index.html', result = result)