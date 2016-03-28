# -*- coding: utf-8 -*-
# Copyright (C) 2016 Yutaka Kamei

from setuptools import find_packages, setup
from cybozu_user_api import __version__

setup(
    name='cybozu_user_api',
    author='Yutaka Kamei',
    author_email='kamei@ykamei.net',
    description='Python implementation for cybozu.com User API',
    license='MIT',
    keywords='API cybozu cybozu.com',
    url='FIXME',
    version=__version__,
    packages=find_packages(),
    test_suite='tests',
)
