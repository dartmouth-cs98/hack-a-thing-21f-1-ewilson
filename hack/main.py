from flask import Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, current_user
from .models import Post
from datetime import datetime
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@main.route('/profile')
@login_required
def profile():
    posts = Post.query.filter_by(author_id=current_user.id)

    return render_template('profile.html', name=current_user.name, posts=posts)


@main.route('/createPost')
def makePost():
    return render_template('post.html')


@main.route('/createPost', methods=['POST'])
def makePost_post():
    title = request.form.get('title')
    content = request.form.get('content')
    
    posted = datetime.now().strftime("%H:%M:%S")
    
    author = current_user.name
    author_id = current_user.id

    new_post = Post(title=title, content=content, posted=posted, author=author, author_id=author_id)
    db.session.add(new_post)
    db.session.commit()


    return redirect(url_for('main.index'))
