from flask_app3 import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"