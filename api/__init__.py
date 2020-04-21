from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from api.config import current_config

db = SQLAlchemy()
bcrypt = Bcrypt()
cors = CORS()


def create_app():
    app = Flask(__name__)
    app.config.from_object(current_config)
    db.init_app(app)
    cors.init_app(app)
    return app
