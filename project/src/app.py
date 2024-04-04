from flask import Flask
from database import db
from flask_migrate import Migrate
from user.api import user_bp
from entry.api import entry_bp
from competition.api import competition_bp

from flask_jwt_extended import JWTManager
from config import Config

def create_app():
    
    migrate = Migrate()
    app = Flask(__name__)

    app.config.from_object(Config)

    jwt = JWTManager(app)

    # Initialize database
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(entry_bp)
    app.register_blueprint(competition_bp)

    return app


app = create_app()

if __name__ == "__main__":
    # app = create_app()
    app.run(debug=True)