import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE = os.path.join(BASE_DIR, 'geeks13.db')
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from geeks13 import views
from geeks13 import models
