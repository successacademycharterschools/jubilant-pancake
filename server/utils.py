class memoized(object):
    '''
    Memoization decorator

    Cache our function call response by input values so that we don't have to
    recompute an insane number of times in recursive scenarios.
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]


@memoized
def med(str1, str2):
    '''
    A quick and dirty minimum edit distance algorithm.

    Note that this does not attempt alignment.
    '''
    len1 = len(str1)
    len2 = len(str2)

    if len1 == 0:
        return len2
    elif len2 == 0:
        return len1

    distance = min(med(str1[:-1], str2) + 1,
                   med(str1, str2[:-1]) + 1,
                   med(str1[:-1], str2[:-1]) + (int(str1[-1] != str2[-1]) * 2))

    return distance
