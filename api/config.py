import os
from decouple import config

BASE_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

class Config():
    SECRET_KEY = config("SECRET_KEY", "secrets")
    SQLALCHEMY_TRACK_MODIFICATION= False
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(BASE_DIRECTORY,"db.sqlite3")




class DevConfig(Config):
    DEBUG= config("DEBUG",default = False, cast=bool)
    SQLALCHEMY_ECHO=True


class TestConfig(Config):
    pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(BASE_DIRECTORY, 'prod_db.sqlite3'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG=config('DEBUG', default = False, cast=bool)



config_dict= {
    "dev":DevConfig,
    "test":TestConfig,
    "prod":ProdConfig
}
