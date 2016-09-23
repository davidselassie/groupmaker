"""Definition of a summary of pair counts."""
from collections import Counter
from typing import Iterable
from typing import Tuple

from .pair import Pair


class PairCounts:
    """A summary of the number of times various unique pairs have existed.

    Treat as immutable.
    """

    def __init__(self, *pair_counts: Iterable[Tuple[Pair, int]]) -> None:
        """Make a new pair count.

        >>> pair_counts = PairCounts((Pair('A', 'A'), 1), (Pair('A', 'B'), 2))
        >>> pair_counts._counter.get(Pair('A', 'A'))
        1
        >>> pair_counts._counter.get(Pair('A', 'B'))
        2
        """
        self._counter = Counter(dict(pair_counts))

    def __eq__(self, other: 'PairCounts') -> bool:
        """Return if pair counts are equal.

        >>> PairCounts((Pair('A', 'A'), 1)) == PairCounts((Pair('A', 'A'), 1))
        True
        >>> PairCounts((Pair('A', 'A'), 1)) == PairCounts((Pair('B', 'B'), 1))
        False
        """
        return self._counter == other._counter

    def __hash__(self):
        return hash(self._counter)

    def __add__(self, other: 'PairCounts') -> 'PairCounts':
        """Sum together two pair counts, pair by pair.

        >>> (PairCounts((Pair('A', 'A'), 1), (Pair('A', 'B'), 1)) +
        ...  PairCounts((Pair('A', 'B'), 1), (Pair('B', 'B'), 1)))
        PairCounts((Pair('A', 'A'), 1), (Pair('A', 'B'), 2), (Pair('B', 'B'), 1))
        """
        sum_counts = PairCounts()
        sum_counts._counter = self._counter + other._counter
        return sum_counts

    def __repr__(self) -> str:
        """Return the literal of a pair count.

        >>> repr(PairCounts((Pair('A', 'A'), 1), (Pair('A', 'B'), 1)))
        "PairCounts((Pair('A', 'A'), 1), (Pair('A', 'B'), 1))"
        >>> repr(PairCounts())
        'PairCounts()'
        """
        pair_count_arg_list = ', '.join(
            repr(item) for item in sorted(self._counter.items())
        )
        return 'PairCounts({})'.format(pair_count_arg_list)

    def get_count(self, pair: Pair) -> int:
        """

        >>> pair_counts = PairCounts((Pair('A', 'A'), 1), (Pair('A', 'B'), 2))
        >>> pair_counts.get_count(Pair('A', 'A'))
        1
        >>> pair_counts.get_count(Pair('B', 'B'))
        0
        """
        return self._counter[pair]
