from search import get_tile_information, get_input_type, search_for_information, get_all_tile_information
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

@app.route('/')
def index():
    tiles = get_all_tile_information()
    
    return render_template('index.html', tiles=tiles)

@app.route('/search')
def search():
    search_term = request.args.get('search-input')
    input_type = get_input_type(input_string=search_term)
    if input_type == 'email':
        search_result = search_for_information(email=search_term)
    else:
        search_result = search_for_information(phone_number=search_term)
    if search_result:
        tiles = [get_tile_information(input_type=input_type, search_tuple=search_result)]
    else:
        tiles = []
    return render_template('index.html', tiles=tiles, is_search=True, results_found=len(tiles) > 0, query=search_term,
                           input_type=input_type)


if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)