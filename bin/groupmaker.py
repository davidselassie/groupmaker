#!/usr/bin/env python3
"""Make student groups, ensuring that students work with those they have worked
with the fewest times before.
"""
import argparse
import sys

from groupmaker.file_io import parse_students_file, parse_groups_file_paths, print_groups_file
from groupmaker.generation import all_groups_set
from groupmaker.scoring import calc_pair_to_count_of_groups_set, find_min_scoring_groups
from groupmaker.table import calc_print_name_count_matrix


def gen_min_scoring_groups(students, group_size, historical_groups_set):
    """Figure out what is the minimum-scoring group out of all possible groups
    of some students.

    >>> gen_min_scoring_groups(
    ...     ['A', 'B', 'C'],
    ...     2,
    ...     [[['A', 'B']], [['B', 'C']]])
    [['A', 'C'], ['B', None]]
    """
    return find_min_scoring_groups(
        all_groups_set(students, group_size),
        calc_pair_to_count_of_groups_set(historical_groups_set))


def main(students_file_path, group_size, historical_groups_file_paths,
         verbosity):
    """Read a list of students, a requested group size, and historical groups,
    then generate a new group of the requested size with the fewest students
    that have worked together before.
    """
    with open(students_file_path) as students_file:
        students = parse_students_file(students_file)
    historical_groups_set = list(parse_groups_file_paths(
        historical_groups_file_paths))

    if verbosity > 0:
        calc_print_name_count_matrix(students, historical_groups_set, file=sys.stderr)

    min_scoring_groups = gen_min_scoring_groups(students, group_size,
                                                historical_groups_set)
    print_groups_file(min_scoring_groups)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-n',
        dest='group_size',
        metavar='GROUP_SIZE',
        type=int,
        default=3,
        help='form groups of this many students (default: %(default)s)')
    parser.add_argument(
        '-v',
        dest='verbosity',
        action='count',
        default=0,
        help='print out historical pair counts to stderr before calculating '
             'new groups')
    parser.add_argument('student_file_path',
                        metavar='STUDENT_FILE',
                        help='file containing student names, one per line')
    parser.add_argument(
        'historical_groups_file_paths',
        metavar='GROUP_FILE',
        nargs='*',
        help='files containing previous groups, one student per line, one '
        'blank line between groups')

    args = parser.parse_args()
    main(args.student_file_path, args.group_size,
         args.historical_groups_file_paths, args.verbosity)
