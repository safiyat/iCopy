"""
An intelligent tool to copy (and move, in future) files and directories from
one location to another.
"""

from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='icopy',

    version='0.1',

    description='A commandline tool to intelligently copy (and move, in ' \
    'future). files and directories from one location to another.',
    long_description=long_description,

    url='https://github.com/safiyat/iCopy',

    author='Md Safiyat Reza',
    author_email='reza.safiyat@acm.org',

    license='GPLv2',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers, System Administrators',
        'Topic :: System :: Software Distribution',

        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],

    keywords='copy file utility commandline tool',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'argparse==1.2.1',
    ],

    extras_require={
    },

    package_data={
    },

    data_files=[],

    entry_points={
        'console_scripts': [
            'icopy=icopy:main',
        ],
    },
)
