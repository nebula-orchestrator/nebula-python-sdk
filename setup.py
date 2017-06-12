__author__ = 'Naor Livne'
__author_email__ = 'naorlivne@gmail.com'
__version__ = '0.7'

from setuptools import setup, find_packages

setup(name='NebulaPythonSDK',
      author=__author__,
      author_email=__author_email__,
      version=__version__,
      description="NebulaPythonSDK is a Pythonic SDK to manage Nebula container orchestrator,",
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      scripts=['setup.py'],
      license="GPLv3",
      keywords="nebula container orchestrator sdk",
      url="https://github.com/nebula-orchestrator/nebula-python-sdk",
      install_requires=['requests>=2.3.0'],
      classifiers=["Development Status :: 4 - Beta",
                   "Environment :: Other Environment",
                   "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                   "Operating System :: OS Independent",
                   "Intended Audience :: Developers",
                   "Intended Audience :: System Administrators",
                   "Topic :: Internet :: WWW/HTTP",
                   "Topic :: Software Development :: Libraries :: Python Modules"])
