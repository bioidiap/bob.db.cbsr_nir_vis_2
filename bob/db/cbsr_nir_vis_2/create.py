#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Tiago de Freitas Pereira <tiago.pereira@idiap.ch>
# @date:   Tue Aug  11 14:07:00 CEST 2015
#
# Copyright (C) 2011-2013 Idiap Research Institute, Martigny, Switzerland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
This script creates the CBSR NIR VIS NIR Dataset in a single pass.

Mapping between the casia format and bob.db format

norm -- train_world.lst = nir_train_dev.txt + vis_train_dev.txt

dev ------ for_models.lst = vis_gallery_dev.txt
       |-- for_probes.lst = nir_probe_dev.txt
       |
       |
test1  |-- for_models.lst = vis_gallery_1.txt
       |-- for_probes.lst = nir_probe_1.txt
test2  |-- for_models.lst = vis_gallery_2.txt
  .    |-- for_probes.lst = nir_probe_2.txt
  .
  .
  .
  .
test10 |-- for_models.lst = vis_gallery_10.txt
       |-- for_probes.lst = nir_probe_10.txt


"""

import os

from .models import *
from .models import PROTOCOLS, GROUPS, PURPOSES
import pkg_resources


def _update(session, field):
  """Add, updates and returns the given field for in the current session"""
  session.add(field)
  session.flush()
  session.refresh(field)
  return field


def add_clients_files(session, protocol_dir, annotation_dir, protocol_file, verbose = True):
  """
  Add the clients and files in one single shot
  
  """
  
  clients  = {} #Controling the clients and the sessions captured for each client
  file_id_offset = 0
  file_paths  = {} 
  
  protocols = os.listdir(protocol_dir)
  
  for p in protocols:

    #Checking the file is a protocol file
    if os.path.splitext(p)[1] != ".txt":
      continue

    if verbose>=1: print("Processing {0}".format(p))
    
    files = open(os.path.join(protocol_dir, p)).readlines()
    for f in files:
      f = f.rstrip("\r\n").replace("\\","/")
  
      # Adding client
      client_name = f.split("/")[2]  
      if(not client_name in clients):
        clients[client_name] = 1
        add_client(session, client_name, verbose=verbose)
      else:
        clients[client_name] += 1 #If the client already exists in the database, include the session
        
      # Adding file
      image_name = os.path.splitext(f)[0]
      if image_name in file_paths:
        continue
      
      file_id_offset += 1
      
      file_paths[image_name] = file_id_offset
      modality = image_name.split("/")[1]
      capture_session = image_name.split("/")[0]
      session.add(File(file_id=file_id_offset, client_id = client_name, image_name = image_name, modality=modality, session=capture_session))

      annotation_filename = os.path.join(annotation_dir, image_name+".pos")
      add_annotations(session, file_id_offset, annotation_filename, verbose = True)
      
  return file_paths


def add_client(session, client_name, verbose = True):

  """Adds the clients and split up the groups 'world', 'dev', and 'eval'"""
  
  if verbose>=1: print("  Adding client {0}".format(client_name))  
  session.add(Client(id=client_name))


def add_annotations(session, file_id, annotation_filename, verbose = True):

  """Adds the Files"""
  annotations = open(annotation_filename).readlines()[0].rstrip("\n").split(" ")
  if verbose>=1: print("  Adding annotation {0}".format(annotation_filename))
  #session.add(Annotation(file_id = file_id, re_x=annotations[2], re_y=annotations[3], le_x=annotations[0], le_y=annotations[1] ))
  session.add(Annotation(file_id = file_id, re_x=annotations[0], re_y=annotations[1], le_x=annotations[2], le_y=annotations[3] ))


def add_protocols(session, protocol_file, file_paths, protocol, group, purpose, verbose = True):

  files = open(protocol_file).readlines()
  for f in files:
    f = os.path.splitext(f.rstrip("\r\n").replace("\\","/"))[0]
    file_id = file_paths[f]
    
    query = session.query(Protocol_File_Association) \
     .filter(Protocol_File_Association.protocol     == protocol) \
     .filter(Protocol_File_Association.group == group) \
     .filter(Protocol_File_Association.purpose == purpose) \
     .filter(Protocol_File_Association.file_id == file_id)

    if len(query.all()) == 0:
      session.add(Protocol_File_Association(protocol=protocol, group=group, purpose=purpose, file_id=file_id))


def create_tables(args):
  """Creates all necessary tables (only to be used at the first time)"""

  from bob.db.base.utils import create_engine_try_nolock

  engine = create_engine_try_nolock(args.type, args.files[0], echo=(args.verbose >= 2));
  Client.metadata.create_all(engine)
  File.metadata.create_all(engine) 
  Annotation.metadata.create_all(engine)
  Protocol_File_Association.metadata.create_all(engine)


# Driver API
# ==========

def create(args):
  """Creates or re-creates this database"""

  from bob.db.base.utils import session_try_nolock

  dbfile = args.files[0]

  if args.recreate:
    if args.verbose and os.path.exists(dbfile):
      print('unlinking %s...' % dbfile)
    if os.path.exists(dbfile): os.unlink(dbfile)

  if not os.path.exists(os.path.dirname(dbfile)):
    os.makedirs(os.path.dirname(dbfile))

  # the real work...
  create_tables(args)
  session = session_try_nolock(args.type, args.files[0], echo=(args.verbose >= 2))
  file_paths = add_clients_files(session, os.path.join(args.image_dir, "protocols"), args.annotations_dir, args.verbose)

  fold = 0  
  for p in PROTOCOLS:
    fold += 1
  
    # Adding world
    add_protocols(session, os.path.join(args.image_dir, "protocols", "nir_train_dev.txt"),file_paths, p, "world", "train")
  
    add_protocols(session, os.path.join(args.image_dir, "protocols", "vis_train_dev.txt"), file_paths, p, "world", "train")
    
    #file_name = "vis_train_{0}.txt".format(fold)
    #add_protocols(session, os.path.join(args.image_dir, "protocols", file_name),file_paths, p, "world", "train")
    
    #file_name = "nir_train_{0}.txt".format(fold)
    #add_protocols(session, os.path.join(args.image_dir, "protocols", file_name),file_paths, p, "world", "train")
  
    # Adding dev
    add_protocols(session, os.path.join(args.image_dir, "protocols", "vis_gallery_dev.txt"), file_paths, p, "dev", "enroll")

    add_protocols(session, os.path.join(args.image_dir, "protocols", "nir_probe_dev.txt"), file_paths, p, "dev", "probe")

    # Adding eval
    file_name = "vis_gallery_{0}.txt".format(fold)
    add_protocols(session, os.path.join(args.image_dir, "protocols", file_name), file_paths, p, "eval", "enroll")

    file_name = "nir_probe_{0}.txt".format(fold)
    add_protocols(session, os.path.join(args.image_dir, "protocols", file_name), file_paths, p, "eval", "probe")

  session.commit()
  session.close()

def add_command(subparsers):
  """Add specific subcommands that the action "create" can use"""

  parser = subparsers.add_parser('create', help=create.__doc__)

  parser.add_argument('-r', '--recreate', action='store_true', help='If set, I\'ll first erase the current database')
  parser.add_argument('-v', '--verbose', action='count', help='Increase verbosity?')
  parser.add_argument('-d', '--image-dir', default='/idiap/resource/database/cbsr_nir_vis_2/', help="Change the relative path to the directory containing the images of the CBSR NIR VIS 2 database.")
  parser.add_argument('-a', '--annotations-dir', default='/idiap/resource/database/cbsr_nir_vis_2/annotations/', help="Change the relative path to the directory containing the images of the CBSR NIR VIS 2 database.")  

  parser.set_defaults(func=create) #action
