from http import HTTPStatus


class TestDeleteSingle:
    URL = "/api/v1/books/{}"

    def test_delete_single_not_found(self, Book, app, books_db):
        Book.query.filter_by.return_value.delete.return_value = None

        expected_status = HTTPStatus.NOT_FOUND
        rv = app.delete(self.URL.format(1), status=expected_status)

        assert rv.status_code == expected_status

        Book.query.filter_by.assert_called_once()
        Book.query.filter_by.return_value.delete.assert_called_once()

        books_db.session.commit.assert_called_once()

    def test_delete_single_successful(self, Book, app, books_db):
        Book.query.filter_by.return_value.delete.return_value = 1

        rv = app.delete(self.URL.format(1))

        assert rv.status_code == HTTPStatus.NO_CONTENT

        Book.query.filter_by.assert_called_once()
        Book.query.filter_by.return_value.delete.assert_called_once()

        books_db.session.commit.assert_called_once()
