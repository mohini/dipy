#!/usr/bin/env python
''' Installation script for dipy package '''

from glob import glob
from distutils.core import setup

setup(name='dipy',
      version='0.1a',
      description='Diffusion utilities in Python',
      author='DIPY python team',
      author_email='matthew.brett@gmail.com',
      url='http://github.com/matthew-brett/dipy',
      packages=['dipy', 'dipy.io', 'dipy.core','dipy.viz'],
      package_data={'dipy.io': ['tests/data/*', 'tests/*.py']},
      scripts=glob('scripts/*.py')
      )

