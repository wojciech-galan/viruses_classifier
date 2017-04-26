#! /usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="viruses_classifier",
    version='1.0.1',
    description='Predict host of a virus based on its (possibly complete) genomic sequence',
    url='https://github.com/wojciech-galan/viruses_classifier',
    author='Wojciech Gałan',
    license='GNU GPL v3.0',
    install_requires=[
        'sklearn',
        'numpy',
        'scipy'
    ],
    packages=find_packages(),
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    entry_points = {
        'console_scripts':[
            'viruses_classifier = viruses_classifier.__main__:main'
        ]

    },
    include_package_data=True
)
