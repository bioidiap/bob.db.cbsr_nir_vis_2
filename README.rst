Speaker recognition protocol on the Voxforge Database 
=====================================================

`Voxforge`_ offers a collection transcribed speech for use with **Free** and **Open Source Speech Recognition Engines**. 
In this package, we design a speaker recognition protocol that uses a **small subset of the english audio files** (only 6561 files) belonging to **30 speakers** randomly selected.
This subset is split into three equivalent parts: Training (10 speakers), Development (10 speakers) and Test (10 speakers) sets.
 
This package serves as a toy example of speaker recognition database while testing `xbob.speaker_recognition`_.

The `xbob.speaker_recognition`_  is developed at Idiap during its participation to the `NIST SRE 2012 evaluation`_. If you use this package and/or its results, please cite the following
publications:

1. The original paper presented at the NIST SRE 2012 workshop::

     @inproceedings{Khoury_NISTSRE_2012,
       author = {Khoury, Elie and El Shafey, Laurent and Marcel, S{\'{e}}bastien},
       month = {dec},
       title = {The Idiap Speaker Recognition Evaluation System at NIST SRE 2012},
       booktitle = {NIST Speaker Recognition Conference},
       year = {2012},
       location = {Orlando, USA},
       organization = {NIST},
       pdf = {http://publications.idiap.ch/downloads/papers/2012/Khoury_NISTSRE_2012.pdf}
    }

2. Bob as the core framework used to run the experiments::

    @inproceedings{Anjos_ACMMM_2012,
      author = {A. Anjos and L. El Shafey and R. Wallace and M. G\"unther and C. McCool and S. Marcel},
      title = {Bob: a free signal processing and machine learning toolbox for researchers},
      year = {2012},
      month = oct,
      booktitle = {20th ACM Conference on Multimedia Systems (ACMMM), Nara, Japan},
      publisher = {ACM Press},
      url = {http://publications.idiap.ch/downloads/papers/2012/Anjos_Bob_ACMMM12.pdf},
    }



Installation
------------

Just download this package and decompress it locally::

  $ wget http://pypi.python.org/packages/source/x/xbob.voxforge/xbob.db.voxforge-0.0.1.zip
  $ unzip xbob.db.voxforge-0.0.1.zip
  $ cd xbob.db.voxforge

Use buildout to bootstrap and have a working environment ready for
experiments::

  $ python bootstrap
  $ ./bin/buildout

This also requires that bob (>= 1.2.0) is installed.


Getting the data
~~~~~~~~~~~~~~~~

The data can be downloaded from its original URL (on Voxforge) and extracted by running `download_and_untar.sh`_ that takes as input the path in which the data will be stored::

  $ ./download_and_untar.sh PATH/TO/WAV/DIRECTORY

.. _Voxforge: http://www.voxforge.org/
.. _xbob.speaker_recognition: https://github.com/bioidiap/xbob.speaker_recognition
.. _NIST SRE 2012 evaluation: http://www.nist.gov/itl/iad/mig/sre12.cfm
.. _download_and_untar.sh: https://github.com/bioidiap/xbob.db.voxforge/blob/master/download_and_untar.sh
