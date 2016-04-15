# -*- coding: utf-8 -*-
# Copyright (C) 2016 Yutaka Kamei

import os
import time
from unittest import TestCase, skip
from cybozu_user_api import *

AUTH_SET = {
    'sub_domain_name': os.environ['CYBOZU_SUB_DOMAIN_NAME'],
    'login_name': os.environ['CYBOZU_LOGIN_NAME'],
    'password': os.environ['CYBOZU_PASSWORD'],
}

class TestUser(TestCase):
    def setUp(self):
        self.user192 = {
            'id': 39,
            'name': 'user192',
            'code': '*',
            'password': 'password',
        }

    def test_add_mod_delete_search(self):
        obj = User(**self.user192)
        obj.import_to_cybozu(**AUTH_SET)
        time.sleep(3)
        self.assertIn(obj.name, [x.name for x in User.export_csv_from_cybozu(**AUTH_SET)])
        obj.delete_flag = True
        time.sleep(3)
        obj.import_to_cybozu(**AUTH_SET)
        time.sleep(3)
        self.assertNotIn(obj.name, [x.name for x in User.export_csv_from_cybozu(**AUTH_SET)])


class TestGroup(TestCase):
    def setUp(self):
        self.group39 = {
            'id': 39,
            'name': 'group39',
            'code': '*',
            'type': 'static',
            'description': 'TEST',
        }

    def test_add_mod_delete_search(self):
        obj = Group(**self.group39)
        obj.import_to_cybozu(**AUTH_SET)
        time.sleep(3)
        self.assertIn(obj.name, [x.name for x in Group.export_csv_from_cybozu(**AUTH_SET)])
        obj.delete_flag = True
        time.sleep(3)
        obj.import_to_cybozu(**AUTH_SET)
        time.sleep(3)
        self.assertNotIn(obj.name, [x.name for x in Group.export_csv_from_cybozu(**AUTH_SET)])


class TestTitle(TestCase):
    def setUp(self):
        self.title121 = {
            'id': 121,
            'name': 'title121',
            'code': '*',
            'description': 'TEST',
        }

    def test_add_mod_delete_search(self):
        obj = Title(**self.title121)
        obj.import_to_cybozu(**AUTH_SET)
        time.sleep(3)
        self.assertIn(obj.name, [x.name for x in Title.export_csv_from_cybozu(**AUTH_SET)])
        obj.delete_flag = True
        time.sleep(3)
        obj.import_to_cybozu(**AUTH_SET)
        time.sleep(3)
        self.assertNotIn(obj.name, [x.name for x in Title.export_csv_from_cybozu(**AUTH_SET)])


class TestOrganization(TestCase):
    def setUp(self):
        self.organization213 = {
            'id': '213',
            'name': 'organization213',
            'code': '*',
            'localName': '組織213',
            'localNameLocale': 'ja',
            'parentCode': None,
            'description': 'TEST',
        }

    #@skip
    def test_add_mod_delete_search(self):
        obj = Organization(**self.organization213)
        obj.import_to_cybozu(**AUTH_SET)
        time.sleep(3)
        self.assertIn(obj.name, [x.name for x in Organization.export_csv_from_cybozu(**AUTH_SET)])
        obj.delete_flag = True
        time.sleep(3)
        obj.import_to_cybozu(**AUTH_SET)
        time.sleep(3)
        self.assertNotIn(obj.id, [x.id for x in Organization.export_csv_from_cybozu(**AUTH_SET)])
