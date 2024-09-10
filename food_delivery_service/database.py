from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:max@localhost/food_delivery_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    return app

def get_db_session():
    return scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=db.engine))

def init_db():
    with db.engine.connect() as conn:
        db.create_all()
