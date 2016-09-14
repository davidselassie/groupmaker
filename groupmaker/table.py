"""Functions to print tables of student pairings."""
import sys

from tabulate import tabulate

from .scoring import calc_pair_to_count_of_groups_set


def _pair(name1, name2):
    """Manually pair two names in order for comparison to a pair count dict.

    >>> _pair('B', 'A')
    ('A', 'B')
    """
    return tuple(sorted((name1, name2)))


def calc_names_count_matrix(names, groups_set):
    """Produce a matrix of how often names have been paired together in a set
    of groups.

    Returns an ordered list of names and the matrix in that order.

    >>> calc_names_count_matrix(['A', 'B'],
    ...                         [[['A', 'B']], [['A']]])
    (['A', 'B'], [[2, 1], [1, 1]])
    >>> calc_names_count_matrix(['B', 'A'],
    ...                         [[['A', 'B']], [['A']]])
    (['A', 'B'], [[2, 1], [1, 1]])
    >>> calc_names_count_matrix(['A', 'B'],
    ...                         [[['A']], [['A']]])
    (['A', 'B'], [[2, 0], [0, 0]])
    """
    names = sorted(names)
    pair_to_count = calc_pair_to_count_of_groups_set(groups_set)
    count_matrix = [
        [
            pair_to_count.get(_pair(name1, name2), 0)
            for name2
            in names
        ]
        for name1
        in names
    ]
    return names, count_matrix


def print_name_count_matrix(names, count_matrix, file=sys.stdout):
    """Print a matrix of names and counts.

    >>> print_name_count_matrix(['A', 'B', 'C'],
    ...                         [[0, 1, 1], [1, 0, 2], [1, 2, 0]])
    +----+-----+-----+-----+
    |    |   A |   B |   C |
    |----+-----+-----+-----|
    | A  |   0 |   1 |   1 |
    | B  |   1 |   0 |   2 |
    | C  |   1 |   2 |   0 |
    +----+-----+-----+-----+
    """
    table = [[name] + counts for name, counts in zip(names, count_matrix)]
    print(tabulate(table, names, tablefmt='psql'), file=file)


def calc_print_name_count_matrix(names, groups_set, file=sys.stdout):
    """Calculate and print a matrix of names to counts."""
    historical_names, historical_count_matrix = calc_names_count_matrix(
        names,
        groups_set)
    print_name_count_matrix(historical_names, historical_count_matrix, file=file)
