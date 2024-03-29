# -*- encoding: utf-8 -*-

import os
from flask_migrate import Migrate
from flask_minify import Minify
from flask_socketio import SocketIO

from sys import exit

from apps.config import app_config
from apps import create_app, db

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = (os.getenv('DEBUG', 'False') == 'True')
config_mode = 'Debug' if DEBUG else 'Production'

try:
    app_config = app_config[config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)

mysocket = SocketIO(app, cors_allowed_origins="*")

Migrate(app, db)

if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)

if DEBUG:
    app.logger.info('DEBUG            = ' + str(DEBUG))
    app.logger.info('FLASK_ENV        = ' + os.getenv('FLASK_ENV'))
    app.logger.info('Page Compression = ' + 'FALSE' if DEBUG else 'TRUE')
    app.logger.info('DBMS             = ' + app_config.SQLALCHEMY_DATABASE_URI)
    app.logger.info('ASSETS_ROOT      = ' + app_config.ASSETS_ROOT)

if __name__ == "__main__":
    mysocket.run(app)
    app.run()


@mysocket.on('scan_event', namespace='/')
def scan_event(message, link=""):
    print('received message (scan_event): ' + message)
    mysocket.emit('scan_event', '{"message": "' + message + '", "link": "' + link + '"}', namespace='/')

