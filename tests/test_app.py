"""Tests for the edit distance web service"""

import pytest
from .data import edit_distance_test_data
from main import create_app
from flask import request


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.mark.parametrize(
    ['source', 'target', 'distance'],
    edit_distance_test_data
)
def test_app(client, source, target, distance):
    """Correct distances are returned when accessing the API endpoint with path syntax"""
    resp = client.get('/editd/{}/{}'.format(source, target))
    assert resp.status_code == 200
    assert int(resp.data) == distance, \
        "For strings {}/{}, app returned {} (should be {})".format(
            source, target, resp.data, distance
        )


@pytest.mark.parametrize(
    ['source', 'target', 'distance'],
    edit_distance_test_data
)
def test_app_request(client, source, target, distance):
    """Correct distances are returned when accessing the API endpoint with keyword syntax"""
    resp = client.get('/editd?source={}&target={}'.format(source, target))
    assert request.args['source'] == source
    assert request.args['target'] == target
    assert resp.status_code == 200
    assert int(resp.data) == distance, \
        "For strings {}/{}, app returned {} (should be {})".format(
            source, target, resp.data, distance
        )


def test_app_invalid(client):
    """500 error is returned when lacking source or target"""
    assert client.get('/editd?source=foo').status_code == 500
    assert client.get('/editd?target=bar').status_code == 500
    assert client.get('/editd?aoeu=dhts').status_code == 500
    assert client.get('/editd').status_code == 500
