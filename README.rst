PRequests: Asyncronous Requests
===============================

PRequests allows you to use Requests with Threadpool to make asyncronous HTTP
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


Installation
------------

Installation is easy with pip::

    $ pip install -e git+https://github.com/leVirve/prequests.git#egg=prequests
