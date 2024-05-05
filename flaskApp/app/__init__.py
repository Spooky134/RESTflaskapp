from flask import Flask
from app.routers import api_bp


def app_init():
    app = Flask(__name__)
    app.register_blueprint(api_bp, url_prefix='/flaskapp')
    return app
