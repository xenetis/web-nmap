# -*- encoding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired, EqualTo, Length


class UpdateAccountForm(FlaskForm):

    username = StringField('Username',
                           id='username',
                           validators=[DataRequired(), Length(min=5)])
    email = StringField('Email',
                        id='email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='password',
                             validators=[])
    passwordConfirm = PasswordField('Password confirm',
                                    id='password_confirm',
                                    validators=[EqualTo("password")])
