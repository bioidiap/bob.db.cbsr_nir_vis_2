# Elie Khoury <Elie.Khoury@idiap.ch>
# Date: Thu Aug 22 18:17:29 CEST 2013

#
# Copyright (C) 2012-2013 Idiap Research Institute, Martigny, Switzerland
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
#

# This script will download the audio files used in the protocol.
# It will first download the tgz files, and then decompress them.

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 DATA_DIR"
  exit 1
fi

baselink="http://www.repository.voxforge1.org/downloads/SpeechCorpus/Trunk/Audio/Main/16kHz_16bit"
directory=$1

mkdir -p $fulldirectory
while read filename; do
  basefilename=`basename $filename .tgz`
  echo $basefilename
  if [ ! -d "$directory/$basefilename" ]; then
    wget $baselink/$filename
    tar -zxvf $filename
    mv $basefilename $directory/.
    rm $filename
  fi
done < bob/db/voxforge/lists/list_of_tgz_files.lst # where the list of files is stored

