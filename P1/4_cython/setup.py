# -*- coding: utf-8 -*-
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('f1_cy.pyx'))
# python setup.py build_ext --compiler=msvc