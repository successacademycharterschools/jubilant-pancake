import pytest
from flask import url_for
from ..main import create_app


@pytest.fixture
def app():
    app = create_app()
    return app