from collections import Iterable


def _is_container(x):
    """Return if the input is a container of other elements, but not a string.

    >>> _is_container(['1'])
    True
    >>> _is_container('Hi')
    False
    >>> _is_container(frozenset({}))
    True
    """
    return isinstance(x, Iterable) and not isinstance(x, str)


def rlist(l):
    """Recursively turn nested iterables into lists.

    >>> rlist(('A', ('B', )))
    ['A', ['B']]
    """
    return [i if not _is_container(i) else rlist(i) for i in l]


def rsorted(l):
    """Recursively sort nested iterables by their string value.

    Just a convenience function for doctesting.

    >>> rsorted(frozenset({'B', frozenset({'C', 'A'})}))
    ['B', ['A', 'C']]
    >>> rsorted(frozenset({'B', None, frozenset({'C', None, 'A'})}))
    ['B', None, ['A', 'C', None]]
    >>> rsorted(frozenset({
    ...                    frozenset({frozenset({'C'})}),
    ...                    frozenset({frozenset({None})})}))
    [[['C']], [[None]]]
    """
    return sorted((i if not _is_container(i) else rsorted(i) for i in l),
                  key=str)
