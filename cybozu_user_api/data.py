# -*- coding: utf-8 -*-
# Copyright (C) 2016 Yutaka Kamei

import csv
import json
from io import StringIO
from collections import OrderedDict
from .exportable import Exportable
from .importable import Importable


class User(Exportable, Importable):
    def __init__(self,
                 id,
                 name,
                 code,
                 password,
                 surName=None,
                 givenName=None,
                 surNameReading=None,
                 givenNameReading=None,
                 localName=None,
                 localNameLocale=None,
                 email=None,
                 valid=1,
                 locale=None,
                 timezone=None,
                 phone=None,
                 extensionNumber=None,
                 mobilePhone=None,
                 url=None,
                 employeeNumber=None,
                 joinDate=None,
                 birthDate=None,
                 description=None,
                 sortOrder=None,
                 callto=None,
                 delete_flag=None):
        self.id = id
        self.name = name
        self.code = code
        self.password = password
        self.surName = surName
        self.givenName = givenName
        self.surNameReading = surNameReading
        self.givenNameReading = givenNameReading
        self.localName = localName
        self.localNameLocale = localNameLocale
        self.email = email
        self.valid = valid
        self.locale = locale
        self.timezone = timezone
        self.phone = phone
        self.extensionNumber = extensionNumber
        self.mobilePhone = mobilePhone
        self.url = url
        self.employeeNumber = employeeNumber
        self.joinDate = joinDate
        self.birthDate = birthDate
        self.description = description
        self.sortOrder = sortOrder
        self.callto = callto
        self.delete_flag = delete_flag
        if self.localName is not None and self.localNameLocale is None:
            raise ValueError('If you want to set localName, you MUST set localNameLocale too.')

    def __setattr__(self, name, value):
        if name == 'delete_flag':
            if str(value) == 1 or value is True:
                object.__setattr__(self, name, '1')
            else:
                object.__setattr__(self, name, None)
        else:
            object.__setattr__(self, name, value)

    def as_json(self):
        return json.dumps(OrderedDict([
            ('id', self.id),
            ('name', self.name),
            ('code', self.code),
            ('password', self.password),
            ('surName', self.surName),
            ('givenName', self.givenName),
            ('surNameReading', self.surNameReading),
            ('givenNameReading', self.givenNameReading),
            ('localName', self.localName),
            ('localNameLocale', self.localNameLocale),
            ('email', self.email),
            ('valid', self.valid),
            ('locale', self.locale),
            ('timezone', self.timezone),
            ('phone', self.phone),
            ('extensionNumber', self.extensionNumber),
            ('mobilePhone', self.mobilePhone),
            ('url', self.url),
            ('employeeNumber', self.employeeNumber),
            ('joinDate', self.joinDate),
            ('birthDate', self.birthDate),
            ('description', self.description),
            ('sortOrder', self.sortOrder),
            ('callto', self.callto),
            ('delete_flag', self.delete_flag),
        ]), indent=2)

    def as_csv(self):
        buf = StringIO()
        writer = csv.writer(buf)
        writer.writerow([
            self.id,
            self.name,
            self.code,
            self.password,
            self.surName,
            self.givenName,
            self.surNameReading,
            self.givenNameReading,
            self.localName,
            self.localNameLocale,
            self.email,
            self.valid,
            self.locale,
            self.timezone,
            self.phone,
            self.extensionNumber,
            self.mobilePhone,
            self.url,
            self.employeeNumber,
            self.joinDate,
            self.birthDate,
            self.description,
            self.sortOrder,
            self.callto,
            self.delete_flag,
        ])
        return buf.getvalue()

    @staticmethod
    def _export_csv_endpoint(sub_domain_name):
        return 'https://{}.cybozu.com/v1/csv/user.csv'.format(sub_domain_name)

    @staticmethod
    def _import_endpoint(sub_domain_name):
        return 'https://{}.cybozu.com/v1/csv/user.json'.format(sub_domain_name)


class Group(Exportable, Importable):
    def __init__(self,
                 id,
                 name,
                 code,
                 type,
                 description=None,
                 delete_flag=None):
        self.id = id
        self.name = name
        self.code = code
        self.type = type
        self.description = description
        self.delete_flag = delete_flag

    def __setattr__(self, name, value):
        if name == 'delete_flag':
            if str(value) == 1 or value is True:
                object.__setattr__(self, name, '1')
            else:
                object.__setattr__(self, name, None)
        elif name == 'type':
            if (isinstance(value, str) and
                    (value == 'static' or value == 'dynamic')):
                object.__setattr__(self, name, value)
            else:
                raise AttributeError("type value MUST be 'static' or 'dynamic'")
        else:
            object.__setattr__(self, name, value)

    def as_json(self):
        return json.dumps(OrderedDict([
            ('id', self.id),
            ('name', self.name),
            ('code', self.code),
            ('type', self.type),
            ('description', self.description),
            ('delete_flag', self.delete_flag),
        ]), indent=2)

    def as_csv(self):
        buf = StringIO()
        writer = csv.writer(buf)
        writer.writerow([
            self.id,
            self.name,
            self.code,
            self.type,
            self.description,
            self.delete_flag,
        ])
        return buf.getvalue()

    @staticmethod
    def _export_csv_endpoint(sub_domain_name):
        return 'https://{}.cybozu.com/v1/csv/group.csv'.format(sub_domain_name)

    @staticmethod
    def _import_endpoint(sub_domain_name):
        return 'https://{}.cybozu.com/v1/csv/group.json'.format(sub_domain_name)


class Organization(Exportable, Importable):
    '''Organization

    Organization overrides import_to_cybozu() method.
    '''
    def __init__(self,
                 id,
                 name,
                 code,
                 localName=None,
                 localNameLocale=None,
                 parentCode=None,
                 description=None,
                 delete_flag=None):
        self.id = id
        self.name = name
        self.code = code
        self.localName = localName
        self.localNameLocale = localNameLocale
        self.parentCode = parentCode
        self.description = description
        self.delete_flag = delete_flag
        if self.localName is not None and self.localNameLocale is None:
            raise ValueError('If you want to set localName, you MUST set localNameLocale too.')

    def __setattr__(self, name, value):
        if name == 'delete_flag':
            if str(value) == 1 or value is True:
                object.__setattr__(self, name, '1')
            else:
                object.__setattr__(self, name, None)
        else:
            object.__setattr__(self, name, value)

    def as_json(self):
        return json.dumps(OrderedDict([
            ('id', self.id),
            ('name', self.name),
            ('code', self.code),
            ('localName', self.localName),
            ('localNameLocale', self.localNameLocale),
            ('parentCode', self.parentCode),
            ('description', self.description),
            ('delete_flag', self.delete_flag),
        ]), indent=2)

    def as_csv(self):
        buf = StringIO()
        writer = csv.writer(buf)
        writer.writerow([
            self.id,
            self.name,
            self.code,
            self.localName,
            self.localNameLocale,
            self.parentCode,
            self.description,
        ])
        return buf.getvalue()

    @staticmethod
    def _export_csv_endpoint(sub_domain_name):
        return 'https://{}.cybozu.com/v1/csv/organization.csv'.format(sub_domain_name)

    @staticmethod
    def _import_endpoint(sub_domain_name):
        return 'https://{}.cybozu.com/v1/csv/organization.json'.format(sub_domain_name)

    def import_to_cybozu(self, sub_domain_name, login_name, password):
        objs = [x if x.id != self.id else self
                for x in self.export_csv_from_cybozu(sub_domain_name, login_name, password)]
        if self not in objs:
            objs.append(self)
        data = ''.join([x.as_csv() for x in objs if x.delete_flag != '1'])
        next_data = self._call_file_endpoint(sub_domain_name,
                                             login_name,
                                             password,
                                             data)
        job_id = self._call_import_endpoint(sub_domain_name,
                                            login_name,
                                            password,
                                            next_data)
        self._call_result_endpoint(sub_domain_name,
                                   login_name,
                                   password,
                                   job_id)


class Title(Exportable, Importable):
    def __init__(self, id, name, code, description=None, delete_flag=None):
        self.id = id
        self.name = name
        self.code = code
        self.description = description
        self.delete_flag = delete_flag

    def __setattr__(self, name, value):
        if name == 'delete_flag':
            if str(value) == 1 or value is True:
                object.__setattr__(self, name, '1')
            else:
                object.__setattr__(self, name, None)
        else:
            object.__setattr__(self, name, value)

    def as_json(self):
        return json.dumps(OrderedDict([
            ('id', self.id),
            ('name', self.name),
            ('code', self.code),
            ('description', self.description),
            ('delete_flag', self.delete_flag),
        ]), indent=2)

    def as_csv(self):
        buf = StringIO()
        writer = csv.writer(buf)
        writer.writerow([self.id, self.name, self.code, self.description, self.delete_flag])
        return buf.getvalue()

    @staticmethod
    def _export_csv_endpoint(sub_domain_name):
        return 'https://{}.cybozu.com/v1/csv/title.csv'.format(sub_domain_name)

    @staticmethod
    def _import_endpoint(sub_domain_name):
        return 'https://{}.cybozu.com/v1/csv/title.json'.format(sub_domain_name)
