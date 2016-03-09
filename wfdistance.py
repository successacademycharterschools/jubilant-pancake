"""
This is our edit distance calculator.

It uses which uses the Wagner & Fischer_algorithm

See https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm
"""


def distance(s, t):
    """Simple edit distance calculation.

    PS: The cost of insert, delete & substitution is assumed to be (1).
    PPS: variable names were chosen to match the algorithm 'description'
    """
    # handle simple case
    if s == t:
        return 0
    m, n = len(s), len(t)
    # handle another simple case if either string is empty
    if m == 0 or n == 0:
        return max(m, n)

    # create & populate the 2-D Array with 0s
    dist = [[0 for col in range(n + 1)] for row in range(m + 1)]
    for i in range(m):
        dist[i + 1][0] = dist[i][0] + 1
    for j in range(n):
        dist[0][j + 1] = dist[0][j] + 1

    for j in range(n):
        for i in range(m):
            if s[i] == t[j]:
                dist[i + 1][j + 1] = dist[i][j]
            else:
                dist[i + 1][j + 1] = min(dist[i + 1][j] + 1,
                                         dist[i][j + 1] + 1,
                                         dist[i][j] + 1)
    return dist[m][n]
