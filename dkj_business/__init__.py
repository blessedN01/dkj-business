from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('.env/config.py')
    db.init_app(app=app)
    migrate.init_app(app, db)
    return app


app = create_app()

from dkj_business.models import *
import dkj_business.routes