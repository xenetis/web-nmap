# -*- encoding: utf-8 -*-

import os


class Config:
    VERSION = os.getenv('VERSION', default='0.0.0')
    SCANNER_LOCK = False

    SECRET_KEY = os.getenv('SECRET_KEY', default='Ch4ng3-m3-1M-n0t-s3cr3t')

    db_engine = os.getenv('DB_ENGINE', default='sqlite')

    # Sqlite database
    if db_engine == 'sqlite':
        dbDir = os.path.abspath(os.curdir) + "/_datas/"
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(dbDir, 'db.sqlite3')

    # Mariadb database
    if db_engine == 'mysql':
        SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
            os.getenv('DB_ENGINE', os.getenv('DB_ENGINE', default='sqlite')),
            os.getenv('DB_USERNAME', os.getenv('DB_USERNAME', default='webnmap')),
            os.getenv('DB_PASS', os.getenv('DB_PASS', default='Ch4ng3-m3-1M-n0t-s3cr3t')),
            os.getenv('DB_HOST', os.getenv('DB_HOST', default='localhost')),
            os.getenv('DB_PORT', os.getenv('DB_PORT', default='3306')),
            os.getenv('DB_NAME', os.getenv('DB_NAME', default='webnmap'))
        )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')


class ProdConfig(Config):
    DEBUG = False

    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600


class DebugConfig(Config):
    DEBUG = True


app_config = {
    'Debug': DebugConfig,
    'Production': ProdConfig,
}
