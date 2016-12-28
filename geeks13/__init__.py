from flask import Flask

from .config import configure_app
from .models import db

app = Flask(__name__)
configure_app(app)
db.init_app(app)

with app.app_context():
    db.create_all()

from .views import *