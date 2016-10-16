import os
from flask import Flask, render_template, request
import giphypop
app = Flask(__name__)

g = giphypop.Giphy()

# Creating our results function and search box

def header_results(results):
    return 'GIFs tagged with "{}"'.format(results)

# creating our index page and rendering to index.html template

@app.route('/')
def index():
    return render_template('index.html')

# creating our about page and rendering to about.html template
@app.route('/about')
def about():
    return render_template('about.html')

# creating our results page and passing through our header, our terms, and the results of your search through to the results page
@app.route('/results')
def results():
    terms = request.values.get('terms')
    header = header_results(terms)
    results = g.search(terms)
    return render_template('results.html', header=header, results=results, terms=terms)

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)