import os


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_PATH') or 'sqlite:///'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    ENV = "PRODUCTION"
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/example'


class DevelopmentConfig(Config):
    ENV = "DEVELOPMENT"
    DEBUG = True


class TestingConfig(Config):
    ENV = "TESTING"
    SQLALCHEMY_DATABASE_URI = None  # patch database instead
    TESTING = True
