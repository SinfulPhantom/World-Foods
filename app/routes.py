import requests
import json
from flask import render_template
from io import BytesIO
import urllib
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Spencer'}
    app_id = ''
    app_key = ''

    # test = requests.get(f'https://api.edamam.com/search?q=chicken&app_id={app_id}&app_key={app_key}&from=0&to=3&calories=591-722&health=alcohol-free').json()
    response = requests.get(f'https://api.edamam.com/search', params={
        'q': 'chicago',
        'app_id': app_id,
        'app_key': app_key,
        'to': 3
    }).json()

    return render_template('index.html', title='Home', user=user, posts=response["hits"])