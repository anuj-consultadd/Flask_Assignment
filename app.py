from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from db import db  
from routes.auth_routes import auth_bp, login_manager
from routes.admin_dashboard import admin_bp
from routes.member_dashboard import member_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db) 

    login_manager.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(member_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)  


