from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_blog.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()    # создаём объект расширения без привязки к app


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

    from flask_blog.users.routes import users
    app.register_blueprint(users)
    # db.init_app(app) требует,
        # чтобы SQLALCHEMY_DATABASE_URI уже был задан в app.config.

    bcrypt.init_app(app)     # Метод init_app(app) связывает объект bcrypt с конкретным приложением Flask,
                            # позволяя использовать его методы (generate_password_hash,
                            # check_password_hash и т.д.) внутри этого приложения

    return app
