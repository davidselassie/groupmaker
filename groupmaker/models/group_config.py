"""Definition of a group config."""
from itertools import chain

from ._util_functions import find_duplicates
from .group import Group


class GroupConfig:
    """A set of groups that together include all students.

    Treat as immutable.
    """

    def __init__(self, *groups):
        """Make a new group config.

        >>> group_config = GroupConfig(Group('A'), Group('B'))
        >>> group_config.groups
        (Group('A'), Group('B'))
        >>> group_config = GroupConfig(Group('B'), Group('A'))
        >>> group_config.groups
        (Group('A'), Group('B'))
        >>> GroupConfig(Group('A', 'B'), Group('A'))
        Traceback (most recent call last):
            ...
        ValueError: duplicate names across groups in group config: ['A']
        """
        all_names = chain.from_iterable(group.names for group in groups)
        duplicate_names = sorted(find_duplicates(all_names))
        if len(duplicate_names) > 0:
            raise ValueError(
                'duplicate names across groups in group config: {!r}'.format(
                    duplicate_names
                )
            )
        self.groups = tuple(sorted(groups))

    def __eq__(self, other):
        """Return if group configs are equal.

        >>> GroupConfig(Group('A')) == GroupConfig(Group('A'))
        True
        >>> GroupConfig(Group('A'), Group('B')) == GroupConfig(Group('B'), Group('A'))
        True
        >>> GroupConfig(Group('A')) == GroupConfig(Group('B'))
        False
        """
        return self.groups == other.groups

    def __hash__(self):
        return hash(self.groups)

    def __lt__(self, other):
        """Return if a current group config is before other group config.

        >>> GroupConfig(Group('A'), Group('B')) < GroupConfig(Group('A'), Group('C'))
        True
        >>> GroupConfig(Group('A'), Group('D')) < GroupConfig(Group('A'), Group('C'))
        False
        """
        return self.groups < other.groups

    def __repr__(self):
        """Return the literal of a group config.

        >>> repr(GroupConfig(Group('A', 'B'), Group('C')))
        "GroupConfig(Group('A', 'B'), Group('C'))"
        >>> repr(GroupConfig())
        'GroupConfig()'
        """
        group_arg_list = ', '.join(repr(group) for group in self.groups)
        return 'GroupConfig({})'.format(group_arg_list)
