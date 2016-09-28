# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # Application name:
    name="blynkapi",

    # Version number (initial):
    version="0.1.3",

    description="This is a simple blynk HTTP/HTTPS API wrapper.",
    long_description=long_description,

    #URL
    url='https://github.com/xandr2/blynkapi',
    download_url = 'https://github.com/xandr2/blynkapi/archive/0.1.3.tar.gz',

    # Application author details:
    author="Alexandr Borysov",
    author_email="xandr2@gmail.com",

    # License
    license='MIT',

    keywords=['python', 'blynk', 'HTTP/HTTPS', 'API', 'wrapper'],

    # Packages
    packages=["blynkapi"],

    # Include additional files into the package
    #include_package_data=True,

    #
    # license="LICENSE.txt",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    #install_requires=[
    #    "urllib2",
    #],
    classifiers = [],
)
