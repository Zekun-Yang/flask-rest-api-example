class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:03010914@localhost/authors"
    SECRET_KEY="DONOT GUESS"

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:03010914@localhost/authors"
    SECRET_KEY="DONOT GUESS"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:03010914@localhost/authors"
    SQLALCHEMY_ECHO = False
    SECRET_KEY="DONOT GUESS"







