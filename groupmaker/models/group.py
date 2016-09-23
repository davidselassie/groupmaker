"""Definition of a group."""
from typing import Iterable

from ._util_functions import find_duplicates


class Group:
    """A single, specific set of students.

    Ordering doesn't matter in a group.

    Treat as immutable.
    """

    def __init__(self, *names: Iterable[str]) -> None:
        """Make a new group.

        >>> group = Group('A', 'B')
        >>> group.names
        ('A', 'B')
        >>> group = Group('B', 'A')
        >>> group.names
        ('A', 'B')
        >>> Group('A', 'A')
        Traceback (most recent call last):
            ...
        ValueError: duplicate names in group: ['A']
        """
        duplicate_names = sorted(find_duplicates(names))
        if len(duplicate_names) > 0:
            raise ValueError(
                'duplicate names in group: {!r}'.format(duplicate_names)
            )
        self.names = tuple(sorted(names))

    def __eq__(self, other: 'Group') -> bool:
        """Return if groups are equal.

        >>> Group('A') == Group('A')
        True
        >>> Group('A', 'B') == Group('B', 'A')
        True
        >>> Group('A') == Group('B')
        False
        """
        return self.names == other.names

    def __hash__(self):
        return hash(self.names)

    def __lt__(self, other: 'Group') -> bool:
        """Return if a current group is before other group.

        >>> Group('A', 'B') < Group('A', 'C')
        True
        >>> Group('B', 'C') < Group('A', 'C')
        False
        """
        return self.names < other.names

    def __repr__(self) -> str:
        """Return the literal of a group.

        >>> repr(Group('A', 'B'))
        "Group('A', 'B')"
        >>> repr(Group())
        'Group()'
        """
        name_arg_list = ', '.join(repr(name) for name in self.names)
        return 'Group({})'.format(name_arg_list)
