from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_database(app):
    with app.app_context():
        db.create_all()
    print("created database!!!!!!!!")

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '40685579'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///Compliantformone.db'
    db.init_app(app)
    
    create_database(app)
    
    return app



