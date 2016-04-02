# -*- coding: utf-8 -*-
# Copyright (C) 2016 Yutaka Kamei

import json
import time
from abc import ABCMeta, abstractmethod
from urllib.request import Request, urlopen
from urllib.error import URLError
from uuid import uuid4
from .utils import auth_header, detect_encoding

MAX_RETRY_COUNT = 5


class Importable(metaclass=ABCMeta):
    def import_to_cybozu(self, sub_domain_name, login_name, password):
        data = self.as_csv()
        boundary = '%s' % (uuid4().hex,)
        headers = auth_header(login_name, password)
        headers['Content-Type'] = 'multipart/form-data; boundary=%s' % (boundary,)
        body = ('--%s\r\n'
                'Content-Disposition: form-data; name="file"; filename="data.csv"\r\n'
                'Content-Type: text/csv\r\n'
                '\r\n'
                '%s\r\n'
                '--%s--\r\n'
                % (boundary, data, boundary))
        request = Request(self._file_endpoint(sub_domain_name),
                          body.encode('utf-8'),
                          headers=headers,
                          method='POST')
        try:
            response = urlopen(request)
        except URLError as e:
            raise  # FIXME
        next_data = response.read()
        headers['Content-Type'] = 'application/json; charset=utf-8'
        request = Request(self._import_endpoint(sub_domain_name),
                          next_data,
                          headers=headers,
                          method='POST')
        try:
            response = urlopen(request)
        except URLError as e:
            raise  # FIXME
        encoding = detect_encoding(response.getheader('Content-Type', 'application/json;charset=utf-8'))
        data = response.read().decode(encoding)
        try:
            job_id = json.loads(data)['id']
        except ValueError as e:
            raise  # FIXME
        except KeyError as e:
            raise  # FIXME
        del headers['Content-Type']
        request = Request(self._result_endpoint(sub_domain_name, job_id),
                          headers=headers,
                          method='GET')
        for i in range(MAX_RETRY_COUNT):
            try:
                response = urlopen(request)
            except URLError as e:
                print(e.read())
                raise  # FIXME
            encoding = detect_encoding(response.getheader('Content-Type', 'application/json;charset=utf-8'))
            data = response.read().decode(encoding)
            try:
                result = json.loads(data)
                done = result['done']
                success = result['success']
                if not done:
                    time.sleep(0.2 * i)
                    continue
                else:
                    if not success:
                        raise Exception('Failed to FILE API: %s' % (result['errorCode'],))
                    break
            except ValueError as e:
                raise  # FIXME
            except KeyError as e:
                raise  # FIXME

    @staticmethod
    def _file_endpoint(sub_domain_name):
        return 'https://{}.cybozu.com/v1/file.json'.format(sub_domain_name)

    @staticmethod
    def _result_endpoint(sub_domain_name, job_id):
        return 'https://{}.cybozu.com/v1/csv/result.json?id={}'.format(sub_domain_name, job_id)

    @abstractmethod
    def as_csv(self):
        pass

    @staticmethod
    @abstractmethod
    def _import_endpoint(sub_domain_name):
        pass

    def __repr__(self):
        return self.as_json()
