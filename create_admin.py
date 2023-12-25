from getpass import getpass
import sys

from webapp import create_app
from webapp.model import db, User


app = create_app()

with app.app_context():
    username = input("Введите ваше имя: ")

    if User.query.filter(User.username == username).count():
        print("Пользователь уже существкет")
        sys.exit()
    password1 = getpass("Введите пароль: ")
    password2 = getpass("Повторите пароль: ")
    if not password1 == password2:
        print("пароли не одинаковые")
        sys.exit()

    new_user = User(username=username, role="admin")
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print("User пользователь создан с id = {}".format(new_user.id))
