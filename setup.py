from setuptools import setup, find_packages

setup(

    name='xbob.paper.tpami2013',
    version='0.0.1a1',
    description='Example on how to use the scalable implementation of PLDA and how to reproduce experiments of the article',
    url='http://pypi.python.org/pypi/xbob.paper.tpami2013',
    license='GPLv3',
    author='Laurent El Shafey',
    author_email='Laurent.El-Shafey@idiap.ch',
    long_description=open('README.rst').read(),

    packages=find_packages(),
    include_package_data=True,

    install_requires=[
      'setuptools',
      'xbob.db.verification.filelist',
    ],

    namespace_packages = [
      'xbob',
      'xbob.db',
    ],

    classifiers = [
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Education',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      ],
)
