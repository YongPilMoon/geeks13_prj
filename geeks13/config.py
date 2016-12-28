import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SECRET_KEY = '1d94e52c-1c89-4515-b87a-f48cf3cb7f0b'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATABASE = os.path.join(BASE_DIR, 'geeks13.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE
    SECRET_KEY = 'a9eec0e0-23b7-4788-9a92-318347b9a39f'


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SECRET_KEY = '792842bc-c4df-4de1-9177-d5207bd9faa6'

config = {
    "development": "geeks13.config.DevelopmentConfig",
    "testing": "geeks13.config.TestingConfig",
    "default": "geeks13.config.DevelopmentConfig"
}


def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])