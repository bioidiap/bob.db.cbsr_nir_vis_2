#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Laurent El Shafey <Laurent.El-Shafey@idiap.ch>
# Fri Aug 23 12:32:01 CEST 2013
#
# Copyright (C) 2011-2014 Idiap Research Institute, Martigny, Switzerland
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

from setuptools import setup, find_packages, dist
dist.Distribution(dict(setup_requires=['bob.extension']))

from bob.extension.utils import load_requirements
install_requires = load_requirements()

# Define package version
version = open("version.txt").read().rstrip()


setup(

    name='bob.db.cbsr_nir_vis_2',
    version=version,
    description='CASIA NIR-VIS 2.0 Face Database protocol',
    url='https://gitlab.idiap.ch/biometric/bob.db.cbsr_nir_vis_2',
    license='BSD',
    keywords = "",
    author='Tiago de Freitas Pereira',
    author_email='tiago.pereira@idiap.ch',
    long_description=open('README.rst').read(),

    packages=find_packages(),
    include_package_data=True,
    zip_safe = False,

    install_requires=install_requires,

    entry_points = {
      'bob.db': [
        'cbsr_nir_vis_2 = bob.db.cbsr_nir_vis_2.driver:Interface',
      ], 
      
      # scripts should be declared using this entry:
      'console_scripts' : [
      ],
    },
    
    

    classifiers = [
      'Framework :: Bob',
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Education',
      'License :: OSI Approved :: BSD License',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'Topic :: Database :: Front-Ends',
    ],
)
