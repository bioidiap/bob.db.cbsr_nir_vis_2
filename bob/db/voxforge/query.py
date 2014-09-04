#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Elie Khoruy <Elie.Khoury@idiap.ch>
# @date: Thu Aug 22 17:49:19 CEST 2013
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

import bob.db.verification.filelist

class Database(bob.db.verification.filelist.Database):
  """Wrapper class for the subVoxforge database for speaker recognition (http://www.voxforge.org/).
  this class defines a simple protocol for training, dev and and by splitting the audio files of the database in three main parts.
  """

  def __init__(self, original_directory = None, original_extension = None):
    # call base class constructor
    from pkg_resources import resource_filename
    lists = resource_filename(__name__, 'lists')
    bob.db.verification.filelist.Database.__init__(self, lists, original_directory = original_directory, original_extension = original_extension)

