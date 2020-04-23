from http import HTTPStatus


class TestApp:
    URL = '/'

    def test_index_successful(self, app):
        rv = app.get(self.URL)
        assert rv.status_code == HTTPStatus.OK

    def test_index_other_methods_not_allowed(self, app):
        expected_status = HTTPStatus.METHOD_NOT_ALLOWED

        for method in ('post', 'patch', 'put', 'options', 'delete'):
            func = getattr(app, method)
            rv = func(self.URL, status=expected_status)
            assert rv.status_code == expected_status
