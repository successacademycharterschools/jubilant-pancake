import pytest
from editd import edit_distance
from .data import edit_distance_test_data


@pytest.mark.parametrize(
    ['source', 'target', 'distance'],
    edit_distance_test_data
)
def test_edit_distance(source, target, distance):
    """Edit distance is correct for known strings"""
    observed = edit_distance(source, target)
    assert observed == distance, \
        "Strings {} and {} should have edit distance {}; got {}".format(
            source, target, distance, observed
        )
