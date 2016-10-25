# coding=utf-8
import os

from setuptools import find_packages
from setuptools import setup

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name = "hawkweed",
    version = "0.1.4",
    description = "Extending Python builtin types",
    long_description = long_description,
    author = "Veit Heller",
    author_email = "veit@veitheller.de",
    license = "MIT License",
    url = "https://github.com/hellerve/hawkweed",
    download_url = 'https://github.com/hellerve/hawkweed/tarball/0.1.4',
    packages = find_packages(),
    include_package_data = True,
)
