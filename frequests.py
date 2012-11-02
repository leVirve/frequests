# -*- coding: utf-8 -*-

"""
frequests
~~~~~~~~~

This module contains an asynchronous replica of ``requests.api``, powered
by futures. All API methods return a ``Request`` instance (as opposed to
``Response``). A list of requests can be sent with ``map()``.
"""

import sys

if sys.version_info[0] == 2:
    try:
        from futures import ThreadPoolExecutor
    except ImportError:
        raise RuntimeError('futures is required for frequests on python 2.X')
else:
    from concurrent.futures import ThreadPoolExecutor

try:
    from requests import api
except ImportError:
    raise RuntimeError('requests is required for frequests')


__all__ = (
    'map', 'imap',
    'get', 'options', 'head', 'post', 'put', 'patch', 'delete', 'request'
)


def patched(f):
    """Patches a given API function to not send."""

    def wrapped(*args, **kwargs):

        kwargs['return_response'] = False
        kwargs['prefetch'] = True

        config = kwargs.get('config', {})
        config.update(safe_mode=True)

        kwargs['config'] = config

        return f(*args, **kwargs)

    return wrapped


# Patched requests.api functions.
get = patched(api.get)
options = patched(api.options)
head = patched(api.head)
post = patched(api.post)
put = patched(api.put)
patch = patched(api.patch)
delete = patched(api.delete)
request = patched(api.request)


def send(r, prefetch=False):
    """Just sends the request using its send method and returns its response.  """
    r.send(prefetch=prefetch)
    return r.response

def map(requests, prefetch=True, size=1, **kwargs):
    """Concurrently converts a list of Requests to Responses.

    :param requests: a collection of Request objects.
    :param prefetch: If False, the content will not be downloaded immediately.
    :param size: Specifies the number of requests to make at a time. If 1, no throttling occurs.
    """

    requests = list(requests)

    with ThreadPoolExecutor(max_workers=size) as executor:
        responses = list(executor.map(send, requests, [prefetch]*len(requests), **kwargs))

    return responses

def imap(requests, prefetch=True, size=2, **kwargs):
    """Concurrently converts a generator object of Requests to
    a generator of Responses.

    :param requests: a generator of Request objects.
    :param prefetch: If False, the content will not be downloaded immediately.
    :param size: Specifies the number of requests to make at a time. default is 2
    """

    def prefetch_generator():
        while True:
            yield prefetch

    with ThreadPoolExecutor(max_workers=size) as executor:
        for response in executor.map(send, requests, prefetch_generator(), **kwargs):
            yield response
