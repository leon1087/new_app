from flask import render_template
from flask import redirect
from flask import url_for
from flask import session
from new_app import app
from author.form import RegisterForm, LoginForm
from author.models import Author


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        pass
    return render_template('author/login.html', form=form, error=error)
    
@app.route("/register", methods=("GET", "POST"))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
        
    return render_template('author/register.html', form=form)
    
@app.route("/success")
def success():
    return "Author Registered!"