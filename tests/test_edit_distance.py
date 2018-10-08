"""Tests for the core edit distance function"""

from editd import edit_distance


def test_edit_distance(distances):
    """Edit distance is correct for known strings"""
    source, target, distance = distances
    observed = edit_distance(source, target)
    assert observed == distance, \
        "Strings {} and {} should have edit distance {}; got {}".format(
            source, target, distance, observed
        )
