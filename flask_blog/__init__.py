from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_blog.config import Config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    # 1️⃣ Сначала загружаем конфигурацию!
    app.config.from_object(Config)

    # 2️⃣ Потом инициализируем расширения
    db.init_app(app)
    login_manager.init_app(app)

    # 3️⃣ Регистрируем Blueprint'ы
    from flask_blog.main.routes import main
    app.register_blueprint(main)

    # db.init_app(app) требует,
    # чтобы SQLALCHEMY_DATABASE_URI уже был задан в app.config.
    return app
