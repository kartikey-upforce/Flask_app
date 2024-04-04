from flask import Flask, jsonify
from database import db
from flask_migrate import Migrate
from user.api import api_bp
from entry.api import entry_bp
from competition.api import competition_bp

def create_app():
    
    migrate = Migrate()

    app = Flask(__name__)
    
    # Configuration settings
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/test_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)
    migrate.init_app(app, db)
    # Import models to ensure they are registered with SQLAlchemy
    from user.models import User

    # Register blueprints
    
    app.register_blueprint(api_bp)
    app.register_blueprint(entry_bp)
    app.register_blueprint(competition_bp)

    # Define a simple route
    @app.route('/')
    def index():
        return jsonify({'message': 'Welcome to the Flask app!'})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)