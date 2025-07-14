from flask import Flask
from src.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route("/")
    def index():
        return "Hello World!"

    return app
