"""Functions that read and write student and group files.

A student file contains one student name on each line.

A groups file contains a student name on each line with a blank line
between groups.
"""
import sys
from itertools import chain


def parse_students_file(students_file):
    r"""Read student file and return a sorted list of the students.

    >>> parse_students_file(['B\n', 'A\n', '\n'])
    ('A', 'B')
    """
    unique_names = (frozenset(name.strip() for name in students_file) -
                    frozenset({''}))
    return tuple(sorted(unique_names))


def parse_groups_file_paths(groups_file_paths):
    """Read all historical groups from a list of groups file paths.

    Return a set of all historical groups.
    """
    for groups_file_path in groups_file_paths:
        with open(groups_file_path) as groups_file:
            yield tuple(parse_groups_file(groups_file))


def parse_groups_file(groups_file):
    r"""Take a groups file and return all of the groups in it.

    >>> list(parse_groups_file(['A\n', 'B\n', '\n', 'C\n']))
    [('A', 'B'), ('C',)]
    """
    working_group = set()
    for name in map(str.strip, chain(groups_file, [''])):
        if name != '':
            working_group.add(name)
        elif len(working_group) > 0:
            yield tuple(sorted(working_group))
            working_group = set()


def print_groups_file(groups, file=None):
    """Print out a groups file.

    >>> print_groups_file([('A', 'B'), ('C', None)])
    A
    B
    <BLANKLINE>
    C
    """
    print('\n\n'.join('\n'.join(student for student in group
                                if student is not None) for group in groups), file=file)
