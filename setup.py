# -*- coding: utf-8 -*-
import versioneer
from setuptools import setup, find_packages

versioneer.VCS = 'git'
versioneer.versionfile_source = 'python_package_skeleton/_version.py'
versioneer.versionfile_build = 'python_package_skeleton/_version.py'
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = 'pyhton-package-skeleton-'

with open('README.rst') as f:
    readme = f.read()

setup(
    name='python-package-skeleton',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='My template for creating a new Python package.',
    long_description=readme,
    author='Dave Forgac',
    author_email='tylerdave@tylerdave.com',
    url='https://github.com/tylerdave/python-package-skeleton',
    packages=find_packages(),
    include_package_data=False,
    install_requires=[],
    license='Public Domain',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3'
        )

)
