FRequests: Asyncronous Requests
===============================

FRequests allows you to use Requests with futures to make asyncronous HTTP
Requests easily.
If you're using Python 3.X you will have no external dependencies except
for requests.  On Python 2.X you will need futures from PyPI - a backport
of concurrency.futures from Python 3.X.
In either case you won't have to deal with the problems caused by gevents
monkey_patching. As frequests is thread based, i think it's slower
than grequests that is based on gevent. But frequests is meant to be an
easy to use solution that just works, not causing you any headakes and
should be 'fast enough' in the most cases.


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

    $ pip install -e git+https://github.com/i-trofimtschuk/frequests.git#egg=frequests
