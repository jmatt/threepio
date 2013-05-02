import os
import setuptools
from threepio.version import get_version

readme = open('README.md').read()

long_description = """
threepio %s
Minimally improved noise for python. Pragmatic, minimal improved logging for python.

To install use pip install git+git://github.com/jmatt/threepio

----

%s

----

For more information, please see: https://github.com/jmatt/threepio
""" % (get_version('short'), readme)

setuptools.setup(
    name='threepio',
    version=get_version('short'),
    author='jmatt',
    author_email='jmatt@jmatt.org',
    description="Minimally improved noise for python. Pragmatic, minimal"
    "improved logging for python.",
    long_description=long_description,
    license="Apache License, Version 2.0",
    url="https://github.com/jmatt/threepio",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Logging"
    ])
