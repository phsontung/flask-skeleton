import os


class Config(object):
    # Flask base configuration
    SECRET_KEY = os.environ.get('SECRET_KEY')

    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')
    DB_NAME = os.environ.get('DB_NAME')

    # SQLAlchemy configuration
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/signals/
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
    )

    # Mail configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')

    # JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_IDENTITY_CLAIM = 'sub'
    JWT_ACCESS_TOKEN_EXPIRES = os.environ.get('JWT_ACCESS_TOKEN_EXPIRES') or 86400  # 24 hours


class DevConfig(Config):
    # Flask configuration
    SECRET_KEY = 'you-are-safe-now'

    # Flask-Mail configuration
    MAIL_SERVER = "localhost"
    MAIL_PORT = 1025
    MAIL_DEFAULT_SENDER = "test-mail@example.com"

    # JWT Variables
    JWT_SECRET_KEY = 'super-secret'


class ProdConfig(Config):
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True


app_config = {
    'dev': DevConfig,
    'prod': ProdConfig,
}
