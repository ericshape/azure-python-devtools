#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os.path
from setuptools import setup


VERSION = "0.1.0+dev"


CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
]


DEPENDENCIES = [
    'azure-common~=1.1.6',
    'azure-mgmt-keyvault~=0.31.0',
    'azure-mgmt-resource~=1.0.0rc1',
    'azure-mgmt-storage~=1.0.0rc1',
    'mock',
    'setuptools-markdown',
    'vcrpy==1.10.3',
]

with open('README.rst', 'r', encoding='utf-8') as f:
    README = f.read()

with open('HISTORY.rst', 'r', encoding='utf-8') as f:
    HISTORY = f.read()

setup(
    name='azure-devtools',
    version=VERSION,
    description='Microsoft Azure Development Tools for SDK',
    long_description_markdown_file='README.md',
    license='MIT',
    author='Microsoft Corporation',
    author_email='azpycli@microsoft.com',
    url='https://github.com/Azure/azure-python-devtools',
    zip_safe=False,
    classifiers=CLASSIFIERS,
    packages=[
        'azure_devtools',
        'azure_devtools.scenario_tests'
    ],
    install_requires=DEPENDENCIES,
)
