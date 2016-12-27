from flask import render_template, request, flash, session, redirect, url_for

from geeks13 import app, db
from geeks13.forms import RegistrationForm
from geeks13.models import Post, User


@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None가
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user is not None and user.check_password(request.form['password']):
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
