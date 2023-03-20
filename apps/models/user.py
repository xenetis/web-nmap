# -*- encoding: utf-8 -*-

from flask_login import UserMixin

from apps import db, login_manager

from apps.tools.password import hash_pass


class UserModel(db.Model, UserMixin):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.LargeBinary)

    def __init__(self, **args):
        for key, value in args.items():

            if hasattr(value, '__iter__') and not isinstance(value, str):
                value = value[0]

            if key == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, key, value)

    def __repr__(self):
        return str(self.username)


@login_manager.user_loader
def user_loader(id):
    return UserModel.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = UserModel.query.filter_by(username=username).first()
    return user if user else None
