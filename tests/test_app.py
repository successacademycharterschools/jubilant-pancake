import pytest
from .data import edit_distance_test_data
from main import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.mark.parametrize(
    ['source', 'target', 'distance'],
    edit_distance_test_data
)
def test_app(client, source, target, distance):
    resp = client.get('/{}/{}'.format(source, target))
    assert resp.status_code == 200
    assert int(resp.data) == distance, \
        "For strings {}/{}, app returned {} (should be {})".format(
            source, target, resp.data, distance
        )
