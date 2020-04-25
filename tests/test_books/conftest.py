import pytest

from unittest.mock import patch


@pytest.fixture
def Book():
    return patch('medium.books.views.Book').start()


@pytest.fixture
def books_db():
    """db object inside books app"""
    return patch('medium.books.views.db').start()
