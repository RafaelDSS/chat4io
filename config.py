import os

class Config:
    path_database = os.path.abspath("database.db")
    DEBUG = True
    SECRET_KEY = 'kjfghjcghit78utfghj87t789i'
    SQLALCHEMY_DATABASE_URI = r'sqlite:///' + path_database

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
    URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = URI