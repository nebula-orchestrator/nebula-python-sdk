from setuptools import setup, find_packages

__author__ = 'Naor Livne'
__author_email__ = 'naorlivne@gmail.com'
__version__ = '2.6.1'

with open('README.md') as f:
    long_description = f.read()

requirements = [
    'requests>=2.3.0',
    'six>=1.12.0'
]

setup(name='NebulaPythonSDK',
      author=__author__,
      author_email=__author_email__,
      version=__version__,
      description="NebulaPythonSDK is a Pythonic SDK to manage Nebula container orchestrator",
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      scripts=['setup.py'],
      license="LGPLv3",
      keywords="nebula container orchestrator sdk",
      url="https://github.com/nebula-orchestrator/nebula-python-sdk",
      install_requires=requirements,
      classifiers=["Development Status :: 5 - Production/Stable",
                   "Environment :: Other Environment",
                   "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
                   "Operating System :: OS Independent",
                   "Intended Audience :: Developers",
                   "Intended Audience :: System Administrators",
                   "Topic :: Internet :: WWW/HTTP",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.4",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6",
                   "Programming Language :: Python :: 3.7"])
