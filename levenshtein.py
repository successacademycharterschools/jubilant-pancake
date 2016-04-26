def levenshtein(a, b):
    """
    Calculates the edit distance between a and b.

    Credit to http://hetland.org/coding/python/levenshtein.py
    (with minor adjustments and error checking)
    """

    if a is None and b is None:
        # two values are required to compute the edit distance
        raise TypeError("Two strings must be provided")

    if a == b:
        return 0
    elif len(a) == 0:
        return len(b)
    elif len(b) == 0:
        return len(a)

    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n

    current = xrange(n + 1)
    for i in xrange(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in xrange(1, n + 1):
            add, delete = previous[j] + 1, current[j - 1] + 1
            change = previous[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current[j] = min(add, delete, change)

    return current[n]
