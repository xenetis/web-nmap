# -*- encoding: utf-8 -*-
from typing import List

from apps import db


class TargetModel(db.Model):
    __tablename__ = 'Target'

    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(255), unique=True)
    type = db.Column(db.Enum('ip', 'domain'))
    # scans = db.Relationship(List["Scan"])


    def __init__(self, **args):
        for key, value in args.items():

            if hasattr(value, '__iter__') and not isinstance(value, str):
                value = value[0]

            setattr(self, key, value)

    def __repr__(self):
        return str(self.target)
