from flask import Flask

app = Flask('__name__')

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba243'

from imdb import routes