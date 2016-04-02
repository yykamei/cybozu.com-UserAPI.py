# -*- coding: utf-8 -*-
# Copyright (C) 2016 Yutaka Kamei

import csv
import json
from io import StringIO
from collections import OrderedDict
from .exportable import Exportable
from .importable import Importable


class Title(Exportable, Importable):
    def __init__(self, id, code, name, description=None, delete_flag=None):
        self.id = id
        self.code = code
        self.name = name
        self.description = description
        self.delete_flag = delete_flag

    def __setattr__(self, name, value):
        if name == 'delete_flag':
            if str(value) == 1 or value == True:
                object.__setattr__(self, name, '1')
            else:
                object.__setattr__(self, name, None)
        elif name == 'description':
            if isinstance(value, str) and len(value) > 0:
                object.__setattr__(self, name, value)
            else:
                object.__setattr__(self, name, None)
        else:
            object.__setattr__(self, name, value)

    def as_json(self):
        return json.dumps(OrderedDict([
            ('id', self.id),
            ('code', self.code),
            ('name', self.name),
            ('description', self.description),
            ('delete_flag', self.delete_flag),
        ]), indent=2)

    def as_csv(self):
        buf = StringIO()
        writer = csv.writer(buf)
        writer.writerow([self.id, self.code, self.name, self.description, self.delete_flag])
        return buf.getvalue()

    @staticmethod
    def _export_endpoint(sub_domain_name):
        return 'https://{}.cybozu.com/v1/csv/title.csv'.format(sub_domain_name)

    @staticmethod
    def _import_endpoint(sub_domain_name):
        return 'https://{}.cybozu.com/v1/csv/title.json'.format(sub_domain_name)
