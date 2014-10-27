.. vim: set fileencoding=utf-8 :
.. Tiago de Freitas Pereira <tiago.pereira@idiap.ch>
.. Thu Sep  4 11:35:05 CEST 2014


=======================================================
 CASIA NIR-VIS 2.0 Face Database
=======================================================

This package contains the access API and descriptions for the `CASIA NIR-VIS 2.0 database <http://www.cbsr.ia.ac.cn/english/NIR-VIS-2.0-Database.html>`. 
The actual raw data for the database should be downloaded from the original URL. 
This package only contains the Bob accessor methods to use the DB directly from python, with the original protocol of the database.

CASIA NIR-VIS 2.0 database offers pairs of mugshot images and their correspondent NIR photos.
Capured by CASIA (Chinese Academy of Sciences), the images of this database were collected in four recording sessions: 2007 spring, 2009 summer, 2009 fall and 2010 summer, in which the first session is identical to the `HFB database <http://www.cbsr.ia.ac.cn/english/HFB%20Databases.asp>`. 
The CASIA NIR-VIS 2.0 database consists of 725 subjects in total. 
There are 1-22 VIS and 5-50 NIR face images per subject.

You would normally not install this package unless you are maintaining it. 
What you would do instead is to tie it in at the package you need to **use** it.
There are a few ways to achieve this:

1. You can add this package as a requirement at the ``setup.py`` for your own
   `satellite package
   <https://github.com/idiap/bob/wiki/Virtual-Work-Environments-with-Buildout>`_
   or to your Buildout ``.cfg`` file, if you prefer it that way. With this
   method, this package gets automatically downloaded and installed on your
   working environment, or

2. You can manually download and install this package using commands like
   ``easy_install`` or ``pip``.

The package is available in two different distribution formats:

1. You can download it from `PyPI <http://pypi.python.org/pypi>`_, or

2. You can download it in its source form from `its git repository
   <https://github.com/bioidiap/xbob.db.cbsr_nir_vis_2>`_.

You can mix and match points 1/2 and a/b above based on your requirements. Here
are some examples:

Modify your setup.py and download from PyPI
===========================================

That is the easiest. Edit your ``setup.py`` in your satellite package and add
the following entry in the ``install_requires`` section (note: ``...`` means
`whatever extra stuff you may have in-between`, don't put that on your
script)::

    install_requires=[
      ...
      "xbob.db.cbsr_nir_vis_2",
    ],

Proceed normally with your ``boostrap/buildout`` steps and you should be all
set. That means you can now import the ``xbob.db.cbsr_nir_vis_2`` namespace into your scripts.

Modify your buildout.cfg and download from git
==============================================

You will need to add a dependence to `mr.developer
<http://pypi.python.org/pypi/mr.developer/>`_ to be able to install from our
git repositories. Your ``buildout.cfg`` file should contain the following
lines::

  [buildout]
  ...
  extensions = mr.developer
  auto-checkout = *
  eggs = xbob.db.cbsr_nir_vis_2

  [sources]
  xbob.db.cbsr_nir_vis_2 = git https://github.com/bioidiap/xbob.db.cbsr_nir_vis_2.git branch= bob_1.2
  ...
