# Development environment configuration

# Flask base configuration
SECRET_KEY = 'DEV_KEY'

# SQLAlchemy configuration
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/signals/
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
