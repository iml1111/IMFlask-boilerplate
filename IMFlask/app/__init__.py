'''
Application Factory Module
'''
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import config
from app import api

from app.api.error_handler import error_handler as error_bp
from app.api.template import template as template_bp

jwt_manager = JWTManager()
cors = CORS()


def create_app(config_name):
    '''Applcation Object 생성 함수'''
    app = Flask(
        import_name=__name__,
        instance_relative_config=True,
        static_url_path="/",
        static_folder="static/",
        template_folder="templates/")
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    jwt_manager.init_app(app)
    cors.init_app(app)
    api.init_app(app)

    app.register_blueprint(error_bp)
    app.register_blueprint(template_bp)

    return app