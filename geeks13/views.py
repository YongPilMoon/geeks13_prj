from geeks13 import app
from flask import render_template

from geeks13.models import Post


@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)
