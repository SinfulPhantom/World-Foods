"""Entrypoint into the world foods web application"""

from flask import Flask


APP = Flask(__name__)


from . import routes
