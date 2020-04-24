from http import HTTPStatus
from operator import itemgetter


class TestGetAll:
    URL = '/api/v1/books'

    def test_other_methods_not_allowed(self, app):
        expected_status = HTTPStatus.METHOD_NOT_ALLOWED

        for method in ('patch', 'put', 'delete', 'options'):
            func = getattr(app, method)
            rv = func(self.URL, status=expected_status)
            assert rv.status_code == expected_status

    def test_get_all_books_empty_db(self, Book, app):
        books = []

        Book.query.all.return_value = books

        rv = app.get(self.URL)

        assert rv.status_code == HTTPStatus.OK
        assert rv.content_type == "application/json"
        assert len(rv.json) == 0

        Book.query.all.assert_called_once()

    def test_get_all_books_populated_db(self, Book, app):
        books = [
            (1, "book1"),
            (2, "book2"),
            (3, "book3"),
        ]
        db_books = [Book(id=k, name=v) for k, v in books]

        Book.query.all.return_value = db_books

        rv = app.get(self.URL)

        assert rv.status_code == HTTPStatus.OK
        assert rv.content_type == "application/json"
        for item in rv.json:
            assert item["id"] in map(itemgetter(0), books)

        Book.query.all.assert_called_once()
