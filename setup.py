# coding=utf-8
import os

from setuptools import find_packages
from setuptools import setup

with open('README.rst') as readme:
    long_description = readme.read()

with open('VERSION') as v:
    version = v.read().strip()

setup(
    name = 'hawkweed',
    version = version,
    description = 'Extending Python builtin types',
    long_description = long_description,
    author = 'Veit Heller',
    author_email = 'veit@veitheller.de',
    license = 'MIT License',
    url = 'https://github.com/hellerve/hawkweed',
    download_url = 'https://github.com/hellerve/hawkweed/tarball/{}'.format(version),
    packages = find_packages(),
    include_package_data = True,
)
