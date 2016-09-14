from functools import reduce
from itertools import combinations_with_replacement, filterfalse


def _is_none(x):
    """Return if a variable is None.

    >>> _is_none('A')
    False
    >>> _is_none(None)
    True
    """
    return x is None


def _pairs(group):
    """Given a group of people, return a tuple pairs generator.

    Nones are ignored in the group.
    Tuple pairs are only emitted in sorted order.

    >>> list(_pairs(['A', 'B']))
    [('A', 'A'), ('A', 'B'), ('B', 'B')]
    >>> list(_pairs(['A', None]))
    [('A', 'A')]
    >>> list(_pairs(['B', 'A']))
    [('A', 'A'), ('A', 'B'), ('B', 'B')]
    >>> list(_pairs(['A', 'C', 'B', None]))
    [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
    """
    group_without_nones = filterfalse(_is_none, group)
    sorted_group = sorted(group_without_nones)
    pair_lists = combinations_with_replacement(sorted_group, 2)
    pair_tuples = map(tuple, pair_lists)
    return pair_tuples


def calc_pair_to_count_of_group(group):
    """Given a group return that each pair was grouped together once.

    Only the sorted pairs are keys.

    >>> sorted(calc_pair_to_count_of_group(['A', 'B']).items())
    [(('A', 'A'), 1), (('A', 'B'), 1), (('B', 'B'), 1)]
    """
    return {pair: 1 for pair in _pairs(group)}


def _sum_count_dict(count_dict1, count_dict2):
    """Sum two dicts from key to count by unique key.

    >>> sorted(_sum_count_dict({'A': 1, 'B': 1}, {'B': 1, 'C': 3}).items())
    [('A', 1), ('B', 2), ('C', 3)]
    """
    out_count_dict = dict(count_dict1)
    for key, sum_num in count_dict2.items():
        if key not in out_count_dict:
            out_count_dict[key] = 0
        out_count_dict[key] += sum_num
    return out_count_dict


def calc_pair_to_count_of_groups(groups):
    """Count how often each pair exists in some groups.

    Only the sorted pairs are keys.

    >>> sorted(calc_pair_to_count_of_groups([['A', 'B'], ['A']]).items())
    [(('A', 'A'), 2), (('A', 'B'), 1), (('B', 'B'), 1)]
    """
    return reduce(_sum_count_dict, map(calc_pair_to_count_of_group, groups))


def calc_pair_to_count_of_groups_set(groups_set):
    """Count how often each pair exists in a set of groups.

    >>> sorted(calc_pair_to_count_of_groups_set(
    ...     [[['A'], ['B']], [['A', 'B']]]).items())
    [(('A', 'A'), 2), (('A', 'B'), 1), (('B', 'B'), 2)]
    """
    return reduce(_sum_count_dict,
                  map(calc_pair_to_count_of_groups, groups_set),
                  {})


def score_group(group, historical_pair_to_count):
    """Given a group and a historical pair counts, return a score of how many times group members have been paired
    together before.

    The higher the score, the more frequently they've been grouped together.

    >>> score_group(
    ...     ['A', 'B', 'C'],
    ...     {('A', 'B'): 1, ('A', 'C'): 1})
    4
    """
    return sum(
        historical_pair_to_count.get(pair, 0)
        for pair
        in _pairs(group)
    ) ** 2


def score_groups(groups, historical_pair_to_count):
    """Given a set of groups and a historical pair counts, return a score of how many times group members have been paired
    together before

    The higher the score, the more frequently they've been grouped together.

    >>> score_groups(
    ...     [['A', 'B'], ['C', 'D']],
    ...     {('A', 'B'): 1, ('C', 'D'): 1})
    2
    """
    return sum(score_group(group, historical_pair_to_count)
               for group in groups)


def find_min_scoring_groups(groups_set, historical_pair_to_count):
    """Given a list of possible groups and historical pair counts, return which
    has the minimum score.

    >>> find_min_scoring_groups(
    ...     [[['A', 'B'], ['C', 'D']], [['A', 'C'], ['D', 'B']]],
    ...     {('A', 'B'): 2, ('B', 'D'): 1})
    [['A', 'C'], ['D', 'B']]
    """
    def _score_groups_with_historical_pair_counts(groups):
        return score_groups(groups, historical_pair_to_count)

    return min(groups_set, key=_score_groups_with_historical_pair_counts)
