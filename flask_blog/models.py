from datetime import datetime
from flask_login import UserMixin
from flask_blog import db, login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.png')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    #В SQLAlchemy атрибуты модели (username, email, password и т.д.) создаются через db.Column(),
    # а не через обычный конструктор Python с параметрами.
    # По умолчанию класс User не имеет явно определённого метода __init__,
    # принимающего эти аргументы, поэтому IDE может считать,
    # что такие параметры при создании объекта недопустимы. Решение ↓ создать __init__
    def __init__(self, username, email, password, image_file='default.png'):
        self.username = username
        self.email = email
        self.password = password
        self.image_file = image_file

    def __repr__(self):
        return f"Пользователь('{self.username}, " \
               f"{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)

    def __repr__(self):
        return f"Запись('{self.title}', '{self.date_posted}')"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
