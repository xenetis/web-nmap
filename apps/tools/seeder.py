# -*- encoding: utf-8 -*-

from apps.models import *


def seeder(db):
    nb_users = db.session.query(UserModel.id).count()
    if nb_users < 1:
        admin_user = UserModel(username='admin', email='admin@example.com', password='admin')
        db.session.add(admin_user)
        db.session.commit()

    nb_targets = db.session.query(TargetModel.id).count()
    if nb_targets < 1:
        target_scanme = TargetModel(host='scanme.nmap.org', type='domain')
        db.session.add(target_scanme)
        db.session.commit()

    nb_commands = db.session.query(CommandModel.id).count()
    if nb_commands < 3:
        command_list = [
            CommandModel(type='nmap', command='', description='Default Nmap scan'),
            CommandModel(type='nmap', command='-A', description='Nmap scan with version'),
            CommandModel(type='nmap', command='-sV --script vuln', description='Nmap vulnerability scan')
        ]

        for nmap_command in command_list:
            db.session.add(nmap_command)
            db.session.commit()
