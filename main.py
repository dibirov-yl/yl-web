from flask import Flask
from data import db_session
import sqlite3

from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    #app.run()

    user = User()

    # user.surname = 'Scott'
    # user.name = 'Ridley'
    # user.age = 21
    # user.position = 'captain'
    # user.speciality = 'research engineer'
    # user.address = 'module_1'
    # user.email = 'scott_chief@mars.org'
    # user.hashed_password = ''
    #
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()
    #
    # user.surname = 'Dibirov'
    # user.name = 'MshD'
    # user.age = 41
    # user.position = 'marshal'
    # user.speciality = 'great engineer'
    # user.address = 'base_module'
    # user.email = 'dibirov@mars.org'
    # user.hashed_password = ''
    #
    # db_sess.add(user)
    # db_sess.commit()
    #
    # user.surname = 'Radjab'
    # user.name = 'Gadjiev'
    # user.age = 15
    # user.position = 'junior'
    # user.speciality = 'stajer'
    # user.address = 'back_module'
    # user.email = 'gadjiev@mars.org'
    # user.hashed_password = ''
    #
    # db_sess.add(user)
    # db_sess.commit()

    db_sess = db_session.create_session()
    for user in db_sess.query(User).all():
        print(user)

if __name__ == '__main__':
    main()

