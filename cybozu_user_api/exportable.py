# -*- coding: utf-8 -*-
# Copyright (C) 2016 Yutaka Kamei

import csv
from abc import ABCMeta, abstractmethod
from io import StringIO
from urllib.request import Request, urlopen
from urllib.error import URLError
from .utils import auth_header, detect_encoding


class Exportable(metaclass=ABCMeta):
    @classmethod
    def export_csv_from_cybozu(cls, sub_domain_name, login_name, password):
        request = Request(cls._export_csv_endpoint(sub_domain_name),
                          headers=auth_header(login_name, password),
                          method='GET')
        try:
            response = urlopen(request)
        except URLError as e:
            raise  # FIXME
        encoding = detect_encoding(response.getheader('Content-Type', 'application/json;charset=utf-8'))
        data = response.read().decode(encoding)
        buf = StringIO(data)
        for row in csv.reader(buf):
            yield cls(*row)

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def as_json(self):
        pass

    @abstractmethod
    def as_csv(self):
        pass

    @staticmethod
    @abstractmethod
    def _export_csv_endpoint(sub_domain_name):
        pass
