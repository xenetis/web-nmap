# -*- encoding: utf-8 -*-
import json
from time import sleep
from apps.default import blueprint
from flask import render_template, request, redirect
from flask_login import login_required
from jinja2 import TemplateNotFound

from apps.models import ScanModel, TargetModel, CommandModel
from apps.tools import validate_ip
from apps import db, config

import validators
import threading

from apps.tools.thread import ThreadScanner


@blueprint.route('/index')
@login_required
def index():
    nb_targets = db.session.query(TargetModel.id).count()

    return render_template('default/index.html', activepath='index', nb_targets=nb_targets)


@blueprint.route('/targets', methods=['GET', 'POST'])
@login_required
def targets():
    if request.method == 'POST':
        if request.form['action'] == 'delete':
            id = request.form['id']
            if TargetModel.query.filter_by(id=id).first() is not None:
                target = TargetModel.query.filter_by(id=id).first()
                db.session.delete(target)
                db.session.commit()

        if request.form['action'] == 'add':
            targets_posted = request.form['targetsList']
            for host in targets_posted.splitlines():
                host = host.strip()
                if TargetModel.query.filter_by(host=host).first() is None:

                    # Add IP
                    if validate_ip(host):
                        target = TargetModel(host=host, type='ip')
                        db.session.add(target)
                        db.session.commit()

                    # Add Domain
                    if validators.domain(host):
                        target = TargetModel(host=host, type='domain')
                        db.session.add(target)
                        db.session.commit()

    return render_template('default/targets.html', activepath='targets', targets=TargetModel.query.all())


@blueprint.route('/scans', methods=['GET', 'POST'])
@login_required
def scans():
    return render_template('default/scans.html',
                           activepath='scans',
                           scans=ScanModel.query.all(),
                           targets=TargetModel.query.all(),
                           commands=CommandModel.query.all())


@blueprint.route('/scans/<scan_id>', methods=['GET', 'POST'])
@login_required
def scan_result(scan_id):
    scan = ScanModel.query.filter_by(id=scan_id).first()
    if scan is not None:
        target = TargetModel.query.filter_by(id=scan.target).first()
        command = CommandModel.query.filter_by(id=scan.command).first()
        result = json.loads(scan.result.decode("utf-8"))
        result_json = json.dumps(result, indent=4)
        return render_template('default/scan_result_nmap.html',
                               activepath='scans',
                               scan=scan,
                               target=target,
                               command=command,
                               result=result,
                               result_json=result_json)
    return redirect("/scans", code=200)


@blueprint.route('/commands', methods=['GET', 'POST'])
@login_required
def commands():
    if request.method == 'POST':
        if request.form['action'] == 'delete':
            id = request.form['id']
            if CommandModel.query.filter_by(id=id).first() is not None:
                command = CommandModel.query.filter_by(id=id).first()
                db.session.delete(command)
                db.session.commit()
        if request.form['action'] == 'add':
            if CommandModel.in_type(request.form['type']):
                command = CommandModel(
                    type=request.form['type'],
                    command=request.form['command'],
                    description=request.form['description'],
                )
                db.session.add(command)
                db.session.commit()

    return render_template('default/commands.html',
                           activepath='commands',
                           commands=CommandModel.query.all())


@blueprint.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    print("Scanner lock: " + str(config.Config.SCANNER_LOCK))
    if request.method == 'POST':
        if request.form['action'] == 'start_thread':
            print("Start thread")
            thread_started = False
            for thread in threading.enumerate():
                if "thread_scanner" in thread.name:
                    thread_started = True

            if not thread_started:
                config.Config.SCANNER_LOCK = True
                my_thread = ThreadScanner(name="thread_scanner")
                my_thread.start()

        if request.form['action'] == 'stop_thread':
            print("Stop thread")
            for thread in threading.enumerate():
                if "thread_scanner" in thread.name:
                    config.Config.SCANNER_LOCK = False
                    sleep(3)

    print("=============== THREADS ===============")
    thread_started = False
    for thread in threading.enumerate():
        print(thread.name)
        if "thread_scanner" in thread.name:
            thread_started = True
    print("=============== THREADS ===============")

    return render_template('default/settings.html', activepath='index', thread_started=thread_started)


@blueprint.route('/<template>')
@login_required
def route_template(template):
    try:

        if not template.endswith('.html'):
            template += '.html'

        activepath = get_activepath(request)

        return render_template("default/" + template, activepath=activepath)

    except TemplateNotFound:
        return render_template('_errors/404.html'), 404

    except:
        return render_template('_errors/500.html'), 500


def get_activepath(request):
    try:
        activepath = request.path.split('/')[-1]
        if activepath == '':
            activepath = 'index'
        return activepath

    except:
        return None
