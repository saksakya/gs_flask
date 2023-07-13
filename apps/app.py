from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from apps.config import config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login" #login_viewのルート設定
login_manager.login_message = ""


def create_app(config_key="local"):
    app = Flask(__name__)
    app.config.from_object(config[config_key])

    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)

    from apps.student import views as student_views

    app.register_blueprint(student_views.student, url_prefix="/student")

    from apps.auth import views as auth_views

    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    return app