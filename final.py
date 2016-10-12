import os
from flask import Flask, render_template, request
import giphypop
app = Flask(__name__)

g = giphypop.Giphy()

def header_results(results):
    return 'GIFs tagged with "{}"'.format(results)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/results')
def results():
    terms = request.values.get('terms')
    header = header_results(terms)
    results = g.search(terms)
    return render_template('results.html', header=header, results=results, terms=terms)

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)