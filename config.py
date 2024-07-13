import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or ''
    DEBUG = True

class ProductionConfig:
    SQLALCHEMY_DATABASE_URI ='https://spork-ortf.onrender.com/'
    DEBUG = True