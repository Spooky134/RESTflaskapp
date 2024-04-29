from flask import Flask
from app.routers import api_bp

def app_init():
    app = Flask(__name__)
    app.config.from_object('config.AppConfig')
    app.config.from_object('config.DBConfig')
    app.register_blueprint(api_bp, url_prefix='/flaskapp')
    return app
