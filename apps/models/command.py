# -*- encoding: utf-8 -*-
import enum

from apps import db


class CommandType(enum.Enum):
    nmap = 'Nmap'
    nikto = 'Nikto'


class CommandModel(db.Model):
    __tablename__ = 'Command'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(CommandType))
    command = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def __init__(self, **args):
        for key, value in args.items():

            if hasattr(value, '__iter__') and not isinstance(value, str):
                value = value[0]

            setattr(self, key, value)

    def __repr__(self):
        return str(self.target)

    @staticmethod
    def in_type(value):

        # if value in ','.join(map(str, enumType)):
        if value in ','.join(map(str, CommandType)):
            return True

        return False
