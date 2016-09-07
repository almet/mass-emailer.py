#!/usr/bin/env python

from setuptools import setup

requires = ['jinja2', 'tablib', ]

entry_points = {
    'console_scripts': [
        'mass-emailer = mass_emailer:main',
    ]
}

README = open('README.rst').read()

setup(
    name="mass-emailer",
    version="0.0.1",
    url='https://github.com/almet/mass-emailer.py',
    author='Alexis Metaireau',
    author_email='alexis@notmyidea.org',
    description="Send lots of emails using templates and datasets. ",
    long_description=README,
    packages=['mass_emailer', ],
    include_package_data=True,
    install_requires=requires,
    entry_points=entry_points,
)
