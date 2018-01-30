from new_app import app
from flask import render_template, url_for, redirect
from author.models import Author
from blog.models import Blog
from blog.form import SetupForm
from new_app import db

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"
    
@app.route('/admin')
def admin():
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect('setup')
    return render_template('blog/admin.html')
    
@app.route('/setup', method=('GET', 'POST'))
def setup():
    form = SetupForm()
    return render_template('blog/setup.html', form=form)
    
