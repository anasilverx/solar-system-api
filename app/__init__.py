from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else:
        app.config['SQLALCHEMY_TEST_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    #Importing models
    from app.models.planet import Planet
    #Initialize app
    db.init_app(app)
    migrate.init_app(app, db)
    #Add blueprint
    from.routes import planets_bp
    app.register_blueprint(planets_bp)
    
    return app
