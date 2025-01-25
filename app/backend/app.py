from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from redis import Redis
from .config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
redis_client = Redis()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)
    
    # Connect Redis
    redis_client.from_url(app.config['REDIS_URL'])
    
    # Register blueprints
    from .routes import auth, profiles, matches
    app.register_blueprint(auth.bp)
    app.register_blueprint(profiles.bp)
    app.register_blueprint(matches.bp)
    
    return app
