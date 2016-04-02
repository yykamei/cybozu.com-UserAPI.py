# -*- coding: utf-8 -*-
# Copyright (C) 2016 Yutaka Kamei

import re
from base64 import b64encode


_charset_re = re.compile(r'charset=([\w-]+)', re.I)


def auth_header(login_name, password):
    auth = b64encode(('%s:%s' % (login_name, password)).encode('utf-8')).decode('utf-8')
    return {
        'X-Cybozu-Authorization': auth,
        'Authorization': 'Basic %s' % (auth,),
    }


def detect_encoding(content_type, default='utf-8'):
    assert isinstance(content_type, str)
    _charset_re = re.compile(r'charset=(.*)', re.I)
    matched = _charset_re.search(content_type)
    if matched:
        return matched.group(1)
    else:
        return default
