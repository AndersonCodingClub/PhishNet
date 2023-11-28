from search import search_for_information
from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    return 'Searched'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)