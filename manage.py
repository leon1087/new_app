import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from flask_app3 import app

manager = Manager(app)

manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = os.getenv('IP', '0.0.0.0'),
    port = os.getenv('PORT', 5000)
    ))
    
if __name__ == "__main__":
    manager.run()