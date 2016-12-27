from werkzeug.security import generate_password_hash, check_password_hash

from geeks13 import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    pw_hash = db.Column(db.String(50))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def __repr__(self):
        return '<User %r>' % (self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(120))

    def __init__(self, title=None, content=None):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Title %r>' % (self.title)