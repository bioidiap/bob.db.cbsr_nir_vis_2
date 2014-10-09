.. vim: set fileencoding=utf-8 :
.. Manuel Guenther <manuel.guenther@idiap.ch>
.. Thu Sep  4 11:35:05 CEST 2014


=======================================================
 CASIA NIR-VIS 2.0 Face Database protocol
=======================================================

Bla



Installation
------------

Just download this package and decompress it locally::

  $ wget http://
  $ unzip 
  $ cd 

Use buildout to bootstrap and have a working environment ready for
experiments::

  $ python bootstrap
  $ ./bin/buildout

This also requires that bob (>= 1.2.0) is installed.


Mapping between the CASIA files and our database files
------------------------------------------------------

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





Getting the data
~~~~~~~~~~~~~~~~

The data can be downloaded from in the following URL (http://www.cbsr.ia.ac.cn/english/NIR-VIS-2.0-Database.html)::

In case you need a help, please contact us.
