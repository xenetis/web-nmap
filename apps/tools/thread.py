# -*- encoding: utf-8 -*-

import json
import os
from threading import Thread
from time import sleep

from nmap import nmap

import apps
from apps.models import *
from apps import Flask, config, db


class ThreadScanner(Thread):
    db = None

    def run(self):
        db_dir = os.path.abspath(os.curdir) + "/_datas/"
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(db_dir, 'db.sqlite3')

        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
        app.app_context().push()

        with app.app_context():
            self.db = apps.db
            self.db.init_app(app)

            while True:
                if not config.Config.SCANNER_LOCK:
                    # Cancel scan processing in case of app restart
                    scan_el = ScanModel.query.filter_by(status='processing').first()
                    if scan_el is not None:
                        scan_el.status = 'pending'
                        db.session.commit()
                    break

                # Check if a scan in progress
                scan_el = ScanModel.query.filter_by(status='processing').first()
                if scan_el is not None:
                    target_el = TargetModel.query.filter_by(id=scan_el.target).first()
                    command_el = CommandModel.query.filter_by(id=scan_el.command).first()
                    print("Scan in progress: " + target_el.host + " command: " +
                          command_el.type.value + " " + command_el.command)
                else:
                    scan_el = ScanModel.query.filter_by(status='pending') .first()
                    if scan_el is not None:
                        # Start a scan
                        target_el = TargetModel.query.filter_by(id=scan_el.target).first()
                        command_el = CommandModel.query.filter_by(id=scan_el.command).first()
                        print("Start scan: " + command_el.type.value + " " + command_el.command + " " + target_el.host)

                        if command_el.type.name == 'nmap':

                            nm = nmap.PortScanner()

                            scan_el.status = 'processing'
                            db.session.commit()

                            result = nm.scan(hosts=target_el.host, arguments=command_el.command)
                            scan_el.result = bytes(json.dumps(result), 'utf-8')
                            scan_el.status = 'completed'
                            db.session.commit()
                            print("Scan: " + command_el.type.value + " " + command_el.command + " " +
                                  target_el.host + " completed")
                    # else:
                    #     print("No scan")

                sleep(2)
