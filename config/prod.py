import os

# Production configuration keys

SECRET_KEY = os.environ['SECRET_KEY']

# SQLAlchemy configuration
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/signals/
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'


# Flask-Mail configuration
MAIL_SERVER = "mailcatcher"
MAIL_PORT = 1025
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_DEFAULT_SENDER = "test-mail@example.com"

# JWT Variables
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']
