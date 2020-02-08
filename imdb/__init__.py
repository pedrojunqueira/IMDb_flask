from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('__name__')

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba243'

from imdb import routes, models