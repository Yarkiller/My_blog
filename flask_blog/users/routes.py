from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flask_blog import db, bcrypt
from flask_blog.models import User, Post
from flask_blog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm)

from flask_blog.users.utils import save_picture

users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # После хеширования вернутся, байты - их надо декодировать в строку ↑

        # Здесь создаём пользователя с hashed_password в базе данных:
        user = User(username=form.username.data,    # User - это SQLAlchemy-модель пользователя (в models.py)
                    email=form.email.data, password=hashed_password)
        # Параметры созданного объекта-пользователя
        # посредством ORM-библиотеки SQLAlchemy будут передаваться в базу данных и сохраняться:
        db.session.add(user)    #   сессия Flask-SQLAlchemy
        db.session.commit()     # объект, который представляет собой транзакцию базы данных
        flash('Ваша учетная запись была создана!'
              ' Теперь вы можете войти в систему', 'success')
        return redirect(url_for('main.home'))
    return render_template('register.html', title='Register', form=form)
