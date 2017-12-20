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
  available_protocols = db.protocols()

  for p in possible_protocols:
    assert p  in available_protocols


def test_clients():
  db = bob.db.cbsr_nir_vis_2.Database()
  
  for p in possible_protocols:
 
    #Checking clients
    assert len(db.clients(protocol=p)) == 715
    assert len(db.clients(protocol=p, groups="world")) == 357
    assert len(db.clients(protocol=p, groups="dev")) == 358
    assert len(db.clients(protocol=p, groups="eval")) == 358


def test_objects():

  db = bob.db.cbsr_nir_vis_2.Database()
  p = "view2_1"
  #Checking groups
  assert len(db.groups(protocol=p)) == 3

  #cheking files
  assert len(db.objects(protocol=p))== 8750+6481+6566
  assert len(db.objects(protocol=p, groups="world"))== 8750

  # Checking the modalities
  assert len(db.objects(protocol=p, groups="world", modality=["VIS"])) == 2480
  assert len(db.objects(protocol=p, groups="world", modality=["NIR"])) == 6270
  
  assert len(db.objects(protocol=p, groups="dev"))== 6481
  assert len(db.objects(protocol=p, groups="eval"))== 6566

  assert len(db.objects(protocol=p, groups="dev", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="dev", purposes="probe"))== 6123

  assert len(db.objects(protocol=p, groups="eval", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="eval", purposes="probe"))== 6208


  p = "view2_2"
  #Checking groups
  assert len(db.groups(protocol=p)) == 3

  #cheking files 
  assert len(db.objects(protocol=p))== 8750+6481+6590
  assert len(db.objects(protocol=p, groups="world"))== 8750

  assert len(db.objects(protocol=p, groups="world", modality=["VIS"])) == 2480
  assert len(db.objects(protocol=p, groups="world", modality=["NIR"])) == 6270
  
  assert len(db.objects(protocol=p, groups="dev"))== 6481
  assert len(db.objects(protocol=p, groups="eval"))== 6590

  assert len(db.objects(protocol=p, groups="dev", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="dev", purposes="probe"))== 6123

  assert len(db.objects(protocol=p, groups="eval", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="eval", purposes="probe"))== 6232


  p = "view2_3"
  #Checking groups
  assert len(db.groups(protocol=p)) == 3

  #cheking files 
  assert len(db.objects(protocol=p))== 8750+6481+6568
  assert len(db.objects(protocol=p, groups="world"))== 8750
  assert len(db.objects(protocol=p, groups="dev"))== 6481
  assert len(db.objects(protocol=p, groups="eval"))== 6568

  assert len(db.objects(protocol=p, groups="dev", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="dev", purposes="probe"))== 6123

  assert len(db.objects(protocol=p, groups="eval", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="eval", purposes="probe"))== 6210


  p = "view2_4"
  #Checking groups
  assert len(db.groups(protocol=p)) == 3

  #cheking files 
  assert len(db.objects(protocol=p))== 8750+6481+6413
  assert len(db.objects(protocol=p, groups="world"))== 8750
  assert len(db.objects(protocol=p, groups="dev"))== 6481
  assert len(db.objects(protocol=p, groups="eval"))== 6413

  assert len(db.objects(protocol=p, groups="dev", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="dev", purposes="probe"))== 6123

  assert len(db.objects(protocol=p, groups="eval", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="eval", purposes="probe"))== 6055


  p = "view2_5"
  #Checking groups
  assert len(db.groups(protocol=p)) == 3

  #cheking files 
  assert len(db.objects(protocol=p))== 8750+6481+6562
  assert len(db.objects(protocol=p, groups="world"))== 8750
  assert len(db.objects(protocol=p, groups="dev"))== 6481
  assert len(db.objects(protocol=p, groups="eval"))== 6562

  assert len(db.objects(protocol=p, groups="dev", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="dev", purposes="probe"))== 6123

  assert len(db.objects(protocol=p, groups="eval", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="eval", purposes="probe"))== 6204


  p = "view2_6"
  #Checking groups
  assert len(db.groups(protocol=p)) == 3

  #cheking files 
  assert len(db.objects(protocol=p))== 8750+6481+6549
  assert len(db.objects(protocol=p, groups="world"))== 8750
  assert len(db.objects(protocol=p, groups="dev"))== 6481
  assert len(db.objects(protocol=p, groups="eval"))== 6549

  assert len(db.objects(protocol=p, groups="dev", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="dev", purposes="probe"))== 6123

  assert len(db.objects(protocol=p, groups="eval", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="eval", purposes="probe"))== 6191
  

  p = "view2_7"
  #Checking groups
  assert len(db.groups(protocol=p)) == 3

  #cheking files 
  assert len(db.objects(protocol=p))== 8750+6481+6605
  assert len(db.objects(protocol=p, groups="world"))== 8750
  assert len(db.objects(protocol=p, groups="dev"))== 6481
  assert len(db.objects(protocol=p, groups="eval"))== 6605

  assert len(db.objects(protocol=p, groups="dev", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="dev", purposes="probe"))== 6123

  assert len(db.objects(protocol=p, groups="eval", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="eval", purposes="probe"))== 6247


  p = "view2_8"
  #Checking groups
  assert len(db.groups(protocol=p)) == 3

  #cheking files 
  assert len(db.objects(protocol=p))== 8750+6481+6580
  assert len(db.objects(protocol=p, groups="world"))== 8750
  assert len(db.objects(protocol=p, groups="dev"))== 6481
  assert len(db.objects(protocol=p, groups="eval"))== 6580

  assert len(db.objects(protocol=p, groups="dev", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="dev", purposes="probe"))== 6123

  assert len(db.objects(protocol=p, groups="eval", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="eval", purposes="probe"))== 6222


  p = "view2_9"
  #Checking groups
  assert len(db.groups(protocol=p)) == 3

  #cheking files 
  assert len(db.objects(protocol=p))== 8750+6481+6520
  assert len(db.objects(protocol=p, groups="world"))== 8750
  assert len(db.objects(protocol=p, groups="dev"))== 6481
  assert len(db.objects(protocol=p, groups="eval"))== 6520

  assert len(db.objects(protocol=p, groups="dev", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="dev", purposes="probe"))== 6123

  assert len(db.objects(protocol=p, groups="eval", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="eval", purposes="probe"))== 6162


  #db = bob.db.cbsr_nir_vis_2.Database()
  p = "view2_10"
  #Checking groups
  assert len(db.groups(protocol=p)) == 3

  #cheking files 
  assert len(db.objects(protocol=p))== 8750+6481+6603
  assert len(db.objects(protocol=p, groups="world"))== 8750
  assert len(db.objects(protocol=p, groups="dev"))== 6481
  assert len(db.objects(protocol=p, groups="eval"))== 6603

  assert len(db.objects(protocol=p, groups="dev", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="dev", purposes="probe"))== 6123

  assert len(db.objects(protocol=p, groups="eval", purposes="enroll"))== 358
  assert len(db.objects(protocol=p, groups="eval", purposes="probe"))== 6245
