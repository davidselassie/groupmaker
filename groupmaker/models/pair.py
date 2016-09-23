"""Definition of a pair."""


class Pair:
    """A pairing of people.

    Ordering doesn't matter in a pair.
    You can be paired with yourself.

    Treat as immutable.
    """

    def __init__(self, name_a: str, name_b: str) -> None:
        """Make a new pair.

        >>> pair = Pair('A', 'B')
        >>> pair.names
        ('A', 'B')
        >>> pair = Pair('B', 'A')
        >>> pair.names
        ('A', 'B')
        """
        self.names = tuple(sorted((name_a, name_b)))

    def __eq__(self, other: 'Pair') -> bool:
        """Return if pairs are equal.

        >>> Pair('A', 'B') == Pair('B', 'A')
        True
        >>> Pair('A', 'B') == Pair('A', 'A')
        False
        """
        return self.names == other.names

    def __hash__(self):
        return hash(self.names)

    def __lt__(self, other: 'Pair') -> bool:
        """Return if a current pair is before other pair.

        >>> Pair('A', 'B') < Pair('A', 'C')
        True
        >>> Pair('B', 'B') < Pair('A', 'C')
        False
        """
        return self.names < other.names

    def __repr__(self) -> str:
        """Return the literal of a pair.

        >>> repr(Pair('A', 'B'))
        "Pair('A', 'B')"
        """
        return 'Pair({!r}, {!r})'.format(*self.names)
