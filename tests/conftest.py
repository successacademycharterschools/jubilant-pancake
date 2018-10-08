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


lipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
    "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex " \
    "ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat " \
    "nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim " \
    "id est laborum."


lipshort = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
    "dolore magna aliqua. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat " \
    "nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim " \
    "id est laborum."


edit_distance_test_data = [
    ('a', 'a', 0),
    ('a', 'aa', 1),
    ('aa', 'a', 1),
    ('aoe', 'aee', 1),
    ('aaaa', 'aaaa', 0),
    ('foo bar baz', 'foobarbaz', 2),
    ('foo bar baz', 'foo barbaz', 1),
    ('foo bar baz', 'foo barbas', 2),
    ('foo bar baz', 'foo  barbas', 3),
    (lipsum, lipshort, 108),
    (lipsum * 10, lipshort * 10, 1080)
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
