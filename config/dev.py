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
