#!/bin/bash -e

python3 -m venv env

source env/bin/activate
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python
easy_install pip
pip install git+git://github.com/rutsky/hieroglyph.git@py2014
