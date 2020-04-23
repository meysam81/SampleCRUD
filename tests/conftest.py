import pytest

from unittest.mock import patch
from webtest import TestApp


from medium.config import TestingConfig


@pytest.fixture
def db():
    """Application ORM Database"""


@pytest.yield_fixture
def app():
    """Flask Test App"""
    with patch('medium.app.db'):
        from medium.app import create_app

        app = create_app(TestingConfig)

        ctx = app.test_request_context()

        ctx.push()
        yield TestApp(app)
        ctx.pop()
