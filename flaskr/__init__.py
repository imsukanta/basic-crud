from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from flask_restful import Api

class Base(DeclarativeBase):
    pass
db=SQLAlchemy(model_class=Base)
migrate=Migrate()
def create_app():
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_pyfile('config.py',silent=True)
    app.config['SQLALCHEMY_DATABASE_URI']="postgresql://flask_cp7q_user:AckkG5e7ezIUxfrnH91wIWaxlnWKcqNf@dpg-cv8j7uqn91rc738jeoqg-a/flask_cp7q"
    if not app.config['SQLALCHEMY_DATABASE_URI']:
        raise ValueError("DATABASE_URL environment variable is not set!")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.init_app(app)
    migrate.init_app(app,db)
    api=Api(app)
    #import all models here
    from flaskr.models import user
    #register all views here
    from flaskr.views import home,home_api
    app.register_blueprint(home.bp)
    #add api here
    api.add_resource(home_api.UserRegister,'/api/create')
    return app