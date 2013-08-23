#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Laurent El Shafey <Laurent.El-Shafey@idiap.ch>
# Fri Aug 23 12:32:01 CEST 2013
#
# Copyright (C) 2011-2013 Idiap Research Institute, Martigny, Switzerland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(

    name='xbob.db.voxforge',
    version='0.0.1a0',
    description='Speaker verification protocol on a subset of the VoxForge database',
    url='http://pypi.python.org/pypi/xbob.db.voxforge',
    license='GPLv3',
    author='Elie Khoury',
    author_email='Elie.Khoury@idiap.ch',
    long_description=open('README.rst').read(),

    packages=find_packages(),
    include_package_data=True,
    zip_safe = False,

    install_requires=[
      'setuptools',
      'bob',
      'xbob.db.verification.filelist',
    ],

    namespace_packages = [
      'xbob',
      'xbob.db',
    ],

    entry_points = {
      # declare database to bob
      'bob.db': [
        'voxforge = xbob.db.voxforge.driver:Interface',
        ],

      # declare tests to bob
      'bob.test': [
        'voxforge = xbob.db.voxforge.test:VoxforgeDatabaseTest',
        ],
      },

    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Education',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'Topic :: Database :: Front-Ends',
      ],
)
