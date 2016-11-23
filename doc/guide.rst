.. vim: set fileencoding=utf-8 :
.. @author: Tiago de Freitas Pereira <tiago.pereira@idiap.ch>
.. @date:   Fri 29 Apr 2016 09:09:34 CEST 

==============
 User's Guide
==============

This package contains the access API and descriptions for the CASIA NIR-VIS 2.0 Database (`CASIA`_) database.
It only contains the Bob_ accessor methods to use the DB directly from python, with our certified protocols.
The actual raw data for the database should be downloaded from the original URL.

The Database Interface
----------------------

The :py:class:`bob.db.cbsr_nir_vis_2.Database` complies with the standard biometric verification database as described in `bob.db.base <bob.db.base>`_, implementing the interface :py:class:`bob.db.base.SQLiteDatabase`.


CASIA Protocols
--------------------


This database has a well defined protocol and it is publicly available for download `http://www.cbsr.ia.ac.cn/english/NIR-VIS-2.0-Database.html`. 
This package just organizes the provided txt files in a python API.


Search protocols
================

Defines a set of protocols for VIS->NIR and NIR->VIS face identification (search) in a **close-set**.

For each task (VIS->NIR) the 715 subjects are split in **10 sets** where:
 - 357 subjects are used for training
 - 358 subjects are used for evaluation

To fetch the object files using, lets say the first split for the VIS->NIR protocol, use the following piece of code:

.. code-block:: python

   >>> import bob.db.cbsr_nir_vis_2
   >>> db = bob.db.cbsr_nir_vis_2.Database()
   >>>
   >>> #fetching the files for training   
   >>> training = db.objects(protocol="view2_1", groups="world")
   >>>
   >>> #fetching the files for testing
   >>> galery =  db.objects(protocol="view2_1", groups="dev", purposes="enroll")
   >>> probes =  db.objects(protocol="view2_1", groups="dev", purposes="probe")
   >>>


To list the available protocols type:

.. code-block:: python

   >>> import bob.db.cbsr_nir_vis_2
   >>> db = bob.db.cbsr_nir_vis_2.Database()
   >>> print(db.protocols())




.. _CASIA: http://www.cbsr.ia.ac.cn/english/NIR-VIS-2.0-Database.html
.. _bob: https://www.idiap.ch/software/bob
