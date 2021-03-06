import os

from flask import Flask

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from instance.config import app_config


# Sentry integration with flask app
if os.environ.get('SENTRY_DSN'):
    sentry_sdk.init(
        dsn=os.environ.get('SENTRY_DSN'),
        integrations=[FlaskIntegration()]
    )


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

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

    # Init mail
    from extensions import mail
    mail.init_app(app)

    # Init jwt
    from extensions import jwt
    jwt.init_app(app)


def init_blueprint(app):
    # Import base blueprint
    from flaskapp.auth import main
    app.register_blueprint(main)

    # blueprint for auth parts of app
    from flaskapp.auth import auth
    app.register_blueprint(auth)
