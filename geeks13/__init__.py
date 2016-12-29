from flask import Flask, render_template

from geeks13.config import configure_app
from geeks13.member.controllers import member
from geeks13.models import db, Post

app = Flask(__name__)
configure_app(app)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

app.register_blueprint(member, url_prefix='/member')