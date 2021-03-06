from http import HTTPStatus


class TestCreate:
    URL = "/api/v1/books"

    def test_non_json_results_bad_request(self, app):
        expected_status = HTTPStatus.BAD_REQUEST
        rv = app.post(self.URL, status=expected_status)
        assert rv.status_code == expected_status

    def test_create_book_successful(self, Book, app, books_db):
        book = {
            "bookName": "book1",
        }

        rv = app.post_json(self.URL, book)

        assert rv.status_code == HTTPStatus.CREATED

        books_db.session.add.assert_called_once()
        books_db.session.commit.assert_called_once()
