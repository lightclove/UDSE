# -*- coding: utf-8 -*-

import psycopg2
import json

with open('config.json') as json_config:
    json_con = json.load(json_config)


class ConnectClass(object):
    def get_connect(self):
        return psycopg2.connect("dbname=%s user=%s host=%s password=%s" % (
        json_con['dbname'], json_con['user'], json_con['host'], json_con['password']))

    def get_con(self):
        self.con = self.get_connect()
        return self.con
