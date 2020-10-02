.. vim: set fileencoding=utf-8 :
.. Tiago de Freitas Pereira <tiago.pereira@idiap.ch>
.. Thu Sep  4 11:35:05 CEST 2014

.. image:: https://img.shields.io/badge/docs-available-orange.svg
   :target: https://www.idiap.ch/software/bob/docs/bob/bob.db.cbsr_nir_vis_2/master/index.html
.. image:: https://gitlab.idiap.ch/bob/bob.db.cbsr_nir_vis_2/badges/v2.0.7/pipeline.svg
   :target: https://gitlab.idiap.ch/bob/bob.db.cbsr_nir_vis_2/commits/v2.0.7
.. image:: https://gitlab.idiap.ch/bob/bob.db.cbsr_nir_vis_2/badges/v2.0.7/coverage.svg
   :target: https://gitlab.idiap.ch/bob/bob.db.cbsr_nir_vis_2/commits/v2.0.7
.. image:: https://img.shields.io/badge/gitlab-project-0000c0.svg
   :target: https://gitlab.idiap.ch/bob/bob.db.cbsr_nir_vis_2

=================================
 CASIA NIR-VIS 2.0 Face Database
=================================

This package contains the access API and descriptions for the `CASIA NIR-VIS
2.0 database <http://www.cbsr.ia.ac.cn/english/NIR-VIS-2.0-Database.html>`_.
The actual raw data for the database should be downloaded from the original
URL. This package only contains the Bob accessor methods to use the DB
directly from python, with the original protocol of the database.

CASIA NIR-VIS 2.0 database offers pairs of mugshot images and their
correspondent NIR photos. Capured by CASIA (Chinese Academy of Sciences), the
images of this database were collected in four recording sessions: 2007 spring,
2009 summer, 2009 fall and 2010 summer, in which the first session is identical
to the `HFB database <http://www.cbsr.ia.ac.cn/english/HFB%20Databases.asp>`_.
The CASIA NIR-VIS 2.0 database consists of 725 subjects in total. There are
1-22 VIS and 5-50 NIR face images per subject.

Installation
------------

Follow our `installation`_ instructions. Then, to install this package, run::
   
   $ conda install bob.db.cbsr_nir_vis_2


Contact
-------

For questions or reporting issues to this software package, contact our
development `mailing list`_.


.. Place your references here:
.. _bob: https://www.idiap.ch/software/bob
.. _installation: https://gitlab.idiap.ch/bob/bob/wikis/Installation
.. _mailing list: https://groups.google.com/forum/?fromgroups#!forum/bob-devel
