# -*- coding: utf-8 -*-
"""
PRequests allows you to use Requests with multiprocessing.pool to make asyncronous HTTP
Requests easily.

Usage
-----

Usage is simple::

    import prequests

    urls = [
        'http://www.heroku.com',
        'http://tablib.org',
        'http://httpbin.org',
        'http://python-requests.org',
        'http://kennethreitz.com'
    ]

Create a set of unsent Requests::

    >>> rs = (prequests.get(u) for u in urls)

Send them all at the same time::

    >>> prequests.map(rs)
    [<Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>]

"""

from setuptools import setup

install_requires = ['requests']


setup(
    name='prequests',
    version='0.1.0',
    url='https://github.com/leVirve/prequests.git',
    license='BSD',
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    description='Requests + Multiprocessing.Pool',
    long_description=__doc__,
    install_requires=install_requires,
    py_modules=['prequests'],
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
