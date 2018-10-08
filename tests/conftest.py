"""Common test fixtures and data"""


import pytest
from main import create_app


@pytest.fixture
def app():
    """Fixture for the Flask app for edit distance

    This shouldn't be used directly. Use the ``client`` fixture instead.

    """
    app = create_app()
    return app


edit_distance_test_data = [
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
"""3-tuples of known edit distances

In the form (source, target, distance)

"""


@pytest.fixture(params=edit_distance_test_data)
def distances(request):
    """Fixture for known edit distances

    When used, it will be a different 3-tuple of (source, target, distance)
    for each run of the test.

    """
    return request.param
