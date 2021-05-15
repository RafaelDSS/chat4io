from flask import Flask
from app.blueprints import home
from app.ext import websocket


def create_app(config='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config)

    # Extensions
    websocket.configure(app)

    # Blueprints
    home.configure(app)

    return app