"""Utils for Jubilant Pancake project"""


def wagner_fisher(string_1, string_2):
    """A method to calculate the minimum edit distance (Levenshtein Distance
       for two strings"""
    diff = {}
    # For efficiency's sake, make sure string_1 is longer than string_2
    if len(string_1) > len(string_2):
        string_1, string_2 = string_2, string_1
    # Initialize tracking array/dict:
    for i in range(-1, len(string_1) + 1):
        diff[(i, -1)] = i + 1
    for j in range(-1, len(string_2) + 1):
        diff[(-1, j)] = j + 1

    for i in range(len(string_1)):  # pylint: disable=consider-using-enumerate
        # pylint: disable=consider-using-enumerate
        for j in range(len(string_2)):
            if string_1[i] == string_2[j]:
                # If the two characters are the same, do not update distance
                diff[i, j] = diff[i - 1, j - 1]
            else:
                # We want to find the shortest distance, so we need to find
                # the minimum of three possible options:
                # 1) Substitution: check i-1, j-1
                # 2) Insertion: check i, j-1
                # 3) Deletion: check i-1, j
                # After finding the minimum, add 1 for the new operation
                diff[(i, j)] = min(
                    diff[(i-1, j)], diff[(i, j-1)], diff[(i - 1, j - 1)]
                ) + 1
    return diff[len(string_1) - 1, len(string_2) - 1]
