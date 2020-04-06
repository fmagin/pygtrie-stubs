# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

packages = \
['pygtrie-stubs']

package_data = \
{'': ['*']}



extras_require = \
{':(python_version >= "2.7" and python_version < "2.8") or (python_version >= "3.3" and python_version < "3.5")': ['typing>=3.6,<4.0']}

setup_kwargs = {
    'name': 'pygtrie-stubs',
    'version': '0.0.1',
    'author': 'Florian Magin',
    'packages': '.',
    'package_data': {'.': ['__init__.py','pygtrie.pyi']},
    'extras_require': extras_require,
}


setup(**setup_kwargs)
