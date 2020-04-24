from http import HTTPStatus


class TestGetSingle:
    URL = "/api/v1/books/{}"

    def test_other_methods_not_allowed(self, app):
        expected_status = HTTPStatus.METHOD_NOT_ALLOWED
        for method in ("post", "options", "put"):
            func = getattr(app, method)
            rv = func(self.URL.format(1), status=expected_status)

            assert rv.status_code == expected_status

    def test_get_single_not_found(self, Book, app):
        Book.query.filter_by.return_value.first.return_value = None

        expected_status = HTTPStatus.NOT_FOUND
        rv = app.get(self.URL.format(1), status=expected_status)

        assert rv.status_code == expected_status

    def test_get_single_successful(self, Book, app):
        id_ = 1

        book = Book(id=id_, name="book1")
        Book.query.filter_by.return_value.first.return_value = book

        rv = app.get(self.URL.format(id_))

        assert rv.status_code == HTTPStatus.OK
        assert rv.content_type == "application/json"
        assert rv.json["id"] == id_

        Book.query.filter_by.assert_called_once()
        Book.query.filter_by.return_value.first.assert_called_once()
