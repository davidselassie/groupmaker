"""Definition of a student set."""
from ._util_functions import find_duplicates


class Students:
    """Set of all students in a class.

    Treat as immutable.
    """

    def __init__(self, *names):
        """Make a new set of students.

        >>> students = Students('A', 'B')
        >>> students.names
        ('A', 'B')
        >>> students = Students('B', 'A')
        >>> students.names
        ('A', 'B')
        >>> Students('A', 'A')
        Traceback (most recent call last):
            ...
        ValueError: duplicate names in students: ['A']
        """
        duplicate_names = sorted(find_duplicates(names))
        if len(duplicate_names) > 0:
            raise ValueError('duplicate names in students: {!r}'.format(duplicate_names))
        self.names = tuple(sorted(names))

    def __eq__(self, other):
        """Return if student sets are equal.

        >>> Students('A', 'B') == Students('B', 'A')
        True
        >>> Students('A') == Students('B')
        False
        """
        return self.names == other.names

    def __hash__(self):
        return hash(self.names)

    def __repr__(self):
        """Return the literal of a student set.

        >>> repr(Students('A', 'B'))
        "Students('A', 'B')"
        >>> repr(Students())
        'Students()'
        """
        name_arg_list = ', '.join(repr(name) for name in self.names)
        return 'Students({})'.format(name_arg_list)
