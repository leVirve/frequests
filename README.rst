FRequests: Asyncronous Requests
===============================

FRequests allows you to use Requests with futures to make asyncronous HTTP
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


Installation
------------

Installation is easy with pip::

    $ pip install frequests
