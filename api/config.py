import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'axes' + str(os.urandom(11)) + 'secret' + str(os.urandom(15)) + 'key'
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 80
    API_ID = 'PB'
    #GOOGLE_CLIENT_ID = "597475379894-43rmbt2p48s38c0i8lmginn33ki16nop.apps.googleusercontent.com"
    SIGNATURE = "8e5089e8-0141-48b5-a955-1b678dfac08c"
    SWAGGER_ENABLE = '0'
    MYSQL_DB = 'nhl_games_service'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://microservice:AXES-DB-Microservice-Manager@127.0.0.1:3306/' + MYSQL_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    HOST = "0.0.0.0"
    API_ID = os.getenv('API_ID') or Config.API_ID
    SIGNATURE = os.getenv('SIGNATURE') or Config.SIGNATURE
    SWAGGER_ENABLE = os.getenv('SWAGGER_ENABLE') or Config.SWAGGER_ENABLE
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = 30000
    API_ID = os.getenv('API_ID') or Config.API_ID
    SIGNATURE = os.getenv('SIGNATURE') or Config.SIGNATURE
    SWAGGER_ENABLE = os.getenv('SWAGGER_ENABLE') or Config.SWAGGER_ENABLE
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or Config.SQLALCHEMY_DATABASE_URI + '_dev'


class DockerConfig(Config):
    DEBUG = os.getenv('DEBUG') or Config.DEBUG
    HOST = os.getenv('API_HOST') or Config.HOST
    PORT = os.getenv('API_PORT') or Config.PORT
    API_ID = os.getenv('API_ID') or Config.API_ID
    SIGNATURE = os.getenv('SIGNATURE') or Config.SIGNATURE
    SWAGGER_ENABLE = os.getenv('SWAGGER_ENABLE') or Config.SWAGGER_ENABLE
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or Config.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') or Config.SQLALCHEMY_TRACK_MODIFICATIONS


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///' + os.path.join(basedir, Config.MYSQL_DB + '.test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DebugConfig(Config):
    DEBUG = False
    HOST = "0.0.0.0"
    PORT = 33100


config_by_name = dict(
    dev=DevelopmentConfig,
    debug=DebugConfig,
    docker=DockerConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

current_config = config_by_name[os.getenv("NHL_SERVICE_ENV") or 'dev']
