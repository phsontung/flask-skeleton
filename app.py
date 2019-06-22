import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    config = os.environ.get('FLASK_APP_ENV')
    app.config.from_object('config.{}'.format(config))

    # Init all extensions
    init_extensions(app)

    # Register API Endpoints
    init_blueprint(app)

    return app


def init_extensions(app):
    # Init database
    from extensions import db
    db.init_app(app)

    # Init migration
    from extensions import migrate
    migrate.init_app(app, db)

    # Init bcrypt
    from extensions import bcrypt
    bcrypt.init_app(app)

    # Init Login manager
    from extensions import login_mgr
    login_mgr.login_view = 'auth.login'
    login_mgr.init_app(app)


def init_blueprint(app):
    # Import base blueprint
    from flaskapp.auth import main
    app.register_blueprint(main)

    # blueprint for auth parts of app
    from flaskapp.auth import auth
    app.register_blueprint(auth)
