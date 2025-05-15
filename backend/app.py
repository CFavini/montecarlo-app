from flask import Flask
from backend.config import Config
from backend.models import db
from backend.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(auth_bp)
    return app