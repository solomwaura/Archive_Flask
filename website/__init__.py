from  flask import Flask
import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hddkhfireugrgrjvj'
    app.config['SQLALCHEMY_DATABASE_URL'] = f'sqlite:///{DB_NAME}'

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    return app