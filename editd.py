"""Functions for computing edit distance

Currently this exports only the ``edit_distance`` function, which calculates
Levenshtein distance

"""


def edit_distance(a, b):
    """Compute the Levenshtein distance to edit ``a`` so it equals ``b``"""
    d = [[]] * (len(a) + 1)
    # fill the edges with the possibility of inserting/dropping all characters
    for i in range(len(a)+1):
        d[i] = [i] + [0] * (len(b))
    for j in range(len(b)+1):
        d[0][j] = j
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            d[i][j] = min((
                d[i-1][j] + 1,  # deletion
                d[i][j-1] + 1,  # insertion
                d[i-1][j-1] + (
                    0 if a[i-1] == b[j-1] else 1  # substitution
                )
            ))
    return d[-1][-1]


__all__ = ['edit_distance']
