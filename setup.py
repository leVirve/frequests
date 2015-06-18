# -*- coding: utf-8 -*-
"""
FRequests allows you to use Requests with Gevent to make asyncronous HTTP
Requests easily.

Usage
-----

Usage is simple::

    import frequests

    urls = [
        'http://www.heroku.com',
        'http://tablib.org',
        'http://httpbin.org',
        'http://python-requests.org',
        'http://kennethreitz.com'
    ]

Create a set of unsent Requests::

    >>> rs = (frequests.get(u) for u in urls)

Send them all at the same time::

    >>> frequests.map(rs)
    [<Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>]

"""

import sys
from setuptools import setup

install_requires = ['requests']

if sys.version_info[0] == 2:
    install_requires.append('futures')

setup(
    name='frequests',
    version='0.1.1',
    url='https://github.com/i-trofimtschuk/frequests.git',
    license='BSD',
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    description='Requests + Futures',
    long_description=__doc__,
    install_requires=install_requires,
    py_modules=['frequests'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
