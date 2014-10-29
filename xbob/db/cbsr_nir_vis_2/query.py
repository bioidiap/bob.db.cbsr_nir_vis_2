#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>
# Thu Oct 09 11:27:27 CEST 2014
#
# Copyright (C) 2012-2014 Idiap Research Institute, Martigny, Switzerland
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

import xbob.db.verification.filelist

class Database(xbob.db.verification.filelist.Database):
  """Wrapper class for the CASIA NIR-VIS 2.0 database for face recognition recognition (http://www.cbsr.ia.ac.cn/english/NIR-VIS-2.0-Database.html).
  this class defines a simple protocol for training, dev and and by splitting the audio files of the database in three main parts.
  """

  def __init__(self, original_directory = None, original_extension = None, annotation_directory=None, annotation_type="eyecenter", annotation_extension=".pos"):
    # call base class constructor
    from pkg_resources import resource_filename
    lists = resource_filename(__name__, 'lists')
    #xbob.db.verification.filelist.Database.__init__(self, lists, original_directory=original_directory, original_extension = original_extension, annotation_directory=annotation_directory)
    xbob.db.verification.filelist.Database.__init__(self, lists, original_directory)

    self.m_annotation_directory = annotation_directory
    self.m_annotation_extension = annotation_extension
    self.original_extension = original_extension
    self.m_annotation_type = annotation_type

  def tobjects(self, protocol=None, model_ids=None, groups=None):
    #No TObjects    
    return []


  def zobjects(self, protocol=None, groups=None):
    #No TObjects    
    return []


  def annotations(self, file_id):
    """Reads the annotations for the given file id from file and returns them in a dictionary.
    If you don't have a copy of the annotation files, you can download them under http://www.idiap.ch/resource/biometric.
    Keyword parameters:
    file_id
    The ID of the file for which the annotations should be read.
    Return value
    The annotations as a dictionary: {'reye':(re_y,re_x), 'leye':(le_y,le_x)}
    """
    if self.m_annotation_directory is None:
      return None
    # since the file id is equal to the file name, we can simply use it
    annotation_file = os.path.join(self.m_annotation_directory, file_id + self.m_annotation_extension)
    # return the annotations as read from file
    return xbob.db.verification.utils.read_annotation_file(annotation_file, self.m_annotation_type)

