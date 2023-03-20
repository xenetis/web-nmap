# -*- encoding: utf-8 -*-

from flask import render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user
)

from apps import db, login_manager
from apps.auth import blueprint
from apps.auth.forms import LoginForm, CreateAccountForm
from apps.models.user import UserModel

from apps.tools.password import verify_pass


@blueprint.route('/')
def route_default():
    return redirect(url_for('auth_blueprint.login'))


# Login & Registration

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:

        # read form data
        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = UserModel.query.filter_by(username=username).first()

        # Check the password
        if user and verify_pass(password, user.password):

            login_user(user)
            return redirect(url_for('auth_blueprint.route_default'))

        # Something (user or pass) is not ok
        return render_template('auth/login.html',
                               msg='Wrong username or password',
                               form=login_form)

    if not current_user.is_authenticated:
        return render_template('auth/login.html',
                               form=login_form)
    return redirect(url_for('home_blueprint.index'))


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:

        username = request.form['username']
        email = request.form['email']

        # Check usename exists
        user = UserModel.query.filter_by(username=username).first()
        if user:
            return render_template('auth/register.html',
                                   msg='Username already exists',
                                   success=False,
                                   form=create_account_form)

        # Check email exists
        user = UserModel.query.filter_by(email=email).first()
        if user:
            return render_template('auth/register.html',
                                   msg='Email already exists',
                                   success=False,
                                   form=create_account_form)

        # else we can create the user
        user = UserModel(**request.form)
        db.session.add(user)
        db.session.commit()
        
        # Delete user from session
        logout_user()        

        return render_template('auth/register.html',
                               msg='Account created successfully.',
                               success=True,
                               form=create_account_form)

    else:
        return render_template('auth/register.html', form=create_account_form)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth_blueprint.login'))


# Errors

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('_errors/403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('_errors/403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('_errors/404.html'), 404


@blueprint.errorhandler(405)
def not_allowed_error(error):
    return render_template('_errors/405.html'), 405


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('_errors/500.html'), 500
