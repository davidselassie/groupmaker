"""Functions that generate groups."""
from itertools import permutations, zip_longest

from ._testing import rlist, rsorted


def _chunk(iterable, size):
    """Take an iterable and chunk it into iterables of a given size.
    Remaining chunks are fleshed out with Nones.

    >>> rlist(_chunk([1, 2, 3, 4], 3))
    [[1, 2, 3], [4, None, None]]
    """
    copies = [iter(iterable)] * size
    return zip_longest(*copies)


def all_groups_set(students, group_size):
    """Generate all possible unique groups of a given size from all students.
    Very permutive.

    >>> rsorted(all_groups_set(['A', 'B', 'C'], 2))
    ... # doctest: +NORMALIZE_WHITESPACE
    [[['A', 'B'], ['C', None]],
     [['A', 'C'], ['B', None]],
     [['A', None], ['B', 'C']]]
    """
    return frozenset(frozenset(frozenset(group)
                               for group in _chunk(ordering, group_size))
                     for ordering in permutations(students))
