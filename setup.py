#!/usr/bin/env python
"""Setup script for Py-FOAAS-cli."""

from setuptools import setup, find_packages

try: # for pip >= 10
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
    from pip.download import PipSession


install_requires = parse_requirements('requirements.txt', session=PipSession())
dependencies = [str(package.req) for package in install_requires]

setup(name='py-foaas-cli',
      include_package_data=True,
      version='1.0.0',
      description='A Python client for interacting with Fuck Off As A Service',
      author='Ravi Teja Gannavarapu',
      author_email='grt4004@gmail.com',
      url='https://github.com/IamRaviTejaG/py-foaas-cli',
      py_modules=['pyfucks'],
      python_requires='>=3',
      install_requires=dependencies,
      packages=find_packages(),
      package_dir={'fucks': 'fucks'},
      entry_points={
            'console_scripts': [
                'pyfoaas = pyfucks:opts',
            ]
        },
      )
