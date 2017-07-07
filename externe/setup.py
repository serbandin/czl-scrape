#!/usr/bin/python3
import re
from setuptools import setup

install_requires = [
    'beautifulsoup4',
    'requests',
    'click',
    'lxml'
]

version_regex = re.compile("VERSION\s*=\s*'(.*?)'$")

with open('__init__.py') as stream:
    VERSION = version_regex.search(stream.read()).group(1)

setup(
    version=VERSION,
    name='mae-scraper',
    url='https://github.com/code4romania/czl-scrape/tree/master/externe',
    author='Rares Urdea, Alexandru Hodorogea',
    author_email='contact@code4.ro',
    description='Scraper pentru site-ul Ministerului de Afaceri Externe',
    install_requires=install_requires,
)
