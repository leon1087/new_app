from new_app import app
from flask import render_template, url_for, redirect, flash
import bcrypt
from author.models import Author
from blog.models import Blog
from blog.form import SetupForm
from new_app import db
from author.decorators import login_required

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"
    
@app.route('/admin')
@login_required
def admin():
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))
    return render_template('blog/admin.html')
    
@app.route('/setup', methods=("POST", "GET"))
def setup():
    form = SetupForm()
    error = ""
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        author = Author(
            form.fullname.data,
            form.email.data,
            form.username.data,
            hashed_password,
            True
            )
        db.session.add(author)
        db.session.flush()
        if author.id:
            blog = Blog(
                form.name.data,
                author.id
                )
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = "Error creating user."
        if author.id and blog.id:
            db.session.commit()
            flash("Blog Created")
            return redirect(url_for("admin"))
        else:
            db.session.rollback()
            error = "Error creating blog"
    return render_template('blog/setup.html', form=form)
    
