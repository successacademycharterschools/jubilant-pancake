import pytest
from editd import edit_distance


@pytest.mark.parametrize(
    ['source', 'target', 'distance'],
    [
        ('a', 'a', 0),
        ('a', 'aa', 1),
        ('aa', 'a', 1),
        ('aoe', 'aee', 1),
        ('aaaa', 'aaaa', 0),
        ('foo bar baz', 'foobarbaz', 2),
        ('foo bar baz', 'foo barbaz', 1),
        ('foo bar baz', 'foo barbas', 2),
        ('foo bar baz', 'foo  barbas', 3)
    ]
)
def test_edit_distance(source, target, distance):
    """Edit distance is correct for known strings"""
    observed = edit_distance(source, target)
    assert observed == distance, \
        "Strings {} and {} should have edit distance {}; got {}".format(
            source, target, distance, observed
        )
