import os

# Development environment configuration

# Flask base configuration
SECRET_KEY = 'DEV_KEY'


DB_HOST = os.environ.get('DB_HOST') or 'localhost'
DB_PORT = os.environ.get('DB_PORT') or '5432'
DB_USER = os.environ.get('DB_USER') or 'test'
DB_PASS = os.environ.get('DB_PASS') or 'test'
DB_NAME = os.environ.get('DB_NAME') or 'test'

# SQLAlchemy configuration
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/signals/
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
    DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
)
# SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'

# Flask-Mail configuration
MAIL_SERVER = "localhost"
MAIL_PORT = 1025
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_DEFAULT_SENDER = "test-mail@example.com"

# JWT Variables
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'super-secret'
JWT_IDENTITY_CLAIM = 'sub'
JWT_ACCESS_TOKEN_EXPIRES = os.environ.get('JWT_ACCESS_TOKEN_EXPIRES') or 86400  # 24 hours
