# -*- coding: utf-8 -*-
from flask import Flask
from flask_admin import Admin

admin = Admin()

from .web import web


def register_blue_print(app: Flask):
    app.register_blueprint(web)


# def register_db(app: Flask):
#     db.init_app(app)
#     with app.app_context():
#         db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure_settings')
    app.debug = app.config['DEBUG']

    register_blue_print(app)

    admin.init_app(app)

    # register_db(app)  # just annotate this line if you don't have database

    return app
