"""Common test fixtures and configuration"""


import pytest
from main import create_app


@pytest.fixture
def app():
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


@pytest.fixture(params=edit_distance_test_data)
def distances(request):
    return request.param
