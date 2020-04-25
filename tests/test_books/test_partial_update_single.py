from http import HTTPStatus


class TestPartialUpdateSingle:
    URL = "/api/v1/books/{}"

    def test_partial_update_non_json_bad_request(self, app):
        expected_status = HTTPStatus.BAD_REQUEST
        rv = app.patch(self.URL.format(1), status=expected_status)

        assert rv.status_code == expected_status

    def test_partial_update_not_found(self, Book, app, books_db):
        Book.query.filter_by.return_value.update.return_value = None

        expected_status = HTTPStatus.NOT_FOUND
        book = {"bookName": "book1"}
        rv = app.patch_json(self.URL.format(1), book, status=expected_status)

        assert rv.status_code == expected_status

        Book.query.filter_by.assert_called_once()
        Book.query.filter_by.return_value.update.assert_called_once()

        books_db.session.commit.assert_called_once()

    def test_partial_update_succesful(self, Book, app, books_db):
        name, id_ = "book1", 1
        book = {"bookName": name}
        db_book = Book(id=id_, name=name)

        Book.query.filter_by.return_value.update.return_value = db_book

        rv = app.patch_json(self.URL.format(1), book)

        assert rv.status_code == HTTPStatus.ACCEPTED
        assert rv.content_type == "application/json"

        Book.query.filter_by.assert_called_once()
        Book.query.filter_by.return_value.update.assert_called_once()

        books_db.session.commit.assert_called_once()
