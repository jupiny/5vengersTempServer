import os

from flask import Flask

from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


from ovengers.database import db_session
from ovengers import views
from ovengers.models import User


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
