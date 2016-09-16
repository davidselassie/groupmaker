"""Module with duplicate finding utility functions."""


def find_duplicates(iterable):
    """Yield out duplicates in an input iterable.

    >>> list(find_duplicates([1, 2, 2, 3]))
    [2]
    >>> list(find_duplicates([1, 2, 3]))
    []
    """
    seen = set()
    for x in iterable:
        if x in seen:
            yield x
        else:
            seen.add(x)
