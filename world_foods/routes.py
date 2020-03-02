"""world foods web application routes"""

import requests
from flask import render_template
from . import APP

@APP.route('/')
@APP.route('/index')
def index():
    """default route, returns 3 recipes from the api"""
    user = {'username': 'Spencer'}
    app_id = ''
    app_key = ''

    response = requests.get(f'https://api.edamam.com/search', params={
        'q': 'chicago',
        'app_id': app_id,
        'app_key': app_key,
        'to': 3
    }).json()

    return render_template('index.html', title='Home', user=user, posts=response["hits"])
