import pytest

from webtest import TestApp
from unittest.mock import patch


from medium.config import TestingConfig


@pytest.fixture
def Book():
    return patch('medium.books.views.Book').start()


@pytest.yield_fixture
def app():
    """Flask Test App"""
    with patch('flask_sqlalchemy.SQLAlchemy'):
        from medium.app import create_app

        app = create_app(TestingConfig)

        ctx = app.test_request_context()

        ctx.push()
        yield TestApp(app)
        ctx.pop()
