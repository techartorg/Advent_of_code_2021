from time import perf_counter
from functools import wraps
from collections import deque
from itertools import islice


"""
Courtesy of Chris Cunningham on the Tech-Art slack
"""

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        ret = func(*args, **kwargs)
        print(f"{func.__name__.replace('_', ' ')} took: {perf_counter() - start:.8f} seconds")
        return ret
    return wrapper


def rolling_window(iterable, n):
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)