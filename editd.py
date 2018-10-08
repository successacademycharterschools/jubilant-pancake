"""Functions for computing edit distance

Currently this exports only the ``edit_distance`` function, which is a
hinted implementation of the Levenshtein algorithm.

"""


def _edit_distance_recursive(a, b, i, j):
    if min((i, j)) == 0:
        ret = _edit_distance_recursive.hint[a, b, i, j] = max((i, j))
        return ret
    if (a, b, i, j) not in _edit_distance_recursive.hint:
        _edit_distance_recursive.hint[a, b, i, j] = min((
            _edit_distance_recursive(a, b, i - 1, j) + 1,
            _edit_distance_recursive(a, b, i, j - 1) + 1,
            _edit_distance_recursive(a, b, i - 1, j - 1) + (
                0 if a[i - 1] == b[j - 1] else 1
            )
        ))
    return _edit_distance_recursive.hint[a, b, i, j]


_edit_distance_recursive.hint = {}


def edit_distance(a, b):
    """Hinted Levenshtein algorithm for edit distance"""
    if (a, b, len(a), len(b)) not in _edit_distance_recursive.hint:
        for i in reversed(range(min((len(a)-1, len(b)-1)), -1, -1)):
            _edit_distance_recursive(a, b, len(a)-i, len(b)-i)
    return _edit_distance_recursive.hint[a, b, len(a), len(b)]


__all__ = ['edit_distance']
