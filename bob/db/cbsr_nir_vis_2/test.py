#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>
# Thu Oct 09 11:27:27 CEST 2014
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

"""A few checks on the protocols of a subset of the CASIA NIR-VIS 2.0 database
"""

import bob.db.cbsr_nir_vis_2

possible_protocols  = ["view2_1", "view2_2", "view2_3", "view2_4", "view2_5", "view2_6", "view2_7", "view2_8", "view2_9", "view2_10"]

def test_protocols():
  import os

  db = bob.db.cbsr_nir_vis_2.Database()
  available_protocols = os.listdir(db.get_base_directory())

  for p in possible_protocols:
    assert p  in available_protocols


def test_clients():

  db = bob.db.cbsr_nir_vis_2.Database()
  for p in possible_protocols:

    #Checking clients
    assert len(db.client_ids(protocol=p)) == 715
    assert len(db.client_ids(protocol=p, groups="world")) == 357
    assert len(db.client_ids(protocol=p, groups="dev")) == 358
    assert len(db.client_ids(protocol=p, groups="eval")) == 358


def test_objects():

  db = bob.db.cbsr_nir_vis_2.Database()
  for p in possible_protocols:

    #Checking groups
    assert len(db.groups(protocol=p)) == 3

    #cheking files
    assert len(db.objects(protocol=p))== 15371
    assert len(db.objects(protocol=p, groups="world"))== 8750
    assert len(db.objects(protocol=p, groups="dev"))== 6481
    assert len(db.objects(protocol=p, groups="eval"))== 6566

    assert len(db.objects(protocol=p, groups="dev", purposes="enrol"))== 358
    assert len(db.objects(protocol=p, groups="dev", purposes="probe"))== 6123

    assert len(db.objects(protocol=p, groups="eval", purposes="enrol"))== 358
    assert len(db.objects(protocol=p, groups="eval", purposes="probe"))== 6208



    

