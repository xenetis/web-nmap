# -*- encoding: utf-8 -*-

from apps import db
import datetime


class ScanModel(db.Model):
    __tablename__ = 'Scan'

    id = db.Column(db.Integer, primary_key=True)
    target = db.Column(db.Integer, db.ForeignKey("Target.id"), nullable=False)
    date_create = db.Column(db.DateTime(), default=datetime.datetime.now)
    date_update = db.Column(db.DateTime(), onupdate=datetime.datetime.now)
    status = db.Column(db.Enum('pending', 'processing', 'completed'))
    command = db.Column(db.Integer, db.ForeignKey("Command.id"), nullable=False)
    result = db.Column(db.LargeBinary)

    def __init__(self, **args):
        for key, value in args.items():

            if hasattr(value, '__iter__') and not isinstance(value, str):
                value = value[0]

            setattr(self, key, value)

    def __repr__(self):
        return str(self.target)
