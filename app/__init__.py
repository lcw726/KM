from flask import Flask, url_for
from flask_login import current_user
from .extensions import login_manager
from importlib import import_module
from .base.models import User
from os import path
import logging

def register_extensions(app):
    login_manager.init_app(app)


def register_blueprints(app):
    for module_name in ('base', 'home', 'setting'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_logs(app):
    # for combine gunicorn logging and flask built-in logging module
    if __name__ != "__main__":
        gunicorn_logger = logging.getLogger("gunicorn.error")
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)
    # endif


def create_app(config, selenium=False):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config)
    if selenium:
        app.config['LOGIN_DISABLED'] = True
    register_extensions(app)
    register_blueprints(app)
    configure_logs(app)
    return app
