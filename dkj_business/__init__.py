from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('.env/config.py')
    db.init_app(app=app)
    return app


app = create_app()
from dkj_business.models import *
with app.app_context():
    db.create_all()
import dkj_business.routes