from flask import render_template
from flask import redirect
from flask import url_for
from flask_app3 import app
from author.form import RegisterForm

@app.route('/login')
def login():
    return "Hello User!"
    
@app.route("/register", methods=("GET", "POST"))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
        
    return render_template('author/register.html', form=form)
    
@app.route("/success")
def success():
    return "Author Registered!"